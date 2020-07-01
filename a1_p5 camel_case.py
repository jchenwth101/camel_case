
def length(input_string: str) -> int:
    """
    TODO: Write this implementation
    """
    return


def input_cleanup(input_string) -> str:
    """
    TODO: Write this implementation
    """
    # input_string = input('Type a string: ')
    out_put = ''
    # removeSpecialChars = re.sub("[!@#$%^&*()[]{};:,./<>?\|`~-=_+]", " ",)
    # for n in input_string:
    #    if n == ' ':
    #        n = '_'
    #    out_put += n
    # print(out_put)
    for n in input_string:
        if n in 'abcdefghijklmnopqrstuvwxyz':
            out_put = out_put + n
        elif n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            k = ord(n)
            l = k + 32
            out_put = out_put + chr(l)
        else:
            out_put += '_'

    while out_put != '' and out_put[0] == '_':
        out_put = out_put[1:]

    while out_put != '' and out_put[-1] == '_':
        out_put = out_put[:-1]

    new_out_put = ''

    for n in out_put:
        if n == '_':
            if new_out_put[-1] != '_':
                new_out_put += n
        else:
            new_out_put += n
    # print(out_put)
    # removeSpecialChars()
    return new_out_put

def is_clean_string(input_string: str) -> bool:
    """
    TODO: Write this implementation
    """
    underscore_counter = 0

    if input_string == '':
        return True

    if input_string[0] not in 'abcdefghijklmnopqrstuvwxyz':
        return False

    if input_string[-1] not in 'abcdefghijklmnopqrstuvwxyz':
        return False

    for i in input_string:
        if i not in 'abcdefghijklmnopqrstuvwxyz_':
            return False
        elif i == '_':
            if underscore_counter >= 1:
                return False
            underscore_counter += 1
        else:
            underscore_counter = 0  # reset counter

    return True


def camel_case(input_string: str, func_is_clean, func_cleanup):
    """Makes a snake case string into a camel case one
       Parameters
       -----------
       snake_case : str
           Snake-cased string (e.g., "snake_cased") to be converted to camel-case (e.g., "camelCase")
       Returns
       -------
       str
           Camel-cased (e.g., "camelCased") version of input string
       """
    # sanitize input string
    clean_input = func_cleanup(input_string)     # DO NOT DELETE / CHANGE

    # check if input string is ready for camelCase conversion

    if not func_is_clean(clean_input):           # DO NOT DELETE / CHANGE
        return None                              # DO NOT DELETE / CHANGE

    # check that input string has at least two words in it
    # return None if it does not
    if '_' not in clean_input:
        return None

    # convert clean input string into camelCase
    output_str = ''
    should_upper_case = False
    for c in clean_input:
        if c == '_':
            should_upper_case = True
            continue
        output_str = output_str + chr(ord(c ) -32) if should_upper_case else output_str + c
        should_upper_case = False
    return output_str



# BASIC TESTING
if __name__ == "__main__":
    if __name__ == "__main__":
        test_set = ("_random_ _word_provided",
                    "@$ptr*4con_", " ran  dom  word",
                    "example    word   ", "ANOTHER_Word",
                    "__", "_ _ _", "    ", "435%7_$$", "random")

        # example 1
        for test_string in test_set:
            result = input_cleanup(test_string)
            print(length(result), result)
        print()

        # example 2
        for test_string in test_set:
            result = input_cleanup(test_string)
            print(is_clean_string(test_string), is_clean_string(result))
        print()

        # example 3
        for test_string in test_set:
            result = camel_case(test_string, is_clean_string, input_cleanup)
            print("'" + test_string + "'", "-->", result)