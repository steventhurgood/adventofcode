grammar Compare;
pairs: pair+;
pair: left right;
left: list_or_int;
right: list_or_int;
list_or_int: number | '[' list? ']';
number: INT;
list: list_or_int (COMMA list_or_int)*;
COMMA: ','+;

INT: [0-9]+;

WS: [\n] -> skip;
END: EOF -> skip;