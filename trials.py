"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    evenNums = []

    for num in nums:
        if num % 2 == 0:
            evenNums.append(num)
    
    return evenNums


def get_odd_indices(items): #ask about this one during review
    result = []

    index = 0
    
    #return range(items[0], items[-1], 2)
    for item in items:
        if index % 2 != 0:
            result.append(item)
        index = index + 1
    
    return result


def print_as_numbered_list(items):

    i = 1
    
    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    nums = []
    nums = list(range(start, stop))
    return nums


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)
    
    return "".join(chars)


def snake_to_camel(string):
    #change word[0] to uppercase
    #whenever there is an _ get rid of it and have the next letter be uppercase
    string_list = string.split('_')
    CamelCase = []
    for word in string_list:
        word = word.capitalize()
        CamelCase.append(word)
    
    return "".join(CamelCase)


def longest_word_length(words):
    
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest


def truncate(string):
    result = []
    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    result = "".join(result)
    return result


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1

            if parens < 0:
                return False
    return parens == 0


def compress(string):
    compressed = []
    last_char = ' '
    char_count = 0
    for char in string:
        if char != last_char:
            compressed.append(last_char)

            if char_count > 1:
                compressed.append(str(char_count))

            last_char = char
            char_count = 0
        
        char_count += 1
    
    compressed.append(last_char)
    if char_count > 1:
        compressed.append(char_count)
    
    return "".join(compressed)