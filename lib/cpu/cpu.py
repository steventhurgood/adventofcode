from dataclasses import dataclass, field

import antlr4

from lib.cpu.grammar.CPULexer import CPULexer
from lib.cpu.grammar.CPUParser import CPUParser
from lib.cpu.grammar.CPUVisitor import CPUVisitor

from typing import Sequence, List


@dataclass
class CPU(CPUVisitor):

    # register_cycles[i] is the value of register x after i cycles
    register_cycles: List[int] = field(default_factory=list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_cycles = [1]

    def register_after(self, cycle: int = -1) -> int:
        """register_after gives the value of register X after cycle cycles

        Args:
            cycle (int, optional): The number of cycles after which to calculate the value of x. Defaults to -1 (the last cycle).

        Returns:
            int: the value of register x
        """
        return self.register_cycles[cycle]

    def visitNoop(self, ctx):
        # the value of the register stays the same for this cycle
        self.register_cycles.append(self.register_cycles[-1])

    def visitCount(self, ctx) -> int:
        return int(ctx.getText())

    def visitAddx(self, ctx):
        count = self.visitCount(ctx.count())
        # the value of the register stays the same for this cycle
        self.register_cycles.append(self.register_cycles[-1])
        self.register_cycles.append(self.register_cycles[-1] + count)

    def execute(self, input_filename: str):
        data = antlr4.FileStream(input_filename)
        lexer = CPULexer(data)
        stream = antlr4.CommonTokenStream(lexer)
        parser = CPUParser(stream)
        self.visit(parser.commands())

    def render(self) -> str:
        rows: List[str] = []

        for y in range(6):
            row: List[str] = []
            for x in range(40):
                cycle_during = (y*40) + x  # cycle during - 1
                sprite_middle = self.register_after(cycle_during)
                if x >= sprite_middle - 1 and x <= sprite_middle + 1:
                    row.append('#')
                else:
                    row.append('.')
            rows.append(''.join(row))

        return '\n'.join(rows)

    def strengths(self, cycles: Sequence[int]) -> Sequence[int]:
        """strengths returns the strengths at certain cyles.

        The strength at cycle n is is the cycle number multiplied by the
        value of register X during that cycle.

        Args:
            cycles (Sequence[int]): the cycles at which to calculate the strength.

        Returns:
            Sequence[int]: the strengths during each requested cycle
        """
        s = []
        for cycle in cycles:
            x = self.register_after(cycle-1)
            s.append(x * cycle)
        return s
