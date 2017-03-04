# -*- coding: UTF-8 -*-

class EndOfProgram(Exception):
    def __init__(self, code):
        self.code = code

class Value:
    def eval(self, memory):
        pass

class Test(Value):
    _tests = {
        "=": lambda e1, e2: e1 == e2,
    }

    def __init__(self, test, e1, e2):
        self.test = test
        self.e1 = e1
        self.e2 = e2

    def eval(self, memory):
        v1 = self.e1.eval(memory)
        v2 = self.e2.eval(memory)

        fn = self._tests.get(self.test)
        if fn:
            return fn(v1, v2)

class ValueOf(Value):
    def __init__(self, name):
        self.memory = {}
        self.name = name

    def eval(self, memory):
        return memory.get(self.name, self.name)


class Literal(Value):
    def __init__(self, value):
        self.value = value

    def eval(self, memory):
        return self.value


class Instruction:
    @property
    def kind(self):
        return self.__class__.__name__.lower()

    def run(self, memory):
        pass


class Return(Instruction):
    def __init__(self, value):
        self.value = value

    def run(self, memory):
        raise EndOfProgram(self.value.eval(memory))


class Assignment(Instruction):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def run(self, memory):
        memory[self.name] = self.value.eval(memory)


class IfThenElse(Instruction):
    def __init__(self, condition, i1, i2):
        self.condition = condition
        self.i1 = i1
        self.i2 = i2

    def run(self, memory):
        if self.condition.eval(memory):
            self.i1.run(memory)
        else:
            self.i2.run(memory)
