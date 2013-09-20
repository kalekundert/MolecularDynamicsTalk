#!/usr/bin/env python

from pylab import *
from os import fork

dist = linspace(0.01, 10, num=500)
vdw = pow(dist, -12) - 2 * pow(dist, -6)
elec = -1 / dist

title("Comparison of the Non-Bonded Energy Terms")
plot(dist, vdw, label="Van der Waals", color='#204a87')
plot(dist, elec, label="Electrostatic", color='#cc0000')

legend()
xlabel("Distance")
ylabel("Energy")
ylim(-1.2, 1.2)
grid()

if not fork():
    show()

