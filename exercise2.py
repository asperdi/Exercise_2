
def roman_to_arabic(roman):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if not all(char in roman_map for char in roman):
        raise ValueError(f"Invalid Roman numeral character in: {roman}")
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        current_value = roman_map[char]
        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value
        prev_value = current_value
        
    if arabic_to_roman(total) != roman:
        raise ValueError(f"Invalid Roman numeral sequence: {roman}")
        
    return total

def arabic_to_roman(arabic):
    if not isinstance(arabic, int) or not (1 <= arabic <= 3999):
        raise ValueError("Input must be an integer between 1 and 3999.")
    
    val_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ""
    for value, numeral in val_map:
        while arabic >= value:
            result += numeral
            arabic -= value
            
    return result

if __name__ == '__main__':
    try:
        roman_num = "MCMXCIV"
        print(f"Roman numeral {roman_num} is {roman_to_arabic(roman_num)} in Arabic.")
        
        arabic_num = 1994
        print(f"Arabic number {arabic_num} is {arabic_to_roman(arabic_num)} in Roman.")
        
    except ValueError as e:
        print(f"Error: {e}")
