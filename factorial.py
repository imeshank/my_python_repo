# finding factorial

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n ==1:
        return 1
    else:
        fact = 1
        while (n>1):
            fact *= n
            n -= 1
        return fact

def main():
    # num = 5;
    num = int(input("\n Enter a number: \n"))
    print("Factorial of {} is {}".format(num, factorial(num)))
    print("success")

if __name__ == "__main__":
    main()