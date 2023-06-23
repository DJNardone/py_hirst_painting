from turtle import Turtle, Screen
import random

# colorgram packet extracts color palette from any image.
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('hirst-download.jpg', 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
# print(rgb_colors)

tommy = Turtle()
tommy.shape("classic")
tommy.speed("fast")
tommy.hideturtle()
Screen().colormode(255)

the_colors = [(229, 223, 226), (217, 227, 220), (195, 172, 121), (222, 227, 232), (157, 97, 59),
          (185, 159, 52), (9, 53, 77), (125, 37, 25), (55, 33, 27), (110, 69, 85), (118, 162, 175),
          (27, 118, 164), (74, 35, 43), (85, 138, 67), (10, 62, 44), (71, 153, 130), (121, 35, 40), (182, 98, 82),
          (207, 202, 146), (144, 176, 161), (178, 150, 156), (176, 202, 188), (217, 179, 172), (22, 77, 93)]
counter = 0
start_pos = 250


def random_colors():
    pick_color = random.choice(the_colors)
    return pick_color


is_drawing = True
while is_drawing:
    tommy.penup()
    tommy.setpos(-250, start_pos)

    def draw_row():
        for i in range(10):
            tommy.dot(20, random_colors())
            tommy.forward(50)

    counter += 1
    start_pos -= 50
    if counter == 10:
        is_drawing = False

    draw_row()

screen = Screen()
screen.exitonclick()
