
#functions for name age address
def name():
    name1=input("Input your name: ")
    return name1

def age():
    age1=input("Input your age: ")
    return age1

def address():
    add1=input("Input your address: ")
    return add1

#main function that we will call
def main_code():
    int1=name()
    int2=age()
    int3=address()
    main1 (int1, int2, int3)
    
#function for completing the datas collected
def main1 (int1, int2, int3):
    print(f"Hi, my name is {int1}. I am {int2} years old and I live in {int3}.")
#call
main_code()
