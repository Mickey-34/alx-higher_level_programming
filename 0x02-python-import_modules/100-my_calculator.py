#!/usr/bin/python3


def calculator():
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    ope = sys.argv[2]
    if ope != '+' and ope != '-' and ope != '*' and ope != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    q = int(sys.argv[1])
    y = int(sys.argv[3])
    if ope == '+':
        res = add(q, y)
    if ope == '-':
        res = sub(q, y)
    if ope == '*':
        res = mul(q, y)
    if ope == '/':
        res = div(q, y)
    print('{} {} {} = {}'.format(q, ope, y, res))


if __name__ == "__main__":
    calculator()
