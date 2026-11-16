from calculator import Calculator  # import from our own module


def main():
    calc = Calculator(precision=2)
    print("Calculator (type 'q' to quit, 'h' for history)")
    while True:
        text = input("Enter: number operator number (e.g. 5 + 3): ").strip()
        if text.lower() == "q":
            break
        if text.lower() == "h":
            print("\n".join(calc.history) or "No history yet")
            continue
        try:
            a, op, b = text.split()
            print("Result:", calc.calculate(float(a), op, float(b)))
        except (ValueError, ZeroDivisionError) as err:
            print("Error:", err)
    print(f"Total calculations: {Calculator.total_calculations}")


if __name__ == "__main__":
    main()
