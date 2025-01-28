def find_intersection(list1, list2):
    intersection = list(set(list1) & set(list2))
    return intersection
def find_union(list1, list2):
    union = list(set(list1) | set(list2))
    return union
# Example Usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection_result = find_intersection(list1, list2)
union_result = find_union(list1, list2)
print("Intersection:", intersection_result)
print("Union:", union_result)