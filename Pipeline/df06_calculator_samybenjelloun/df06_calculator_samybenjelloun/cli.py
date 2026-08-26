import argparse

from df06_calculator_samybenjelloun.math_operations import add, subtract, multiply, divide

def main():
    parser = argparse.ArgumentParser(description="A simple calculator.")
    parser.add_argument("--add",      nargs=2, type=int, help="Add two numbers")
    parser.add_argument("--subtract", nargs=2, type=int, help="Subtract the second number from the first")
    parser.add_argument("--multiply", nargs=2, type=int, help="Multiply two numbers")
    parser.add_argument("--divide",   nargs=2, type=int, help="Divide the first number by the second")
    args = parser.parse_args()

    if args.add:
        a, b = args.add
        print(f"{a} + {b} = {add(a, b)}")
    elif args.subtract:
        a, b = args.subtract
        print(f"{a} - {b} = {subtract(a, b)}")
    elif args.multiply:
        a, b = args.multiply
        print(f"{a} * {b} = {multiply(a, b)}")
    elif args.divide:
        a, b = args.divide
        print(f"{a} / {b} = {divide(a, b)}")

if __name__ == "__main__":
    main()
