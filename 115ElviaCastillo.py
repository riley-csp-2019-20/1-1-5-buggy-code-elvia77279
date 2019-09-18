#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 4
length = 70
angle = 200 / legs
spider.pensize(5)
count = 0
while (count < legs):
  spider.goto(0,20)
  spider.setheading(angle*count - 50)
  spider.forward(length)
  spider.goto(0,20)
  spider.setheading(angle*count + 50)
  spider.forward(length)
  count = count + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()

# x = drawer
#body of spider
# y = length
# z = angle
# w = limit of number of legs and distance between legs
# n = count