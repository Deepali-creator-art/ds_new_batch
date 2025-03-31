#To search list element from a given list.
x=[5,15,20,35,40,27]
search_element=28
for i in x:
    if(i==search_element):
        print("Search element ",search_element,"present in list")
        break
else:
    print("Search element ",search_element,"is not present in list")
