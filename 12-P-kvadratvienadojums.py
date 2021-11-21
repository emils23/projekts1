import math

def kva():
    """
    funkcija aprēķina kvadrātvienādojuma
    a*x**2+b*x+c=0

    diskriminantu un, ja iespējams, saknes
    """
    a = float(input("Ievadi kvadrātvienādojuma koeficientu a"))
    b = float(input("Ievadi kvadrātvienādojuma koeficientu b"))
    c = float(input("Ievadi kvadrātvienādojuma koeficientu c"))
    d = b**2 - 4*a*c

    if d>0:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        print(f"Kvadrātvienādojuma diskriminants ir {d}, saknes \nx1 = {x1}\nx2={x2}")

    elif d == 0:
        x = -b/(2*a)
        print(f"Kvadrātvienādojuma diskriminants ir 0, sakne x = {x}")

    else:
        print(f"Kvadrātvienādojuma diskriminants ir {d}, sakņu nav.")
