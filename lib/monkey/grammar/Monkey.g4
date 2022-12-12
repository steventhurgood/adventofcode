grammar Monkey;
monkeys: (monkey NL?)+ EOF?;
monkey: identifier items operation test iftrue iffalse;

// Monkey: 0
identifier: 'Monkey ' number ':' NL;
number: INT;

// Starting items: 1, 2, 3
ITEMS_PREFIX: '  Starting items: ';
items: ITEMS_PREFIX itemlist NL;
itemlist: (number COMMA?)+;
COMMA: ', ' -> skip;

// Operation: new = old + 10
operation: '  Operation: new = old ' expr NL;
expr: mul_old_expr | mul_num_expr | sum_old_expr | sum_num_expr;
mul_old_expr: '* old';
mul_num_expr: '* ' number;
sum_old_expr: '+ old';
sum_num_expr: '+ ' number;

// Test: divisible by 5
test: '  Test: divisible by ' number NL;

// if true: 
iftrue: '    If true: throw to monkey ' number NL;
// if true: 
iffalse: '    If false: throw to monkey ' number NL;

INT: [0-9]+;
NL: '\n';
LINE: [^n]* '\n';