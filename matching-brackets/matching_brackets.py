opening_brackets = ['(', '{', '[']
closing_brackets = [')', '}', ']']

def is_paired(input_string):
    first_bracket = -1
    min_loc = len(input_string)+1
    last_bracket = -1
    max_loc = -1
    
    for i in range(len(opening_brackets)):
        location = input_string.find(opening_brackets[i])
        if location == -1:
            location = len(input_string)+1
        else:
            if location < min_loc:
                min_loc = location
                first_bracket = i
                
        location = input_string.find(closing_brackets[i])
        if location > max_loc:
            max_loc = location
            last_bracket = i
                
    if last_bracket == -1 and first_bracket == -1:
        print("No brackets")
        return True
    
    elif last_bracket == first_bracket:
#         print("searching {}".format(input_string[min_loc+1: max_loc]))
        return is_paired(input_string[min_loc+1: max_loc])
    
    else:
        return False
    
if __name__ == "__main__":
    print(is_paired("J(O[H{NC]ODE)"))