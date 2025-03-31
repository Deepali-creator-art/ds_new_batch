def linear_search(arrays, search_element):
    # Count the elements of a list
    found_indices = []  # List to store the indices where the element is found
    
    for i in range(len(arrays)):
        if arrays[i] == search_element:
            found_indices.append(i)  # Add the index to the list
            
    if found_indices:
        print("Search element", search_element, "is present in the list at indices:", found_indices)
    else:
        print("Search element", search_element, "is not present in the list")

items = ['pratham', 'pratiksha', 'sarvesh', 'pratiksha']
target_value = input("Enter the search element: ")  # Input as string
linear_search(items, target_value)  # Function call