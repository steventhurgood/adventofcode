def find_offset(input: str, n: int = 14) -> int:
    for i in range(n, len(input)):
        chars = set(input[i-n:i])
        if len(chars) == n:
            return i
    raise Exception(f'No non-repeating string of {n} chars found')
