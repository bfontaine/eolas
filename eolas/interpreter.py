# -*- coding: UTF-8 -*-

import sys
import argparse

from eolas.instructions import EndOfProgram
from eolas.parser import parse

class Program:
    def __init__(self, source, memory=None):
        self.memory = memory or {}
        self.instructions = parse(source)

    def eval(self):
        try:
            for inst in self.instructions:
                inst.run(self.memory)
        except EndOfProgram as e:
            return e.code

        return 0

    def get_result(self):
        return self.memory.get("Result")

    def dump_memory(self):
        for k, v in sorted(self.memory.items()):
            print("  %s = %s" % (k, v))


class main():
    p = argparse.ArgumentParser(description="Eolas interpreter")
    p.add_argument("--set", action="append", help="Set variables")
    p.add_argument("--eval", "-e", help="Evaluate a string")
    p.add_argument("source", nargs="?", metavar="SOURCE", default=sys.stdin,
                   type=argparse.FileType("r"))
    opts = p.parse_args()

    memory = {}
    if opts.set:
        for assign in opts.set:
            name, value = assign.split("=", 1)
            memory[name] = value

    if opts.eval:
        source = opts.eval
    else:
        source = opts.source.read()

    prg = Program(source, memory)
    ret = prg.eval()
    print(prg.get_result())
    sys.exit(ret)

if __name__ == "__main__":
    main()
