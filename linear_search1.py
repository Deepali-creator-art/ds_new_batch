#input parameters
def linear_search(arrays,search_element):
    #count the elements of a list
    size=len(arrays)
    target_number_index=[] #to collect index number of target value
    for i in range(size):
        if(arrays[i]==search_element):
            target_number_index.append(i)                          
    if(len(target_number_index)==0):
        print(f"Element {search_element} is not found")
    else:
        print(f"Element {search_element} is found")
        print(f"Targeted number index ",target_number_index)   
items=['Pratham','Pratiksha','Sarvesh','Pratiksha']
target_value=input("Enter the search element")
linear_search(items,target_value) #function call