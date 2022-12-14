grammar Cave;
cave: rock+ EOF?;
rock: pair ('->' pair)* NL;
pair: x ',' y;
x: number;
y: number;
number: INT;

NL: '\n';
INT: '-'? [0-9]+;
WS: ' ' -> skip;