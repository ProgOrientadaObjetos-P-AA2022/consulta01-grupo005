class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isuma(self, other):

        self.x += other.x
        self.y += other.y

    def suma(self, other):
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    v1 = Vector(2.3, 6.9)
    v2 = Vector(1.0, -1.0)
    v1.isuma(v2)
    print(f"(x = {v1.x}, y = {v1.y})")

    v1 = Vector(2.3, 6.9)
    v2 = Vector(1.0, -1.0)
    v3 = v1.suma(v2)
    print(f"(x = {v3.x}, y = {v3.y})")