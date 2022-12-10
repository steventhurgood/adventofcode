grammar CPU;

commands: command+ EOF;
command: (noop | addx) NL?;
noop: 'noop';
addx: 'addx' WS count;
count: INT;
INT: '-'? [0-9]+;
NL: '\n';
WS: ' ';
