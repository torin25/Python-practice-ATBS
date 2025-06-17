def print_picture_grid(grid):
    l1=len(grid)
    l2=len(grid[0])

    for i in range(l2):
        for j in range(l1):
            print(grid[j][i],end="")
        print("")

def get_user_input(prompt):
    while True:
        try:
            user_entry=int(input(prompt))
            if user_entry<=0:
                print("\nPLease enter a valid input")
                continue
            return user_entry

        except Exception as e:
            print("\nError occured: ",e)
            print("\nPlease enter a valid input")
            continue
     

def get_list_entries(num_of_lists,num_of_entries):
    main_list=[]
    for i in range(1,num_of_lists+1):
        inner_list=[]
        for j in range(1,num_of_entries+1):
            inner_list.append(input(f"Enter the entry {j} for list {i}: "))
        print("")
        main_list.append(inner_list)
    return main_list


def main():
    num_of_lists= get_user_input("Enter the number of lists in the main list: ")
    num_of_entries=get_user_input("Enter the number of entries in each list: ")

    print(f"\nNumber of lists in the main list: {num_of_lists}")
    print(f"Number of entries in each list: {num_of_entries}\n")
    main_list=get_list_entries(num_of_lists,num_of_entries)
    print(f"Grid formed: {main_list}")

    print("\nThe image grid: ")
    print_picture_grid(main_list)
    

main()






    