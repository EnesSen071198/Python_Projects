import turtle
import time

# Ekranı oluştur
turtle_screen=turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Python Turtle")

t = turtle.Turtle()
t.color("Red")

# Kare çizme fonksiyonu
'''
for _ in range(4):
    t.left(90)  # 90 derece sola dön
    t.forward(100)  # 100 birim ileri git
'''

# Üçgen çizme fonksiyonu
'''
for _ in range(3):
    t.left(120)  # 90 derece sola dön
    t.forward(100)  # 100 birim ileri git
'''

# Yıldız çizme fonksiyonu
'''
for i in range(5):
    t.right(144)  # 90 derece sağa dön
    t.forward(300)  # 100 birim ileri git
'''

# Çokgen çizme fonksiyonu
'''
number_sides=6
angle=360/number_sides
side_length=300

for i in range(number_sides):
    t.right(angle)  # 90 derece sola dön
    t.forward(side_length)  # 100 birim ileri git
'''

# İç içe kare çizme fonksiyonu
'''
def squares(size):
    if size <= 0:  # Stop the recursion when the size is 0 or negative
        return
    for _ in range(4):
        t.left(90)  # 90 derece sola dön
        t.forward(size)  # 100 birim ileri git
        size-=5
    squares(size - 5)
squares(300)
'''

# Yuvarlak döngü çizme fonksiyonu
'''
turtle_colors=["red","green","blue","yellow","gray","orange","purple","white"]

for i in range(100):
    t.color(turtle_colors[i%6])
    t.circle(10*i)
    t.circle(-10*i)
    t.speed(0)
'''

'''
# İnteraktif çizme fonksiyonu

def turtle_forward():
    t.forward(100)

def rotate_angle_right():
    t.setheading(t.heading()-100)

def rotate_angle_left():
    t.setheading(t.heading()+100)

def clear_screen():
    t.clear()

def turtle_pen_up():
    t.penup()

def turtle_pen_down():
    t.pendown()

def turtle_return_home():
    t.home()

turtle_screen.listen()
turtle_screen.onkey(key="space",fun=turtle_forward)
turtle_screen.onkey(key="Down",fun=rotate_angle_right)
turtle_screen.onkey(key="Up",fun=rotate_angle_left)
turtle_screen.onkey(key="c",fun=clear_screen)
turtle_screen.onkey(key="q",fun=turtle_pen_up)
turtle_screen.onkey(key="w",fun=turtle_pen_down)
turtle_screen.onkey(key="h",fun=turtle_return_home)

turtle_screen.exitonclick()
 
'''

# Kalp çizme fonksiyonu
t.hideturtle()


def draw_heart(size):
    t.pensize(2)
    t.fillcolor("red")
    t.begin_fill()

    t.left(140)
    t.forward(size)

    for _ in range(200):
        t.right(1)
        t.forward(size * 0.01)

    t.left(120)

    for _ in range(200):
        t.right(1)
        t.forward(size * 0.01)

    t.forward(size)
    t.end_fill()

    # Reset position and angle for next heart
    t.setheading(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()


def growing_nested_hearts():
    base_size = 10
    while True:
        t.clear()

        # Her iterasyonda 5 iç içe kalp çiz
        for i in range(5):
            current_size = base_size * (i + 1)
            draw_heart(current_size)

        turtle_screen.update()
        base_size += 2  # Ana boyutu artır


try:
    t.penup()
    t.goto(0, 0)
    t.pendown()
    growing_nested_hearts()

except KeyboardInterrupt:
    print("\nProgram terminated by user")
    turtle_screen.bye()

turtle_screen.mainloop()
turtle.done()
