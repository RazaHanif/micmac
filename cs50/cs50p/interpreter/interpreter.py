def main():
    equation = input("Expression: ").lower().strip()
    num1, exp, num2 = equation.split()
    num1 = float(num1)
    num2 = float(num2)

    print(calc(num1, num2, exp))

def calc(n1, n2, e):
    match e:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            if n2 != 0:
                return n1 / n2
            else:
                return "cannot divide by 0"
        case _:
            return "??"
            
main()