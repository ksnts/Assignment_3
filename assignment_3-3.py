#function for total money
def money():
    money1=int(input("Input amount of money: "))
    return money1
#function for apple price
def apple():
    apple1=int(input("Input price of apple: "))
    return apple1
#function to call 
def amount():
    amount1=(money())
    amount2=(apple())

    main(amount1, amount2)
#function for calculating amount and change
def main(amount1, amount2):

    amount3=amount1//amount2
    amount4=amount1%amount2
    print(f"You can buy amount of apples: {amount3}")
    print(f"Your change is: {amount4}")
#call
amount()
    









