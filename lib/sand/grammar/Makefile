GRAMMAR=Cave.g4

all: code
code: $(GRAMMAR)
	antlr4 $(GRAMMAR) -Dlanguage=Python3 -visitor

clean:
	rm -f CaveLexer.py
	rm -f Cave.interp
	rm -f CaveLexer.interp
	rm -f CaveLexer.tokens
	rm -f CaveParser.py
	rm -f CaveListener.py
	rm -f Cave.tokens
	rm -f CaveVisitor.py