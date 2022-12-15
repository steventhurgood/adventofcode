from __future__ import annotations

from dataclasses import dataclass
from functools import total_ordering
from typing import Any, List, Tuple

import antlr4
import heapq

from lib.compare.grammar.CompareLexer import CompareLexer
from lib.compare.grammar.CompareParser import CompareParser
from lib.compare.grammar.CompareVisitor import CompareVisitor

import logging
logging.basicConfig()

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


class ComparablePairCompiler(CompareVisitor):
    pairs: List[Tuple[Comparable, Comparable]]
    comparables: List[Comparable]
    key_a_index: int = -1
    key_b_index: int = -1
    decoder_key: int = -1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pairs = []
        self.comparables = []

    def flatten_pairs(self) -> List[Comparable]:
        out = []
        for left, right in self.pairs:
            out.append(left)
            out.append(right)
        return out

    def find_decoder_key(self, divider_a=None, divider_b=None) -> int:
        if divider_a is None:
            divider_a = [[2]]
        if divider_b is None:
            divider_b = [[6]]

        divider_a_cmp = Comparable.build_comparable(divider_a)
        divider_b_cmp = Comparable.build_comparable(divider_b)

        comparables = self.flatten_pairs()
        heapq.heapify(comparables)

        heapq.heappush(comparables, divider_a_cmp)
        heapq.heappush(comparables, divider_b_cmp)

        self.comparables = [heapq.heappop(comparables)
                            for i in range(len(comparables))]

        divider_a_index = self.comparables.index(divider_a_cmp) + 1
        divider_b_index = self.comparables.index(divider_b_cmp) + 1

        self.key_a_index = divider_a_index
        self.key_b_index = divider_b_index
        self.decoder_key = divider_a_index * divider_b_index

        return self.decoder_key

    def visitPairs(self, ctx: CompareParser.PairsContext):
        logger.info('Visiting Pairs: %s', ctx.getText())
        if ctx.children is not None:
            for child in ctx.children:
                pair = self.visit(child)
                self.pairs.append(pair)

    def visitPair(self, ctx) -> Tuple[Comparable, Comparable]:
        logger.info('Visiting pair: %s', ctx.getText())
        left = self.visit(ctx.left())
        right = self.visit(ctx.right())
        return (left, right)

    def visitLeft(self, ctx) -> Comparable:
        logger.info('Left: %s', ctx.getText())
        return self.visit(ctx.list_or_int())

    def visitRight(self, ctx) -> Comparable:
        logger.info('Right: %s', ctx.getText())
        return self.visit(ctx.list_or_int())

    def visitList_or_int(self, ctx: CompareParser.List_or_intContext):
        number = ctx.number()
        if number is not None:
            return ComparableNumber(self.visit(number))

        items = ctx.list_()
        if items is not None:
            return ComparableList(self.visit(items))

        return ComparableList([])

    def visitNumber(self, ctx) -> int:
        logger.info('Number: %s', ctx.getText())
        return int(ctx.getText())

    def visitList(self, ctx) -> List[Comparable]:
        logger.info('List: %s', ctx.getText())
        out = []
        if ctx.children is None:
            raise Exception(f'List had no children: {ctx.getText()}')
        for i in range(0, len(ctx.children), 2):
            item = self.visit(ctx.children[i])
            out.append(item)
        return out


@total_ordering
@dataclass
class Comparable:
    """Comparable represents a recursively comparable tree of numbers.
    """
    @classmethod
    def compile_comparable_pairs(cls,
                                 input_filename: str) -> Tuple[
            List[Tuple[Comparable, Comparable]],
            ComparablePairCompiler]:
        """Create a list of pairs of comparables, from a file"""

        data = antlr4.FileStream(input_filename)
        lexer = CompareLexer(data)
        stream = antlr4.CommonTokenStream(lexer)
        parser = CompareParser(stream)

        compiler = ComparablePairCompiler()
        compiler.visit(parser.pairs())
        return compiler.pairs, compiler

    @classmethod
    def build_comparable(cls, number_or_list: List[Any]) -> Comparable:
        """build_comparable creates a Comparable from nested lists.

        Args:
            number_or_list (List[Any]): A list of numbers and lists.

        Returns:
            Comparable: an object that can be used to compare the ordering of
                two Comparable objects
        """
        if isinstance(number_or_list, int):
            return ComparableNumber(number=number_or_list)

        if isinstance(number_or_list, list):
            items = []
            for item in number_or_list:
                items.append(cls.build_comparable(item))
            return ComparableList(items=items)

    def __lt__(self, other: Comparable) -> bool:
        if isinstance(self, ComparableNumber):
            if isinstance(other, ComparableNumber):
                # we need nested IFs to make Pylance happy
                return self.number < other.number

            if isinstance(other, ComparableList):
                new_left = ComparableList([self])
                return new_left < other

            raise Exception(
                f'Incompatible types: {self}({type(self)}) '
                'and {other}({type(other)})')

        if isinstance(self, ComparableList):
            if isinstance(other, ComparableList):
                for i, left in enumerate(self.items):
                    if i >= len(other.items):
                        # we ran out of items on the right hand side
                        return False

                    right = other.items[i]
                    if left < right:
                        return True
                    if left != right:
                        return False
                # we have reached the end of the right hand list.
                return len(self.items) < len(other.items)

            if isinstance(other, ComparableNumber):
                new_right = ComparableList([other])
                return self < new_right

            raise Exception(
                f'Incompatible types: {self}({type(self)})'
                ' and {other}({type(other)})')

        raise Exception(
            f'Incompatible types: {self}({type(self)})'
            ' and {other}({type(other)})')


@ dataclass
class ComparableNumber(Comparable):
    """ComparableNumber represents a number in the comparable tree"""
    number: int

    def __str__(self) -> str:

        return str(self.number)


@ dataclass
class ComparableList(Comparable):
    """ComparableList represents a list in the recursively comparable tree"""
    items: List[Comparable]

    def __str__(self) -> str:
        out: List[str] = []
        for item in self.items:
            out.append(str(item))
        return '[' + ','.join(out) + ']'
