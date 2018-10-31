import turtle

window = turtle.Screen()

window.bgcolor("beige")

leo = turtle.Turtle()

leo.speed(0)
leo.fill(True)
# left eyebrow
leo.color("brown")
leo.penup()
leo.setposition(-75, 70)
leo.pendown()
leo.left(90)
for i in range(20):
    leo.forward(10)
    leo.right(161)
    leo.forward(10)
    leo.left(160)

# nose
leo.color("black")
leo.right(140)
leo.forward(10)
leo.right(20)
leo.forward(35)
leo.right(18)
leo.forward(20)
leo.left(90)
leo.forward(19)
leo.left(40)
leo.forward(20)
leo.left(90)
leo.forward(20)
leo.right(18)
leo.forward(35)
leo.right(30)
leo.forward(10)
leo.left(25)

# right eyebrow
leo.color("brown")
for i in range(20):
    leo.forward(10)
    leo.right(161)
    leo.forward(10)
    leo.left(160)

# right cheek
leo.color("black")
leo.forward(5)
leo.right(80)
leo.forward(15)
leo.right(75)
leo.forward(35)
leo.right(5)
leo.forward(35)

# right beard
leo.color("brown")
for i in range(18):
    leo.forward(35)
    leo.right(175)
    leo.forward(30)
    leo.left(172)

# mustash
leo.right(200)
leo.forward(13)
leo.left(35)

size = 32

for i in range(22):
    leo.forward(size)
    leo.left(175)
    leo.forward(size-1)
    leo.right(173)
    size -= 1

for i in range(22):
    leo.forward(size)
    leo.left(175)
    leo.forward(size+1)
    leo.right(173)
    size += 1

leo.right(150)
leo.forward(13)
leo.right(29)

# left beard
for i in range(18):
    leo.forward(30)
    leo.right(175)
    leo.forward(35)
    leo.left(172)

# left cheek
leo.color("black")
leo.right(170)
leo.forward(35)
leo.right(5)
leo.forward(35)

# hair
leo.color("brown")
leo.tracer(0, 0)

leo.left(85)
hl = 1
for i in range(30):
    leo.forward(hl)
    leo.right(170)
    leo.forward(hl)
    leo.left(170)
    if i % 3 == 0:
        hl += 1


turtle.update()

for i in range(185):
    leo.forward(10)
    leo.right(170.94)
    leo.forward(10)
    leo.left(170)
    turtle.update()

for i in range(30):
    leo.forward(hl)
    leo.right(170)
    leo.forward(hl)
    leo.left(170)
    if i % 3 == 0:
        hl -= 1


# done
leo.color("black")
leo.right(100)
leo.forward(12)


# leo.color("white")
# leo.left(99)
# leo.forward(90)
# leo.left(90)
# leo.forward(200)
# for i in range(3):
#     leo.left(90)
#     leo.forward(400)
# leo.left(90)
# leo.forward(200)
# leo.left(90)
# leo.forward(90)
# leo.fill(False)

turtle.update()

window.exitonclick()
