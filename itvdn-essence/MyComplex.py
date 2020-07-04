class MyComplex:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imaginary + other.imaginary)

    def __neg__(self):
        return MyComplex(-self.real, -self.imaginary)

    def __sub__(self, other):
        return self + (-other)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __repr__(self):
        return "Complex({!r}, {!r})".format(self.real, self.imaginary)

    def __str__(self):
        return "{} + {}i".format(self.real, self.imaginary)


c = MyComplex(5, 4)
print(c)
print(c.__repr__())
print(c + MyComplex(1,1))
print(c - MyComplex(1, 1))
d = MyComplex(5, 4)
print(c == d)
print(c is d)