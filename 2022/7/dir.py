
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import List, Tuple, Map

input_filename = os.path.join(os.path.dirname(__file__), 'data/test_data.txt')


@dataclass
class Directory:
    files: List[Tuple[str, int]]
    subdirs: Map[str, Directory]


@dataclass
class DirectoryProcessor:
    root: Directory

    def __init__(self):
        self.root = Directory()

    def parse_output(self, lines: Sequence[str]) -> Tuple[
        List[Tuple[str, int]],
        Map[name, Directory]
    ]:
        files = []
        subdirs = {}
        for line in lines:
            parts = line.split()
            if parts[0] == 'dir':
                subdirs.append((parts[1], Directory()))
            else:
                files.append((parts[1]), int(parts[0]))

        return (files, dict(subdirs))

    def process(self, commands: Sequence[str]):
        processing_output = False  # are we processing a command, or
        output = []  # collected output from a command
        cwd = self.root
        for line in commands:
            if processing_output:
                # we are processing output from a command
                if line.startswith('$'):
                    processing_output = False
                    files, subdirs = self.parse_output(output)
                    cwd.files = files
                    cwd.subdirs = subdirs
                    output = []
                else:
                    output.append(line)
                    continue
