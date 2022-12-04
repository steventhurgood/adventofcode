from absl import app, flags
import os


FLAGS = flags.FLAGS

default_filename = os.path.join(
    os.path.dirname(__file__), "data/data.txt")

flags.DEFINE_string("input", default_filename, 'File from whch to read codes')


class Escaper:
    def as_code(self, code: str) -> int:
        chars = 1  # initial '"' character

        for c in code:
            if c == '\\':
                chars += 2  # '/' -> '//'
                continue

            if c == '"':
                chars += 2  # '"' -> '/"'
                continue

            chars += 1

        return chars + 1  # final '"'

    def in_memory(self, code: str) -> int:
        chars = 0
        i = 1  # disregard initial " char

        while True:
            if code[i] == '"':
                return chars

            if code[i] == '\\' and code[i+1] == 'x':
                # '\xFF'
                chars += 1
                i += 4
                continue

            if code[i] == '\\':
                # '\\' or '\"'
                chars += 1
                i += 2
                continue

            chars += 1
            i += 1


def main(argv):
    e = Escaper()
    codes = 0
    in_memory = 0
    encoded = 0

    with open(FLAGS.input) as f:
        for line in f:
            count = e.in_memory(line.strip())
            as_code = e.as_code(line.strip())
            codes += len(line.strip())
            in_memory += count
            encoded += as_code
            print(
                f'{line.strip()} ({len(line.strip())}) ->in memory {count}; encoded {as_code}')

    print(codes, in_memory, codes - in_memory)
    print(codes, encoded, encoded - codes)


if __name__ == '__main__':
    app.run(main)
