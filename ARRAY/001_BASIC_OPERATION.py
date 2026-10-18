import numpy as np
def list_menu():
    my_list=[10,13,26,47,46,97,45,74,62,80,39]
    while True:
        print("\n******************************************")
        print("PYTHON LIST OPERATION")
        print("\n******************************************")
        print("1.Display list")
        print("2.Access the element")
        print("3.Slicing")
        print("4.Update element")
        print("5.Insert element")
        print("6.Delete element")
        print("7.Search element")
        print("8.Iterate through array")
        print("9.Concatenation & Repitition")
        print("10.Aggregation(Sum,Max,Min,Length)")
        print("11.Sort and Reverse")
        print("12.Return to main menu")
        choice = input("Enter your chice(1-12):")


        if choice == '1':
            print("Current list:",my_list)
        elif choice =='2':
            try:
                idx = int(input(f"Enter index(0 to {len(my_list)-1})"))
                print((f"Element at index {idx}:{my_list}"))
            except Exception as e:
                print("Error:",e)
        elif choice == '3':
            



