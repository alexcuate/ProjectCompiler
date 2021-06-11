# Created By José Alejandro Vázquez Sánchez
# Compiler Final Project
import ply.lex as lex
import os


# Regex Rules
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_TIMES = r'\*'
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_SEMICOLON = ';'
t_COMMA = r','
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_QUOTES = r'\"'
t_PLUS = r'\+'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_MINUS = r'-'
t_MINUSMINUS = r'\-\-'


# Reserved Keywords
tokens = (
    'ENDL',
    'ELSE',
    'STRING',
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'COUT',
    'CIN',
    'RETURN',
    'VOID',
    'WHILE',
    'IF',
    'INT',
    'FOR',

    # Symbols
    'TIMES',
    'EQUAL',
    'HASH',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'PLUS',
    'PLUSPLUS',
    'NUMBER',
    'MINUS',
    'MINUSMINUS',
    'DEQUAL',
    'DISTINT',
    'SEMICOLON',
    'COMMA',
    'RBRACKET',
    'LESS_THAN',
    'LESS_OR_EQUAL',
    'GREATER_THAN',
    'GREATEREQUAL',
    'L_SHIFT',
    'R_SHIFT',
    'LBLOCK',
    'RBLOCK',
    'QUOTES',
    'ID'
)

def t_INCLUDE(t):
    r"""include"""
    return t


def t_USING(t):
    r"""using"""
    return t


def t_NAMESPACE(t):
    r"""namespace"""
    return t


def t_STD(t):
    r"""std"""
    return t


def t_COUT(t):
    r"""cout"""
    return t


def t_CIN(t):
    r"""cin"""
    return t


def t_ENDL(t):
    r"""endl"""
    return t


def t_ELSE(t):
    r"""else"""
    return t


def t_IF(t):
    r"""if"""
    return t


def t_INT(t):
    r"""int"""
    return t


def t_RETURN(t):
    r"""return"""
    return t


def t_VOID(t):
    r"""void"""
    return t


def t_WHILE(t):
    r"""while"""
    return t


def t_ID(t):
    r"""\w+(_\d\w)*"""
    return t


def t_STRING(t):
    r"""\"?(\w+ \ *\w*\d* \ *)\"?"""
    return t


def t_HASH(t):
    r"""\#"""
    return t


def t_PLUSPLUS(t):
    r"""\+\+"""
    return t


def t_LESS_OR_EQUAL(t):
    r"""<="""
    return t


def t_GREATEREQUAL(t):
    r""">="""
    return t


def t_DEQUAL(t):
    r"""=="""
    return t


def t_FOR(t):
    r"""for"""
    return t


def t_NUMBER(t):
    r"""\d+"""
    t.value = int(t.value)
    return t


def t_L_SHIFT(t):
    r"""<<"""
    return t


def t_R_SHIFT(t):
    r""">>"""
    return t


def t_DISTINT(t):
    r"""!="""
    return t


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_comments(t):
    r"""/\*(.|\n)*?\*/"""
    t.lexer.lineno += t.value.count('\n')


def t_comments_C99(t):
    r"""//(.)*?\n"""
    t.lexer.lineno += 1


def t_error(t):
    print(("Lexical Error: " + str(t.value[0])))
    t.lexer.skip(1)


lexer_analyzer = lex.lex()

