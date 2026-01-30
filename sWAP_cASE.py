def swap_case(s):
    return "".join([chr(ord(c) ^ 32) if c.isalpha() else c for c in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)