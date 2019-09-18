#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 8
length = 70
angle = 200 / legs
spider.pensize(5)
count = 0
while (count < legs):
  spider.goto(0,20)
  if count < 4:
    spider.setheading(angle*count + 0)
    spider.forward(length)
  else:
    spider.setheading(angle*count + 90)
    spider.forward(length)
  
  count = count + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()

# x = drawer
#body of spider
# y = length
# z = angle
# w = legs or limit of number of legs and distance between legs
# n = count