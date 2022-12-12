GRAMMAR=Monkey.g4

all: code
code: $(GRAMMAR)
	antlr4 $(GRAMMAR) -Dlanguage=Python3 -visitor

clean:
	rm -f MonkeyLexer.py
	rm -f Monkey.interp
	rm -f MonkeyLexer.interp
	rm -f MonkeyLexer.tokens
	rm -f MonkeyParser.py
	rm -f MonkeyListener.py
	rm -f Monkey.tokens
	rm -f MonkeyVisitor.py