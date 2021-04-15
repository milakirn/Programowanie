import math
class Figure:
    def __init__(self, side_A):
        self.side_A = side_A

class Square(Figure):
    def __init__(self, side_A):
        super().__init__(side_A)

    def Area(self):
        area = self.side_A**2
        print(f"Area of this square is {area}")
    def Perimeter(self):
        p = 4 * self.side_A
        print(f"Perimeter of the square is {p}")

class Rectangle(Figure):
    def __init__(self, side_A, side_B):
        super().__init__(side_A)
        self.side_B = side_B

    def Area(self):
        area = self.side_A * self.side_B
        print(f"Area of this rectangle is {area}")
    def Perimeter(self):
        p = 2 * (self.side_A + self.side_B)
        print(f"Perimeter of the rectangle is {p}")

class Triangle(Figure):
    def __init__(self, side_A, side_B, side_C, height):
        super().__init__(side_A)
        self.side_B = side_B
        self.side_C = side_C
        self.height = height

    def Area(self):
        if (self.side_A == self.side_B == self.side_C):
            area = round((math.sqrt(3) / 4) * self.side_A ** 2, 2)
            print(f"Area of this triangle is {area}")
        else:
            area = (self.side_A * self.height) / 2
            print(f"Area of this triangle is {area}")

    def Perimeter(self):
        if (self.side_A == self.side_B == self.side_C):
            p = 3 * self.side_A
            print(f"Perimeter of this triangle is {p}")
        else:
            p = self.side_A + self.side_B + self.side_C
            print(f"Perimeter of the triangle is {p}")

class Circle():
    def __init__(self, raduis):
        self.radius = raduis

    def Diametr(self):
        return (self.radius * 2)

    def Area(self):
        area = round((math.pi * self.radius ** 2), 2)
        print(f"Area of this circle is {area}")

    def Circumference(self):
        c = round((2 * self.radius * math.pi), 2)
        print(f"Circumference of the circle is {c}")

class Diamond(Figure):
    def __init__(self, side_A, height):
        super().__init__(side_A)
        self.height = height

    def Area(self):
        area = self.side_A * self.height
        print(f"Area of this diamond is {area}")

    def Perimeter(self):
        p = 4 * self.side_A
        print(f"Perimeter of the diamond is {p}")

class Trapeze(Figure):
    def __init__(self, side_A, side_B, side_C, side_D, height):
        super().__init__(side_A)
        self.side_B = side_B
        self.side_C = side_C
        self.side_D = side_D
        self.height = height

    def Area(self):
        area = ((self.side_A + self.side_B) * self.height) / 2
        print(f"Area of the trapeze is {area}")

    def Perimeter(self):
        p = self.side_A + self.side_B + self.side_C + self.side_D
        print(f"Perimeter of this trapeze is {p}")


wybor = input("Choose one of figures: square, rectangle, triangle, circle, diamond, trapeze --> ").capitalize()
if wybor == "Square":
    side = int(input("Write side: "))
    square1 = Square(side)
    square1.Area()
    square1.Perimeter()
elif wybor == "Rectangle":
    sideA = int(input("Write side A: "))
    sideB = int(input("Write side B: "))
    rectangle1 = Rectangle(sideA, sideB)
    rectangle1.Area()
    rectangle1.Perimeter()
elif wybor == "Triangle":
    sideA = int(input("Write side A: "))
    sideB = int(input("Write side B: "))
    sideC = int(input("Write side C: "))
    height = int(input("Write height: "))
    triangle1 = Triangle(sideA, sideB, sideC, height)
    triangle1.Area()
    triangle1.Perimeter()
elif wybor == "Circle":
    radius = int(input("Write Raduis: "))
    circle1 = Circle(radius)
    circle1.Diametr()
    circle1.Area()
    circle1.Circumference()
elif wybor == "Diamond":
    sideA = int(input("Write side A: "))
    height = int(input("Write height: "))
    diamond1 = Diamond(sideA, height)
    diamond1.Area()
    diamond1.Perimeter()
elif wybor == "Trapeze":
    sideA = int(input("Write side A: "))
    sideB = int(input("Write side B: "))
    sideC = int(input("Write side C: "))
    sideD = int(input("Write side D: "))
    height = int(input("Write height: "))
    trapeze1 = Trapeze(sideA, sideB, sideC, sideD, height)
    trapeze1.Area()
    trapeze1.Perimeter()