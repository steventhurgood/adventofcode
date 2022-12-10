import os
from typing import List

import antlr4
from absl import app, flags, logging

from lib.rope.grammar.CommandLexer import CommandLexer
from lib.rope.grammar.CommandParser import CommandParser
from lib.rope.grammar.CommandVisitor import CommandVisitor
from lib.rope.rope import Rope

FLAGS = flags.FLAGS

default_filename = os.path.join(os.path.dirname(__file__), 'data/data.txt')

flags.DEFINE_string('input', default_filename, 'input filename')
flags.DEFINE_integer('length', 10, 'rope length')


class RopeDriver(CommandVisitor):
    rope: Rope

    def __init__(self, rope: Rope, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rope = rope

    def visitCommand(self, ctx):
        direction = self.visitDirection(ctx.direction())
        count = self.visitCount(ctx.count())
        logging.info(f'command {direction} {count}')
        self.rope.move(direction, count)

    def visitDirection(self, ctx) -> str:
        return ctx.getText()

    def visitCount(self, ctx) -> int:
        return int(ctx.getText())


def main(argv):
    data = antlr4.FileStream(FLAGS.input)
    lexer = CommandLexer(data)
    stream = antlr4.CommonTokenStream(lexer)
    parser = CommandParser(stream)
    rope = Rope(FLAGS.length)
    visitor = RopeDriver(rope)

    visitor.visit(parser.commands())
    print(rope.num_visited())


if __name__ == '__main__':
    app.run(main)
