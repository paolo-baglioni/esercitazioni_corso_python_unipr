# CERCHI CONCENTRICI GRADUALI - EXERCISE 1.4

import g2d

N_circle = int(input("Digita il numero di cerchi che vuoi disegnare "))
R_step = float(input("Digita lo step che vuoi applicare sul raggio "))
C_step = float(input("Digita lo step che vuoi applicare sulle tonalità di rosso "))

R_0 = 3*R_step

x_total = y_total = (R_0 + R_step * (N_circle + 1)) * 2

center = x_total/2

g2d.init_canvas((x_total, y_total))  # width, height

for i in range(N_circle):
    index_inverted = N_circle - i - 1
    R = R_0 + index_inverted*R_step
    red = 0 + index_inverted*C_step
    g2d.set_color((red,0,0))
    g2d.fill_circle((center, center), R)

g2d.main_loop()  # manage the window/canvas2