# 3. Shape Hierarchy with an Abstract Method
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError(
            "Child classes must override area()"
        )

    def perimeter(self):
        raise NotImplementedError(
            "Child classes must override perimeter()"
        )

    def describe(self):
        print(
            f"{self.name}: "
            f"area={self.area()}, "
            f"perimeter={self.perimeter()}"
        )


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return (
            s
            * (s - self.a)
            * (s - self.b)
            * (s - self.c)
        ) ** 0.5

try:
    shape = Shape("Generic Shape")
    shape.describe()
except NotImplementedError as e:
    print("Shape itself cannot calculate area/perimeter:")
    print(e)

print()
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]
for shape in shapes:
    shape.describe()