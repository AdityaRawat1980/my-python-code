def roman_to_int(s):
    # Dictionary to map Roman numerals to their integer values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the result
    result = 0
    n = len(s)
    # print(n,"\n")
    # Iterate through the string
    for i in range(n):
        # # print(i,"\n")
        # print(roman_values[s[i]])
        # print(roman_values[s[i + 1]])
        # If this is not the last character and the current character is less than the next one
        if i < n - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
            # Subtract the current character's value
            result -= roman_values[s[i]]
            print(result)
        else:
            # Add the current character's value
            result += roman_values[s[i]]
    
    return result

# Example usage:
# print(roman_to_int("III"))      # Output: 3
# print(roman_to_int("LVIII"))    # Output: 58
# print(roman_to_int("MCMXCIV"))  # Output: 1994
