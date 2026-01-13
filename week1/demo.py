def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    num = int(input("Enter a non-negative integer: "))
    print(factorial(num))


if __name__ == "__main__":
    main()
