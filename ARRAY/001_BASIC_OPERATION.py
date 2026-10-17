import numpy as np

def list_menu():
    # Initializing a sample list
    my_list = [10, 25, 15, 40, 30]
    
    while True:
        print("\n==============================")
        print("   PYTHON LIST OPERATIONS     ")
        print("==============================")
        print("1. Display List")
        print("2. Access Element (Indexing)")
        print("3. Slicing")
        print("4. Update / Modify Element")
        print("5. Insert Element")
        print("6. Delete / Remove Element")
        print("7. Search / Find Element")
        print("8. Iterate through List")
        print("9. Concatenation & Repetition")
        print("10. Aggregation (Sum, Max, Min, Len)")
        print("11. Sort and Reverse")
        print("12. Return to Main Menu")
        
        choice = input("Enter your choice (1-12): ")
        
        if choice == '1':
            print("Current List:", my_list)
            
        elif choice == '2':
            try:
                idx = int(input(f"Enter index (0 to {len(my_list)-1}): "))
                print(f"Element at index {idx}: {my_list[idx]}")
            except Exception as e:
                print("Error:", e)
                
        elif choice == '3':
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(f"Sliced List [{start}:{end}]:", my_list[start:end])
            except Exception as e:
                print("Error:", e)
                
        elif choice == '4':
            try:
                idx = int(input(f"Enter index to update (0 to {len(my_list)-1}): "))
                val = int(input("Enter new value: "))
                my_list[idx] = val
                print("Updated List:", my_list)
            except Exception as e:
                print("Error:", e)
                
        elif choice == '5':
            val = int(input("Enter value to insert: "))
            pos = input("Insert at 'end' or specific 'index'? (end/index): ").lower()
            if pos == 'end':
                my_list.append(val)
            else:
                idx = int(input("Enter index: "))
                my_list.insert(idx, val)
            print("Updated List:", my_list)
            
        elif choice == '6':
            val = int(input("Enter value to remove: "))
            try:
                my_list.remove(val)
                print("Updated List:", my_list)
            except ValueError:
                print("Value not found in list!")
                
        elif choice == '7':
            val = int(input("Enter value to search: "))
            if val in my_list:
                print(f"Found {val} at index {my_list.index(val)}")
            else:
                print(f"{val} not found in list.")
                
        elif choice == '8':
            print("Iterating through list:")
            for item in my_list:
                print(item, end=" ")
            print()
            
        elif choice == '9':
            print("List + [100, 200]:", my_list + [100, 200])
            print("List * 2:", my_list * 2)
            
        elif choice == '10':
            print("Sum:", sum(my_list))
            print("Max:", max(my_list))
            print("Min:", min(my_list))
            print("Length:", len(my_list))
            
        elif choice == '11':
            my_list.sort()
            print("Sorted List:", my_list)
            my_list.reverse()
            print("Reversed List:", my_list)
            
        elif choice == '12':
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 12.")

def numpy_menu():
    # Initializing a sample NumPy array
    arr = np.array([10, 25, 15, 40, 30])
    
    while True:
        print("\n==============================")
        print("   NUMPY ARRAY OPERATIONS     ")
        print("==============================")
        print("1. Display Array")
        print("2. Access Element (Indexing)")
        print("3. Slicing")
        print("4. Update / Modify Element")
        print("5. Search / Filter Elements")
        print("6. Iterate through Array")
        print("7. Vectorized Mathematical Operations")
        print("8. Aggregation Functions (Sum, Mean, Max, Min)")
        print("9. Sort and Reverse")
        print("10. Return to Main Menu")
        
        choice = input("Enter your choice (1-10): ")
        
        if choice == '1':
            print("Current Array:\n", arr)
            
        elif choice == '2':
            try:
                idx = int(input(f"Enter index (0 to {len(arr)-1}): "))
                print(f"Element at index {idx}: {arr[idx]}")
            except Exception as e:
                print("Error:", e)
                
        elif choice == '3':
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(f"Sliced Array [{start}:{end}]:", arr[start:end])
            except Exception as e:
                print("Error:", e)
                
        elif choice == '4':
            try:
                idx = int(input(f"Enter index to update (0 to {len(arr)-1}): "))
                val = int(input("Enter new value: "))
                arr[idx] = val
                print("Updated Array:", arr)
            except Exception as e:
                print("Error:", e)
                
        elif choice == '5':
            val = int(input("Find elements greater than value: "))
            filtered = arr[arr > val]
            print(f"Elements > {val}:", filtered)
            
        elif choice == '6':
            print("Iterating through array:")
            for item in arr:
                print(item, end=" ")
            print()
            
        elif choice == '7':
            print("Original Array:", arr)
            print("Array + 5 (Scalar Addition):", arr + 5)
            print("Array * 2 (Scalar Multiplication):", arr * 2)
            print("Square root of elements:", np.sqrt(arr))
            
        elif choice == '8':
            print("Sum:", np.sum(arr))
            print("Mean:", np.mean(arr))
            print("Max:", np.max(arr))
            print("Min:", np.min(arr))
            
        elif choice == '9':
            sorted_arr = np.sort(arr)
            print("Sorted Array:", sorted_arr)
            reversed_arr = arr[::-1]
            print("Reversed Array:", reversed_arr)
            
        elif choice == '10':
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 10.")

def main():
    while True:
        print("\n==================================")
        print("   ARRAY OPERATIONS MAIN MENU     ")
        print("==================================")
        print("1. Work with Python Lists")
        print("2. Work with NumPy Arrays")
        print("3. Exit Program")
        
        main_choice = input("Enter your choice (1-3): ")
        
        if main_choice == '1':
            list_menu()
        elif main_choice == '2':
            numpy_menu()
        elif main_choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()