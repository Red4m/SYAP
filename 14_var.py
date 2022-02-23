import math


def get_expression_result():
    a = input("enter a: ")
    x = input("enter x: ")
    if a.isdigit() and x.isdigit():
        a = float(a)
        x = float(x)
    else:
        return {"error": "enter numbers , not str"}

    try:
        result = -1/(5*x**3) * math.atan(2*a/x) + 1/(3*a*x**2) + 1/(3*x*a**2) + 1/(7*a**3) * math.log10(2*x**2 + a**2)
        return {"result": result}
    except ZeroDivisionError:
        return {"error": "ups, enter valid data , not zero"}


def main():
    while True:
        response = get_expression_result()
        if response.get("error"):
            print(response["error"])
            continue
        else:
            print(response["result"])
            break


if __name__ == "__main__":
    main()
