
from dataclasses import dataclass
from typing import List

import antlr4

from lib.monkey.grammar.MonkeyLexer import MonkeyLexer
from lib.monkey.grammar.MonkeyParser import MonkeyParser
from lib.monkey.grammar.MonkeyVisitor import MonkeyVisitor

from typing import Callable, Sequence

from absl import logging


@dataclass
class Monkey:
    items: List[int]
    operation: Callable[[int], int]
    divisor: int
    if_true: int
    if_false: int

    inspection_count: int = 0


class MonkeyBuilder(MonkeyVisitor):
    monkeys: List[Monkey]

    def __init__(self, input_filename):
        super().__init__()
        data = antlr4.FileStream(input_filename)
        lexer = MonkeyLexer(data)
        stream = antlr4.CommonTokenStream(lexer)
        self.parser = MonkeyParser(stream)
        self.monkeys = []

    def build(self) -> List[Monkey]:
        self.visit(self.parser.monkeys())
        return self.monkeys

    def visitMonkey(self, ctx):

        items = self.visit(ctx.items())
        operation = self.visit(ctx.operation())
        divisor = self.visit(ctx.test())
        iftrue = self.visit(ctx.iftrue())
        iffalse = self.visit(ctx.iffalse())

        monkey = Monkey(
            items=items,
            operation=operation,
            divisor=divisor,
            if_true=iftrue,
            if_false=iffalse,
        )

        self.monkeys.append(monkey)

    def visitTest(self, ctx) -> int:
        return self.visit(ctx.number())

    def visitIftrue(self, ctx) -> int:
        return self.visit(ctx.number())

    def visitIffalse(self, ctx) -> int:
        return self.visit(ctx.number())

    def visitOperation(self, ctx) -> Callable[[int], int]:
        return self.visit(ctx.expr())

    def visitExpr(self, ctx) -> Callable[[int], int]:
        return self.visit(ctx.children[0])

    def visitMul_old_expr(self, ctx) -> Callable[[int], int]:
        return lambda x: x*x

    def visitMul_num_expr(self, ctx) -> Callable[[int], int]:
        number: int = self.visit(ctx.number())
        return lambda x: x*number

    def visitSum_old_expr(self, ctx) -> Callable[[int], int]:
        return lambda x: x+x

    def visitSum_num_expr(self, ctx) -> Callable[[int], int]:
        number: int = self.visit(ctx.number())
        return lambda x: x + number

    def visitItems(self, ctx) -> List[int]:
        il = ctx.itemlist()
        return self.visit(il)

    def visitItemlist(self, ctx) -> List[int]:
        items = []
        list_contents = ctx.getText()
        for child in ctx.children:
            item = self.visit(child)
            items.append(item)
        return items

    def visitIdentifier(self, ctx):
        return self.visit(ctx.number())

    def visitNumber(self, ctx) -> int:
        return int(ctx.getText())


class Monkeys:
    parser: MonkeyParser
    monkeys: List[Monkey]

    worrier: bool
    rounds: int = 0
    max_divisor: int = 1

    def __init__(self, input_filename, worrier: bool = False):
        """create a new Monkeys simulation

        Args:
            input_filename (string): the filename containing the monkey spec
            worrier (bool, optional): if False, worry will decrease by a third each time.
        """

        monkeys = MonkeyBuilder(input_filename).build()
        self.monkeys = monkeys
        self.worrier = worrier

        for monkey in monkeys:
            self.max_divisor *= monkey.divisor

    def round(self, n: int = 1):
        for i in range(n):
            for monkey in self.monkeys:
                for item in monkey.items:
                    monkey.inspection_count += 1
                    new = monkey.operation(item) % self.max_divisor
                    if not self.worrier:
                        new = new // 3
                    if new % monkey.divisor == 0:
                        self.monkeys[monkey.if_true].items.append(new)
                    else:
                        self.monkeys[monkey.if_false].items.append(new)
                monkey.items = []
            self.rounds += 1
            logging.info(
                f'After {self.rounds} ({i}): {self.inspection_counts()}')

    def inspection_counts(self) -> Sequence[int]:
        return [monkey.inspection_count for monkey in self.monkeys]

    def monkey_business(self) -> int:
        inspection_counts = sorted(
            self.inspection_counts(), reverse=True)
        return inspection_counts[0] * inspection_counts[1]
