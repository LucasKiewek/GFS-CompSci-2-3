import turtle

window = turtle.Screen()

leo = turtle.Turtle()

leo.speed(0)

# left eyebrow
leo.penup()
leo.setposition(-75, 70)
leo.pendown()
leo.left(90)
for i in range(20):
    leo.forward(10)
    leo.right(161)
    leo.forward(10)
    leo.left(160)

leo.right(140)
leo.forward(10)
leo.right(20)
leo.forward(35)
leo.right(18)
leo.forward(20)
leo.left(90)

# nose
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
for i in range(20):
    leo.forward(10)
    leo.right(161)
    leo.forward(10)
    leo.left(160)

# right cheek
leo.forward(5)
leo.right(80)
leo.forward(15)
leo.right(75)
leo.forward(35)
leo.right(5)
leo.forward(35)

# right beard
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
leo.right(170)
leo.forward(35)
leo.right(5)
leo.forward(35)

# hair
leo.left(85)
hl = 1
for i in range(30):
    leo.forward(hl)
    leo.right(170)
    leo.forward(hl)
    leo.left(170)
    if i % 3 == 0:
        hl += 1

for i in range(185):
    leo.forward(10)
    leo.right(170.94)
    leo.forward(10)
    leo.left(170)

for i in range(30):
    leo.forward(hl)
    leo.right(170)
    leo.forward(hl)
    leo.left(170)
    if i % 3 == 0:
        hl -= 1

# done
leo.right(100)
leo.forward(12)

window.exitonclick()
