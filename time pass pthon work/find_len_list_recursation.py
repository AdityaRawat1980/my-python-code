def list_length(lst):
    # Base case: if the list is empty, its length is 0
    if not lst:
        return 0
    # Recursive case: return 1 (for the current element) plus the length of the rest of the list
    return 1 + list_length(lst[1:])
# Example Usage
my_list = [1, 2, 3, 4, 5]
print("Length of the list:", list_length(my_list))