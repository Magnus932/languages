
import sys
import token
import tokenizer

#obj = tokenizer.Tokenizer(open("token.py", "rt").read())
obj = tokenizer.Tokenizer(sys.argv[1])

while 1:
	tok = obj.next_token()
	print(tok)
	if (tok.type == token.Token.TOKEN_EOF): break 