import tkinter as tk
import math


class MathUtils:
    @staticmethod
    def P(n, j):
        """Возвращает j-ю вершину многоугольника на единичной окружности.

        Args:
            n (int): Количество сторон многоугольника.
            j (int): Индекс текущей вершины.

        Returns:
            tuple: Координаты (x, y) j-й вершины многоугольника.
        """
        return (math.cos(2 * math.pi * j / n), math.sin(2 * math.pi * j / n))

    @staticmethod
    def interpolate(p1, p2, u):
        """Интерполирует между двумя точками p1 и p2 с использованием параметра u.

        Args:
            p1 (tuple): Первая точка в виде кортежа (x1, y1).
            p2 (tuple): Вторая точка в виде кортежа (x2, y2).
            u (float): Параметр интерполяции (число от 0 до 1).

        Returns:
            tuple: Интерполяционная точка между p1 и p2.
        """
        return ((1 - u) * p1[0] + u * p2[0], (1 - u) * p1[1] + u * p2[1])

    @staticmethod
    def to_screen_coords(x, y):
        """Преобразует координаты единичной окружности в экранные координаты.

        Args:
            x (float): Координата по оси x.
            y (float): Координата по оси y.

        Returns:
            tuple: Преобразованные экранные координаты (x, y).
        """
        return (x * 150 + 200, -y * 150 + 200)


class Polygon:
    def __init__(self, canvas, n, subdivisions=10):
        """Инициализирует класс Polygon.

        Args:
            canvas (tk.Canvas): Экземпляр tk.Canvas, на котором будет рисоваться многоугольник.
            n (int): Количество сторон многоугольника.
            subdivisions (int): Количество подделений каждого ребра многоугольника.
        """
        self.canvas = canvas
        self.n = n
        self.subdivisions = subdivisions
        self.original_points = [
            self.canvas.create_oval(0, 0, 0, 0, fill="red") for _ in range(self.n)
        ]
        self.polygon = self.canvas.create_polygon(0, 0, 0, 0, fill="", outline="blue")

    def calculate_points(self, u):
        """Возвращает координаты всех точек многоугольника на экране.

        Args:
            u (float): Параметр анимации, определяющий, насколько многоугольник
                       трансформирован в окружность (число от 0 до 1).

        Returns:
            list: Список координат (x, y) всех точек многоугольника для рисования.
        """
        polygon_points = []
        for k in range(self.n):
            vertex_1 = MathUtils.P(self.n, k)
            vertex_2 = MathUtils.P(self.n, (k + 1) % self.n)

            for i in range(self.subdivisions):
                t = i / self.subdivisions
                edge_point = MathUtils.interpolate(vertex_1, vertex_2, t)
                angle = 2 * math.pi * (k + t) / self.n
                circle_point = (math.cos(angle), math.sin(angle))

                point_pos = MathUtils.interpolate(edge_point, circle_point, u)
                screen_pos = MathUtils.to_screen_coords(*point_pos)
                polygon_points.extend(screen_pos)

                # Обновляем только исходные вершины многоугольника как красные точки
                if i == 0:
                    self.canvas.coords(
                        self.original_points[k],
                        screen_pos[0] - 3, screen_pos[1] - 3,
                        screen_pos[0] + 3, screen_pos[1] + 3,
                    )

        return polygon_points

    def draw(self, u):
        """Отрисовывает многоугольник на канвасе.

        Args:
            u (float): Параметр анимации (число от 0 до 1).
        """
        points = self.calculate_points(u)
        self.canvas.coords(self.polygon, *points)


class PolygonToCircleAnimation(tk.Tk):
    def __init__(self):
        """Инициализирует класс PolygonToCircleAnimation и запускает анимацию."""
        super().__init__()

        self.title("Polygon to Circle Animation")
        self.geometry("400x450")

        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.n = 3  # количество сторон многоугольника
        self.u = 0  # параметр анимации
        self.frame = 0  # текущий кадр анимации
        self.max_frames = 200  # максимальное количество кадров
        self.direction = 1  # направление анимации, 1 вперед, -1 назад

        self.polygon = Polygon(self.canvas, 3)  # Создание объекта Polygon
        self.circle = self.canvas.create_oval(50, 50, 350, 350, outline="red", dash=(5, 5))
        # Нарисовать описанную окружность

        # Создаем текстовые объекты для отображения n и u
        self.text_n = self.canvas.create_text(50, 20, text=f"n: {self.n}", font=("Arial", 12), fill="black")
        self.text_u = self.canvas.create_text(350, 20, text=f"u: {self.u:.2f}", font=("Arial", 12), fill="black")

        # Добавим кнопку "Перезапустить"
        self.restart_button = tk.Button(self, text="Перезапустить", command=self.restart_animation)
        self.restart_button.pack(pady=10)

        self.animate()  # Запуск анимации

    def animate(self):
        """Основной цикл анимации, обновляет состояние анимации и графику.

        Если достигнуто максимальное количество кадров, анимация останавливается.
        """
        if self.frame <= self.max_frames:
            self.u += self.direction * 0.01
            if self.u >= 1 or self.u <= 0:
                self.direction *= -1

            self.polygon.draw(self.u)  # Рисует многоугольник

            # Обновляем текст на экране для n и u
            self.canvas.itemconfig(self.text_n, text=f"n: {self.n}")
            self.canvas.itemconfig(self.text_u, text=f"u: {self.u:.2f}")

            self.frame += 1
            self.after(20, self.animate)  # Повторяем цикл через 20 мс
        else:
            print("Анимация завершена")

    def restart_animation(self):
        """Сбрасывает параметры анимации и перезапускает её."""
        self.u = 0
        self.frame = 0
        self.direction = 1
        self.animate()  # Перезапускаем цикл анимации


if __name__ == "__main__":
    app = PolygonToCircleAnimation()  # Создание экземпляра анимации
    app.mainloop()  # Запуск главного цикла приложения
