# -*- coding: UTF-8 -*-

import unittest

from eolas.lexer import lex
from eolas.parser import parse

class LexTest(unittest.TestCase):
    def test_identifiers(self):
        idents = ("a", "foo", "___x", "with spaces", "a b c d", "if true")
        for ident in idents:
            self.assertEqual(ident, next(lex(ident)).value)

    def test_reserved_identifiers(self):
        self.assertEqual("IF", next(lex("if")).type)
        self.assertEqual("RETURN", next(lex("return")).type)

    def test_ints(self):
        self.assertEqual(42, next(lex("42")).value)

class ParseTest(unittest.TestCase):
    def test_valid_programs(self):
        valid_programs = (
            "{ return 42 }",
            "{ return 42; }",
            "{ a = 42 }",
            "{ a = b = c = d = e }",
            "{ IF (a = a) THEN (Result = 1) ELSE (Result = 2) ; }"
        )

        for prg in valid_programs:
            try:
                parse(prg)
            except SyntaxError as e:
                self.assertIsNone(e)

if __name__ == "__main__":
    unittest.main()
