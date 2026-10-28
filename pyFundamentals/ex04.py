def get_php():
    return float(input("Amount in PHP: "))

def get_rate():
    return float(input("PHP per 1 USD: "))

def php_to_usd(php, rate):
    return php / rate

def display(php, usd):
    print(f"PHP {php:.2f} is about USD {usd:.2f}")

def main():
    php = get_php()
    rate = get_rate()
    usd = php_to_usd(php, rate)
    display(php, usd)

if __name__ == '__main__':
    main()