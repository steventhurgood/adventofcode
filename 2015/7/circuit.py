from typing import Sequence
from typing import Dict
from typing import Iterator

from dataclasses import dataclass

from absl import app
import os

data_file = os.path.join(os.path.dirname(__file__), "data/test_data.txt")


class Component:
    def evaluate(self) -> int:
        raise NotImplementedError('Component does not implement evaluate()')


class Circuit:
    wires: Dict[str, Component]

    def __init__(self):
        self.wires = {}

    def assemble(self, instructions: Iterator[str]):
        for line in instructions:
            parts = line.strip().split()

            if len(parts) == 3:
                # 44430 -> b
                number = parts[0]
                to_wire = parts[2]
                self.wires[to_wire] = Input(self, number)
                continue

            if parts[0] == 'NOT':
                # NOT dq -> dr

                from_wire = parts[1]
                to_wire = parts[3]
                self.wires[to_wire] = Not(self, from_wire)
                continue

            if parts[1] == 'AND':
                # eg AND ei -> ej
                left_wire = parts[0]
                right_wire = parts[2]

                to_wire = parts[4]
                self.wires[to_wire] = And(self, left_wire, right_wire)
                continue

            if parts[1] == 'OR':
                # eg AND ei -> ej
                left_wire = parts[0]
                right_wire = parts[2]

                to_wire = parts[4]
                self.wires[to_wire] = Or(self, left_wire, right_wire)
                continue

            if parts[1] == 'LSHIFT':
                # eo LSHIFT 15 -> es
                wire = parts[0]
                shift = int(parts[2])

                to_wire = parts[4]
                self.wires[to_wire] = LeftShift(self, wire, shift)
                continue

            if parts[1] == 'RSHIFT':
                # eo RSHIFT 15 -> es
                wire = parts[0]
                shift = int(parts[2])

                to_wire = parts[4]
                self.wires[to_wire] = RightShift(self, wire, shift)
                continue

            raise Exception(f'Error parsing line: {line}')


class Input(Component):
    circuit: Circuit
    wire: str

    def __init__(self, circuit: Circuit, wire: str):
        self.circuit = circuit
        self.wire = wire

    def evaluate(self) -> int:
        if self.wire.isnumeric():
            return int(self.wire)

        source = self.circuit.wires[self.wire]
        return source.evaluate()


class BinaryComponent(Component):
    circuit: Circuit
    left_wire: str
    right_wire: str

    def __init__(self, circuit: Circuit, left_wire: str, right_wire: str):
        self.left_wire = left_wire
        self.right_wire = right_wire
        self.circuit = circuit


class And(BinaryComponent):
    def evaluate(self) -> int:
        left: Component
        if self.left_wire.isnumeric():
            left = Input(self, self.left_wire)
        else:
            left = self.circuit.wires[self.left_wire]
        right: Component
        if self.right_wire.isnumeric():
            right = Input(self, self.right_wire)
        else:
            right = self.circuit.wires[self.right_wire]
        return left.evaluate() & right.evaluate()


class Or(BinaryComponent):
    def evaluate(self) -> int:
        left: Component
        if self.left_wire.isnumeric():
            left = Input(self, self.left_wire)
        else:
            left = self.circuit.wires[self.left_wire]
        right: Component
        if self.right_wire.isnumeric():
            right = Input(self, self.right_wire)
        else:
            right = self.circuit.wires[self.right_wire]
        return left.evaluate() | right.evaluate()


class Not(Component):
    circuit: Circuit
    wire: str

    def __init__(self, circuit: Circuit, wire: str):
        self.wire = wire
        self.circuit = circuit

    def evaluate(self) -> int:
        source: Component
        if self.wire.isnumeric():
            source = Input(self, self.wire)
        else:
            source = self.circuit.wires[self.wire]
        return 0xFFFF - source.evaluate()


class Shifter(Component):
    circuit: Circuit
    wire: str
    shift: int

    def __init__(self, circuit: Circuit, wire: str, shift: int):
        self.circuit = circuit
        self.wire = wire
        self.shift = shift


class LeftShift(Shifter):
    def evaluate(self) -> int:
        source: Component
        if self.wire.isnumeric():
            source = Input(self, self.wire)
        else:
            source = self.circuit.wires[self.wire]
        value = (source.evaluate() << self.shift) & 0xFFFF
        if value < 0:
            value = value + 0xFFFF
        return value


class RightShift(Shifter):
    def evaluate(self) -> int:
        source: Component
        if self.wire.isnumeric():
            source = Input(self, self.wire)
        else:
            source = self.circuit.wires[self.wire]
        value = source.evaluate() >> self.shift
        if value < 0:
            value = value + 0xFFFF
        return value


def main(argv):
    c = Circuit()

    with open(data_file) as f:
        c.assemble(f)
        for letter in 'defgh':
            output = c.wires[letter].evaluate()
            print(output)


if __name__ == '__main__':
    app.run(main)
