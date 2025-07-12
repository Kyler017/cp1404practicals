class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year, pointer_arithmetic=False):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"PointerArithmetic={self.pointer_arithmetic}, First appeared in {self.year}")


