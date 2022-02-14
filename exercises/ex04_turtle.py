"""Attempting to draw a face!"""
__author__ = "730507751"
from turtle import Turtle, colormode, done


def simplified_function(the_turtle: Turtle, x: float, y: float, the_color_of_the_shape: str, the_fill_color: str) -> None:
    """An attempt to prevent the following functions from becoming too complex; transforms the turtle to the given color and x, y coordinates."""
    the_turtle.pencolor(the_color_of_the_shape)
    the_turtle.fillcolor(the_fill_color)
    the_turtle.penup()
    the_turtle.goto(x, y)
    the_turtle.pendown()


def draw_triangle(the_turtle: Turtle, x: float, y: float, width: float, the_color_of_the_shape: str, the_fill_color: str) -> None:
    """Draws a triangle of the given width and colors in the given x, y coordinates; calls the simplified_function."""
    simplified_function(the_turtle, x, y, the_color_of_the_shape, the_fill_color)
    the_turtle.begin_fill()
    i: int = 0
    while i < 3:
        the_turtle.forward(width)
        the_turtle.right(120)
        i = i + 1
    the_turtle.end_fill()


def draw_hexagon(the_turtle: Turtle, x: float, y: float, width: float, the_color_of_the_shape: str, the_fill_color: str) -> None:
    """Draws a hexagon of the given width and colors in the given x, y coordinates; calls the simplified_function."""
    simplified_function(the_turtle, x, y, the_color_of_the_shape, the_fill_color)
    the_turtle.begin_fill()
    i: int = 0
    while i < 6:
        the_turtle.forward(width)
        the_turtle.right(300)
        i = i + 1
    the_turtle.end_fill()


def draw_circle(the_turtle: Turtle, x: float, y: float, radius: int, the_color_of_the_shape: str, the_fill_color: str) -> None:
    """Draws a circle of the given radius and colors in the given x, y coordinates; calls the simplified_function."""
    simplified_function(the_turtle, x, y, the_color_of_the_shape, the_fill_color)
    the_turtle.begin_fill()
    the_turtle.circle(radius)
    the_turtle.end_fill()


def draw_line(the_turtle: Turtle, x: float, y: float, width: int, the_color_of_the_shape: str) -> None:
    """Draws a line of the given width and color in the given x, y coordinates; calls the simplified_function."""
    simplified_function(the_turtle, x, y, the_color_of_the_shape, "")
    the_turtle.forward(width)
 

def main() -> None:
    """The entrypoint of my scene; institutes a turtle object."""
    bob_the_turtle: Turtle = Turtle()
    colormode(255)
    bob_the_turtle.color(99, 204, 250)
    bob_the_turtle.speed(50)
    """Draws a face!"""
    draw_circle(bob_the_turtle, 0.0, 0.0, 100, "black", "pink")
    i: int = 0
    while i < 2:
        if i == 0:
            """Draws the left eye!"""
            draw_hexagon(bob_the_turtle, -55.0, 120.0, 20, "black", "white")
            draw_circle(bob_the_turtle, -52.0, 125.0, 5, "black", "blue")
            i += 1
        elif i == 1:
            """Draws the right eye!"""
            draw_hexagon(bob_the_turtle, 35.0, 120.0, 20, "black", "white")
            draw_circle(bob_the_turtle, 38.0, 125.0, 5, "black", "blue")
            i += 1
    """Draws the nose!"""
    draw_triangle(bob_the_turtle, -10.0, 95.0, 15, "black", "black")
    """Draws a content mouth!"""
    draw_line(bob_the_turtle, -55.0, 50.0, 110, "black")
    """Hides the turtle."""
    bob_the_turtle.hideturtle()
    done()


if __name__ == "__main__":
    main()