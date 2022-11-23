'''
8. Design a method called solveSecondOrderEquation that receives three integer
positive numbers corresponding to the coefficients of a second order equation
(ax2+bx+c=0) and computes its possible solutions. If the parameters are not valid the
method should return None.

Rafael García Benítez
'''

def ecuacionSegundoGrado (a,b,c):
    discriminante =  b * b - 4 * a * c
    ecu=0
    ecu2=0
    if discriminante < 0:
        ecu=None
        ecu2=None
    else:
        if discriminante != 0:
            ecu=((-b+(((b**2)-(4*a*c))**(1/2)))/(2*a))
            ecu2=((-b-(((b**2)-(4*a*c))**(1/2)))/(2*a))
        else:
            ecu=((-b+(((b**2)-(4*a*c))**(1/2)))/(2*a))
    return ecu,ecu2

print(ecuacionSegundoGrado(-2, 4, -2))