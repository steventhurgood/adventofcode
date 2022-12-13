GRAMMAR=Compare.g4

all: code
code: $(GRAMMAR)
	antlr4 $(GRAMMAR) -Dlanguage=Python3 -visitor

clean:
	rm -f CompareLexer.py
	rm -f Compare.interp
	rm -f CompareLexer.interp
	rm -f CompareLexer.tokens
	rm -f CompareParser.py
	rm -f CompareListener.py
	rm -f Compare.tokens
	rm -f CompareVisitor.py