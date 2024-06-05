# from turtle import Turtle, Screen
#
# maya = Turtle()
#
# maya.shape("turtle")
# maya.color("coral")
#
# while True:
#     maya.circle(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Makichu", "NimsekiChu"])
table.add_column("Pokemon", ["Pikachu", "Makichu", "NimsekiChu"])
table.align = "l"
print(table)