def create_list():
    # Create a list
    my_list = [1, 2, 3, 4, 5]
    return my_list
def access_list(my_list):
    # Access elements in the list
    for item in my_list:
        print(item)
def update_list(my_list):
    # Add item to the list
    my_list.append(6)
    
    # Remove item from the list
    #my_list.remove(3)

    return my_list
def delete_list(my_list):
    # Delete the entire list
    del my_list
    # Uncomment the line below if you want to verify the deletion (it will raise an error)
    # print(my_list)

def main():
    # Create a list
    my_list = create_list()
# Access elements in the list
    print("Elements in the list:")
    access_list(my_list)

    # Update the list (Add item, Remove item)
    print("\nUpdated list:")
    updated_list = update_list(my_list)
    print(updated_list)
# Delete the list
    print("\nDeleting the list...")
    delete_list(updated_list)

if __name__ == "__main__":
    main()