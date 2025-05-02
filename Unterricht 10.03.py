class Aoo:
    def __init__(self):
        self.ree = 87

    def bar(self):
        print(f"Wert von ree ist:: {self.ree}.")


class Boo(Aoo):
    def __init__(self):
        super().__init__()
        self.tee = 0

    def foo(self, objA: Aoo):
        objA.bar()


boo = Boo()
boo.foo(boo)