import sys

def main():
    if len(sys.argv) > 2:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
        except ValueError:
            print("Error: Please provide valid numbers as arguments.")
            sys.exit(1)
    else:
        num1 = 10
        num2 = 20

    total = num1 + num2
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"The sum is: {total}")

if __name__ == "__main__":
    main()
