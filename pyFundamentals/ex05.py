def get_num1():
    return int(input("Enter 1st number: "))

def get_num2():
    return int(input("Enter 2nd number: "))

def process(n1, n2):
    result = []
    result.append(n1 + n2)
    result.append(n1 - n2)
    result.append(n1 * n2)
    result.append(n1 / n2)
    result.append(n1 // n2)
    result.append(n1 % n2)
    result.append(n1 ** n2)
    return result

def display(result):
    labels = ["Sum", "Difference", "Product", "Quotient",
              "Floor Division", "Modulus", "Exponent"]
    for i in range(len(result)):
        print(f"{labels[i]}: {result[i]}")

def main():
    n1 = get_num1()
    n2 = get_num2()

    result = process(n1, n2)
    display(result)

if __name__ == '__main__':
    main()