# some behavior that i want ot implement -> write some _function_
# top-level function or top-level syntax -> corresponding _function
# x + y ->  _add_
# init x -> _init_ etc etc
# repr(x) ->  _repr_
# x()  -> _call_


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r}.)'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass


p1 = Polynomial(1, 2, 3) #x**2 + 2x + 3
p2 = Polynomial(3, 4, 3) #3x**2 + 4x + 3




