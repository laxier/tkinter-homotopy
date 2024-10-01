# Laboratory 3: Advanced Animation

## Objective
The goal of this lab is to apply acquired skills in graphics and animation to tackle more complex projects. Each task requires thoughtful program structuring and design.

## Execution Order
Tasks must be completed individually, assigned randomly by the instructor. Students can request clarifications on task requirements or underlying mathematical concepts during seminars. A creative approach is essential, as tasks provide only a general outline, allowing students to make design choices regarding animation speed, element size, color schemes, etc. Successful design choices will be rewarded, while unsuccessful ones may lower the grade.

Many tasks involve mastering mathematical concepts necessary for task understanding and execution. Research is crucial in software development. An object-oriented approach is strongly recommended, along with attention to code formatting, style conventions, comments, and readability. Using version control is a plus.
## Circle to Triangle Animation
This animation demonstrates the transformation of a circle into a triangle using polar coordinates. The process involves gradually interpolating the vertices of the circle to form the vertices of a triangle, creating a visually engaging transition.

## Mathematical Concepts
The animation employs several mathematical methods implemented in the `MathUtils` class:

## Circle to Triangle Animation
This animation demonstrates the transformation of a circle into a triangle using polar coordinates. The process involves gradually interpolating the vertices of the circle to form the vertices of a triangle, creating a visually engaging transition.

### Mathematical Concepts
The animation employs several mathematical methods implemented in the `MathUtils` class:

1. **Vertex Calculation**: 
   - The `P(n, j)` method returns the coordinates of the j-th vertex of a regular polygon with n sides inscribed in a unit circle.

2. **Interpolation**:
   - The `interpolate(p1, p2, u)` method linearly interpolates between two points `p1` and `p2` based on a parameter `u` (ranging from 0 to 1). This allows for smooth transitions between the vertices of the polygon and the circle.

3. **Screen Coordinate Transformation**:
   - The `to_screen_coords(x, y)` method converts unit circle coordinates into screen coordinates for accurate rendering on a canvas.

## Polygon Class

The `Polygon` class is responsible for managing the drawing and transformation of a polygon on a Tkinter canvas. Below are the key methods of the class:

### Methods

#### `__init__(self, canvas, n, subdivisions=10)`
Initializes the `Polygon` object.

- **Parameters**:
  - `canvas` (tk.Canvas): The canvas where the polygon will be drawn.
  - `n` (int): The number of sides of the polygon.
  - `subdivisions` (int): The number of subdivisions for each edge of the polygon (default is 10).

#### `calculate_points(self, u)`
Calculates the screen coordinates for the polygon's vertices based on the animation parameter.

- **Parameters**:
  - `u` (float): Animation parameter indicating how much the polygon has transformed into a circle (value from 0 to 1).
  
- **Returns**: 
  - `list`: A list of (x, y) coordinates for drawing the polygon.

#### `draw(self, u)`
Renders the polygon on the canvas.

- **Parameters**:
  - `u` (float): Animation parameter (value from 0 to 1) indicating the current state of the animation.
