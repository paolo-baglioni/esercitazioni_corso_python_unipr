# CERCHI CONCENTRICI CASUALI - EXERCISE 1.5

import g2d
import random

radious = []
red = []
green = []
blue = []

r = 200
radious.append(r)
red.append(random.randint(0,255))
green.append(random.randint(0,255))
blue.append(random.randint(0,255))

while(True):
    decrement = random.randint(0,r-1)
    new_r = r - decrement
    if(new_r < 10):
        break
    else:
        r = new_r
        radious.append(r)
        red.append(random.randint(0,255))
        green.append(random.randint(0,255))
        blue.append(random.randint(0,255))
        
print("Raggi estratti : ", radious)
        
x_total = y_total = 500
center = x_total/2

g2d.init_canvas((x_total, y_total))  # width, height

for i in range(len(radious)):
    g2d.set_color((red[i],green[i],blue[i]))
    g2d.fill_circle((center, center), radious[i])
    
g2d.main_loop()