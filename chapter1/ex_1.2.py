from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # if not implemented, interpreter will show you an Object name with its address
    def __repr__(self):
        return 'Vector({!r}, {!r})'.format(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # in if or while statements, python should assert if the given var is true or false.
    # python use bool(x), which in turn will return x.__bool()__
    # By default, python assumes any object as true, without __bool__ magic method.
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    vector = Vector()
    if vector:
        print('should not reach')

    vectors = [Vector(1, 3), Vector(2, 5)]
    print(vectors[0] + vectors[1])
    print(vectors[0] * 3)
    # Type error, should use rmul()
    # print(3 * vectors[0])