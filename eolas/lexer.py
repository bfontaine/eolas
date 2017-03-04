#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import re
import ply.lex

# {
# IF (avocat = Maitre Eolas)
# THEN (Result = Win)
# ELSE
# (Result = lose)
# return 0;
# }

keywords = {
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
    "return": "RETURN",
}

tokens = [
    "LBRACKET",
    "RBRACKET",
    "LBRACE",
    "RBRACE",
    "EQUAL",
    "INT",
    "IDENTIFIER",
] + list(keywords.values())

t_LBRACKET = r"\{"
t_RBRACKET = r"\}"
t_LBRACE = r"\("
t_RBRACE = r"\)"
t_EQUAL = r"="
t_ignore = "; \t\r\n"

def t_error(t):
    raise SyntaxError(
        "Illegal character '%s' in ...%s..." % (t.value[0], t.value[0:100]))

def t_IDENTIFIER(t):
    r"[a-zA-Z_](?: [a-zA-Z]|\w)*"
    t.type = keywords.get(t.value.lower(), "IDENTIFIER")
    return t

def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t

def lex(text=None):
    lexer = ply.lex.lex(reflags=re.UNICODE)
    if text is not None:
        lexer.input(text)
    return lexer
