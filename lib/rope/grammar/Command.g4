grammar Command;
commands: command+ EOF;
command: direction WHITESPACE count NEWLINE?;
direction: 'U' | 'D' | 'L' | 'R';
count: INT;
INT: [0-9]+;
WHITESPACE: [ \t]+;
NEWLINE: [\r\n];