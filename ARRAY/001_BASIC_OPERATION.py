

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


if __name__ == "__main__":
    main()