
def linear_search(arrays,search_element):
    #count the elements of a list
    size=len(arrays)
    for i in range(size):
        if(arrays[i]==search_element):
            print("Search element ",search_element,"present in list")
            break
        else:
            print("Search element ",search_element,"is not present in list")  
items=[23,12,67,89,56,90,28,56,78,34,27]
target_value=int(input("Enter the search element"))
linear_search(items,target_value) #function call