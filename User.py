from Library import Base

assert hasattr(Base, 'foo'), "function is not in library!!" #check if this is implemented in library


class Derived(Base):
    def bar(self):
        return self.foo()

    #test git


