"""This script """

def greeting(name):
    """This function takes in a name"""
    print(f"hello, {name}!")

def pack(item1, item2, item3):
    '''this function takes in 3 items and returns them in a list'''
    return [item1, item2, item3]

def eat_lunch(list):
    '''this function prints our lunchbox contents'''
    if len(list) == 0:
        print("Lunchbox empty!")
        return
    else: 
        for i in range(len(list)):
            if i == 0:
                print(f"First, I eat a {list[i]}")
            else:
                print(f"Then I eat a {list[i]}")
    
def test_all():
    """tests that all functions run properly"""
    greeting("test")
    print(pack("socks", "underwear", "shoes"))
    print(eat_lunch(["banana", "sandwich", "yogurt", "cheese stick"]))


'''Run our functions'''
test_all()

#comments in python

#variable declaration in python
some_var = 3
other_var = "happy"