# -*- coding: UTF-8 -*-

import ply.yacc

from eolas.lexer import tokens, lex
from eolas.instructions import Test, ValueOf, Literal
from eolas.instructions import Return, Assignment, IfThenElse

if False:
    tokens

precedence = (
    ("right", "EQUAL"),
)

start = "program"

def p_expression_int(p):
    """expression : INT"""
    p[0] = Literal(p[1])

def p_expression_expression_eq_expression(p):
    """expression : expression EQUAL expression"""
    p[0] = Test("=", p[1], p[3])

def p_expression_identifier(p):
    """expression : IDENTIFIER"""
    p[0] = ValueOf(p[1])

def p_instruction_assignment(p):
    """instruction : IDENTIFIER EQUAL expression"""
    p[0] = Assignment(p[1], p[3])


def p_instruction_if_then_else(p):
    """instruction : IF LBRACE expression RBRACE THEN LBRACE instruction RBRACE ELSE LBRACE instruction RBRACE"""
    p[0] = IfThenElse(p[3], p[7], p[11])

def p_instruction_return_expression(p):
    """instruction : RETURN expression"""
    p[0] = Return(p[2])

def p_instructions_instructions_instruction(p):
    """instructions : instructions instruction"""
    p[0] = p[1] + [p[2]]

def p_instructions_instruction(p):
    """instructions : instruction"""
    p[0] = [p[1]]

def p_program_instructions(p):
    """program : LBRACKET instructions RBRACKET"""
    p[0] = p[2]

def p_error(p):
    if p is None:
        raise SyntaxError("EOF")
    raise SyntaxError(p)

def parse(text):
    parser = ply.yacc.yacc()
    return parser.parse(text, lexer=lex())
