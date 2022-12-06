from absl import app, flags, logging

FLAGS = flags.FLAGS


def looksay(input: str, repeat: int = 1) -> str:
    output = []
    previous_c = None
    previous_count = 0
    for c in input:
        if previous_c is None:
            previous_c = c
            previous_count = 1
            continue
        if previous_c != c:
            output.append(str(previous_count))
            output.append(previous_c)
            previous_count = 1
            previous_c = c
            continue
        previous_count += 1
    output.append(str(previous_count))
    output.append(previous_c)
    ret = ''.join(output)
    if repeat > 1:
        return looksay(ret, repeat-1)
    return ret


def main(argv):
    value = looksay('1321131112', 50)
    # print(value)
    print(len(value))


if __name__ == '__main__':
    app.run(main)
