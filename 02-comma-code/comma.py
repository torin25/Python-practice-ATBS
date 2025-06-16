def sep_comma(spam):
    # without using join operation
    # l=len(spam)
    # string=""
    # for i in range(l):
    #     if i!=l-1:
    #         string+=f"{spam[i]}, "
    # string+=f"and {spam[l-1]}"
    # return string
    
    # using join operation
    if len(spam)==1:
        return spam[0]
     
    return ", ".join(spam[:-1])+", and "+spam[-1]



while True:
    try:
        num_of_entries=int(input("Enter the number of list entries: "))
        if num_of_entries<=0:
            print("\nPlease enter a valid input")
            continue
        break
    except Exception as e:
        print("\nAn Error occured: ",e,"\n")
        print("Please enter a valid input")
        continue

spam=[]    
for i in range(1,num_of_entries+1):
    entry=input(f"Enter the string-{i}: ")
    spam.append(entry)
    
print(sep_comma(spam))
