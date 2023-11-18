import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Hilbert Curve parameters
order = 5  # Adjust the order as needed
size = 1.0
points = []

# Function to generate Hilbert Curve points recursively
def hilbert_curve(x, y, xi, xj, yi, yj, n):
    if n <= 0:
        # Base case: Append the calculated point
        points.append((x + (xi + yi) / 2, y + (xj + yj) / 2))
    else:
        # Step 3: Recursive cases for each quadrant
        hilbert_curve(x, y, yi / 2, yj / 2, xi / 2, xj / 2, n - 1)  # Visit the sub-square in a specific order
        hilbert_curve(x + xi / 2, y + xj / 2, xi / 2, xj / 2, yi / 2, yj / 2, n - 1)  # Recursively apply the process
        hilbert_curve(x + xi / 2 + yi / 2, y + xj / 2 + yj / 2, xi / 2, xj / 2, yi / 2, yj / 2, n - 1)  # Recursively apply the process
        hilbert_curve(x + xi / 2 + yi, y + xj / 2 + yj, -yi / 2, -yj / 2, -xi / 2, -xj / 2, n - 1)  # Visit the sub-square in a specific order

# Function to draw the Hilbert Curve using OpenGL
def draw_hilbert_curve():
    global points
    points = []  # Clear points

    # Step 1: Start with a square
    hilbert_curve(-size / 2, -size / 2, size, 0, 0, size, order)

    glBegin(GL_LINE_STRIP)
    for point in points:
        glVertex2fv(point)
    glEnd()

# Main function to set up GLFW, create a window, and run the rendering loop
def main():
    if not glfw.init():
        return

    # Create a window
    window = glfw.create_window(512, 512, "Hilbert Curve", None, None)
    if not window:
        # If window creation fails, terminate GLFW and return
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set up OpenGL projection matrix for 2D
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-size / 2, size / 2, -size / 2, size / 2)
    glMatrixMode(GL_MODELVIEW)

    # Main rendering loop
    while not glfw.window_should_close(window):
        # Poll for events (e.g., window close events)
        glfw.poll_events()

        # Clear the color buffer
        glClear(GL_COLOR_BUFFER_BIT)

        # Set drawing color to white
        glColor3f(1.0, 1.0, 1.0)
        
        # Step 4: Draw the Hilbert Curve
        draw_hilbert_curve()

        # Swap front and back buffers to display the rendered content
        glfw.swap_buffers(window)

    # Terminate GLFW when the window is closed
    glfw.terminate()

# Check if the script is the main module and execute the main function
if __name__ == "__main__":
    main()
