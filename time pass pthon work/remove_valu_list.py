
def remove_ith_occurrence(word_list,word,i):
    """
    Remove the i-th occurrence of given word in the word list.
    Args:
    -word_list(list):list of word where removal will be performed 
    -word(str):the word to remove. 
    -i(int):the occurrence number to remove. 
    return:
    -bool: True if the removal was successful,False otherwise.
    """
    count=0
    for index,w in enumerate(word_list):
        if w==word:
            count+=1
            if count == 1:
                del word_list[index]
                return True
    return False 

def main():
    #Example usage:
    word_list = ["apple","banana","apple","orange","apple"]
    word_to_remove = "apple"
    occurrence_to_remove = 2
    if remove_ith_occurrence(word_list,word_to_remove,occurrence_to_remove):
        print(f"Removed {occurrence_to_remove}-th occurrence of '{word_to_remove}':{word_list}")
    else:
        print(f"'{word_to_remove}' occurrence less then{occurrence_to_remove} times in the list.")

    if __name__ =="__main__":
        main()



    
