
def money():
    money1=int(input("Input amount of money: "))
    return money1

def apple():
    apple1=int(input("Input price of apple: "))
    return apple1

def amount():
    amount1=(money())
    amount2=(apple())

    main(amount1, amount2)

def main(amount1, amount2):

    amount3=amount1//amount2
    amount4=amount1%amount2
    print(f"amount of apples: {amount3}")
    print(f"amount of change: {amount4}")


    









