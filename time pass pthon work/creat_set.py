my_set = {1,2,3,4,5,5,5,5,6,7,8,9,10}
print(my_set)
my_set.add(11) # add  element in set
print(my_set)
hi_set ={3,4,5,6,7}
print(my_set.union(hi_set), "----------",my_set | hi_set)
print(my_set.intersection(hi_set), "----------",my_set & hi_set)
print(my_set.difference(hi_set), "----------",my_set - hi_set) # IN THIS SIT CHECK THAT THE FIRST SET 'S DIFFERENT VALUES
print(my_set.symmetric_difference(hi_set), "----------",my_set ^ hi_set) # IT WILL CHECK THE BOTH SET 'S UNIQUE VALUES
my_set.clear()
print(my_set)