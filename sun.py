from turtle import *

color("blue", "green")
begin_fill()
while True:
    forward(250)
    left(200)
    if abs(pos()) < 1:
        break
end_fill()
done()
