
import os
import sys
from token import Token

'''
	Easy, simple LL(1) lexer :/.
'''

class Tokenizer:

	def __init__(self, arg):
		self.buf = arg
		self.p = 0
		self.c = self.buf[self.p]

	def consume(self):
		self.p += 1
		if (self.p >= len(self.buf)):
			self.c = -1
		else:
			self.c = self.buf[self.p]

	def is_letter(self):
		if (self.c == -1): return False
		return (self.c >= 'a' and self.c <= 'z' or
			    self.c >= 'A' and self.c <= 'Z')

	def ID(self):
		buf = str()
		while (self.is_letter()):
			buf += self.c
			self.consume()
		if (buf == "if"):
			return Token(Token.TOKEN_IF, buf)
		if (buf == "for"):
			return Token(Token.TOKEN_FOR, buf)
		if (buf == "while"):
			return Token(Token.TOKEN_WHILE, buf)

		return Token(Token.TOKEN_ID, buf)

	def is_digit(self):
		if (self.c == -1): return False
		return (self.c >= '0' and self.c <= '9')

	def INT(self):
		buf = str()
		while (self.is_digit()):
			buf += self.c
			self.consume()
		return Token(Token.TOKEN_INT, buf)

	def whitespace(self):
		while (self.c == ' ' or self.c == '\t' or self.c == '\n'
			   or self.c == '\r'): self.consume()

	def comment(self):
		while (self.c != '\n' and self.c != -1):
			self.consume()

	def next_token(self):
		while (self.c != -1):
			if (self.c == ' ' or self.c == '\t' or self.c == '\n'
				or self.c == '\r'):
				self.whitespace()
				continue
			if (self.c == '#'):
				self.comment()
				continue
			elif (self.c == '='):
				self.consume()
				return Token(Token.TOKEN_EQL, '=')
			elif (self.c == '+'):
				self.consume()
				return Token(Token.TOKEN_PLU, '+')
			elif (self.c == '-'):
				self.consume()
				return Token(Token.TOKEN_MIN, '-')
			elif (self.c == '*'):
				self.consume()
				return Token(Token.TOKEN_MUL, '*')
			elif (self.c == '/'):
				self.consume()
				return Token(Token.TOKEN_DIV, '/')
			else:
				if (self.is_letter()):
					return self.ID()
				if (self.is_digit()):
					return self.INT()
				raise Exception("invalid character: %s" % self.c)
		return Token(Token.TOKEN_EOF, "EOF")
