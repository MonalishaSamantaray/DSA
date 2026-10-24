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
            try:
                start=int(input("Enter start index:"))
                end=int(input("Enter end index:"))
                print(f"sliced list [{start}:{end}]:",my_list[start:end])
            except Exception as e:
                print("Error:",e)
        elif choice== '4':
            try:
                idx = int(input(f"Enter the index to update (0 to {len(my_list)-1}):"))
                val = int (input("Enter new value:"))
                my_list[idx]=val
                print("Updated list:",my_list)
            except Exception as e:
                print("Error:",e)
        elif choice =='5':
            val= int(input("Enter value to insert:"))
            pos=input("Insert at 'end' or specific index? ").lower()
            if pos =='end':
                my_list.append(val)
            else:
                idx = int(input("Enter index:"))
                my_list.insert(idx,val)
            print("updated list:",my_list)
        elif choice =='6':
            val=int(input("Enter value to remove:"))
            try:
                my_list.remove(val)
                print("Updated list:",my_list)
            except ValueError:
                print("Value not found")
        elif choice =='7':
            val=int(input("Enter value to search:"))
            if val in my_list:
                print(f"Found {val} at index {my_list.index(val)}")
            else:
                print(f"{val} not found in list")
        elif choice == '8':
            print("Iterating through list")
            for item in my_list:
                print(item,end="")
            print()
        elif choice == '9':
            print("list + [100,200]:",my_list + [100,200])
            print("List * 2", my_list * 2)
        elif choice =='10':
            print("Sum", sum(my_list))
            print("Max", max(my_list))
            print("Min", min(my_list))
            print("Length", len(my_list))
        elif choice =='11':
            my_list.sort()
            print("Sorted list:",my_list)
            my_list.reverse()
            print("Reverse list:",my_list)
        elif choice =='12':
            break
        else:
            print("Invalide choice!!!!!")


def numpy_menu():
    arr=np.array([10,13,26,47,46,97,45,74,62,80,39])
    while True:
        print("\n******************************************")
        print("NUMPY ARRAY OPERATION")
        print("\n******************************************")
        print("1.Display Array")
        print("2.Access the element")
        print("3.Slicing")
        print("4.Update element")
        print("5.Search element")
        print("6.Iterate through array")
        print("7.Vectorise mathematical operation")
        print("8.Aggregation(Sum,Max,Min,Mean)")
        print("9.Sort and Reverse")
        print("10.Return to main menu")

        choice = input("Enter your chice(1-12):")

        if choice =='1':
            print("Current Array:\n",arr)
        elif choice =='2':
            try:
                idx = int(input(f"Enter index (0 to {len(arr)-1}):"))
                print(f"Element to index{idx}:{arr[idx]}")
            except Exception as e:
                print("Eroor:",e)
        elif choice == '3':
            try:
                start=int(input("Enter start index:"))
                end=int(input("Enter end index:"))
                print(f"sliced list [{start}:{end}]:",arr[start:end])
            except Exception as e:
                print("Error:",e)
        elif choice== '4':
            try:
                idx = int(input(f"Enter the index to update (0 to {len(arr)-1}):"))
                val = int (input("Enter new value:"))
                arr[idx]=val
                print("Updated Array:",arr)
            except Exception as e:
                print("Error:",e)
        elif choice =='5':

            val=int(input("Find element greater than value:"))
            filtered=arr[arr>val]
            print(f"Element>{val}:",filtered)
        elif choice == '6':
            print("Iterating through array")
            for item in arr:
                print(item,end="")
            print()

        elif choice == '7':
            print("Original array:",arr)
            print("Array + 5 (Scalar addition):",arr+5)
            print("Array * 5 (Scalar multiplication):",arr*5)
            print("Square root of element:",np.sqrt(arr))
        elif choice =='8':
            print("Sum:",np.sum(arr))
            print("Mean:",np.mean(arr))
            print("Max:",np.max(arr))
            print("Min:",np.min(arr))
        elif choice == '9':
            sorted_arr=np.sort(arr)
            print("Sorted Array:",sorted_arr)
            reversed_arr=arr[::-1]
            print("Reversed array:",reversed_arr)
        elif choice == '10':
            break
        else:
            print("Invalid choice!!!!!!!!")
def main():
    while True:
        print("\n####################")
        print("Array Operation Main Menu")
        print("\n####################")
        print("1.Work with python list")
        print("2.Work with numpy array")
        print("3.EXIT ")
        main_choice=input("Enter your choice(1-3):")
        if main_choice == '1':
            list_menu()
        elif main_choice == '2':
            numpy_menu()
        elif main_choice == '3':
            print("Exiting program.goodbye!!")
            break
        else:
            print("Invalid choice!!")
if __name__=="__main__" :
    main()
