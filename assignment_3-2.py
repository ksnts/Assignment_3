#functions for amount of oranges and apples
def buyO():
    orange1=int(input("Input amount of oranges: "))
    return orange1

def buyA():
    apple1=int(input("Input amount of apples: "))
    return apple1
#functions for prices
def priceO():
    price1=25
    return price1

def priceA():
    price2=20
    return price2
#main function that multiplies price and amount
def main_code():
    total1=(buyO()*priceO())
    total2=(buyA()*priceA())
    main1(total1, total2)
#function for sum
def main1(total1, total2):
    print(f"Total amount is: {total1 +total2} ")
#call
main_code()





