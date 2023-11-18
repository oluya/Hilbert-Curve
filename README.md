# Hilbert-Curve
Drawing the Hilbert Curve in OpenGl using Python


The Hilbert curve is a continuous fractal space-filling curve that passes through every point in a square grid exactly once. It was introduced by the German mathematician David Hilbert in 1891 as a way to establish a one-to-one correspondence between points in a one-dimensional space and points in a two-dimensional space.
The key idea is to recursively subdivide a square into smaller squares and then connect the midpoints of the sides in a specific order to form a curve that fills the space. The recursive nature of the construction leads to a curve with interesting properties, including self-similarity.


# Start with a square.
# Divide the square into four equal sub-squares.
# Visit the sub-squares in a specific order, recursively applying the same process within each sub-square.
# Connect the corners of the sub-squares in a specific order to form the curve.
# As the recursion continues, the curve fills the entire square, creating a continuous and space-filling path. 
# The order in which the sub-squares are visited determines the final shape of the Hilbert curve.

**Step 1 **
The hilbert_curve function is the core of the Hilbert Curve generation.
The initial call to this function (hilbert_curve(-size / 2, -size / 2, size, 0, 0, size, order)) starts with a square.
The function calculates and appends points based on the provided parameters.

** Step 2 **
In the recursive calls of the hilbert_curve function, the square is divided into four equal sub-squares.
Each recursive call corresponds to one of the sub-squares.

**Step 3 **
The order in which the sub-squares are visited is determined by the order of the recursive calls.
Each recursive call applies the same process within a sub-square.

** Step 4 **
The draw_hilbert_curve function is responsible for visualizing the constructed Hilbert Curve using OpenGL.
The hilbert_curve function is called with the initial parameters to generate the curve points.
The points are then connected with lines (GL_LINE_STRIP) to form the Hilbert Curve.

**Step 5 **
The main rendering loop ensures that the recursion continues until the specified order (order) is reached.
As the recursion continues, the Hilbert Curve fills the entire square.
This code effectively implements the construction steps of creating the Hilbert Curve, starting from a square and recursively dividing and connecting sub-squares until the entire square is filled with the curve.


