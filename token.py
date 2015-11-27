
class Token:

	TOKEN_ID	= 0
	TOKEN_INT	= 1
	TOKEN_EQL	= 2
	TOKEN_PLU	= 3
	TOKEN_MIN	= 4
	TOKEN_MUL	= 5
	TOKEN_DIV	= 6
	TOKEN_IF	= 7
	TOKEN_FOR	= 8
	TOKEN_WHIL	= 9
	TOKEN_EOF	= 10

	token_names = ["ID", "INT", "EQUAL", "PLUS", "MINUS",
	               "MULTIPLY", "DIVIDE", "IF", "FOR", "WHILE",
	               "EOF"]

	def __init__(self, typ, text):
		self.type = typ
		self.text = text

	def __str__(self):
		return "('%s', '%s')" % (self.text, Token.token_names[self.type])