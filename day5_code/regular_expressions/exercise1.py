import re


def check_dice(input_string):
    # Zkontroluj jestli je v input_string validni hazeni kostkou
    # Vrat True pokud ano, False pokud ne

    dice_pattern = r'\d*[dD]{1}\d+([+-]{1}\d+)?'
    compiled_pattern = re.compile(dice_pattern)
    search_result = re.search(compiled_pattern, input_string)

    print("search_result: ", search_result)
    if search_result is not None:
        print("Matched text to pattern: ", {search_result.group()})

    if search_result is None:
        return False
    return True

#text1 = "8d7+10"
#text2 = "8s7+10"
#text3 = "8D7+10 abcdefghijk"
text4 = "8d-h"
print(check_dice(text4))