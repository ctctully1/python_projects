# Take pascal or camel case string and converting to snake case
def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
           snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')
    return clean_snake_cased_string

def comp_case_converter(pascal_or_camel_string):
    snake_cased_char_list = []

    char = ['_'+i.lower() if i.isupper() else i for i in pascal_or_camel_string]
    snake_cased_char_list = char
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')
    return clean_snake_cased_string

def main():
    #print(convert_to_snake_case('aLongAndComplexString'))
    print(comp_case_converter('aLongAndComplexString'))

if __name__ == '__main__':
    main()