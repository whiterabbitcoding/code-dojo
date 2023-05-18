# def encrypt_text(plaintext, n):
#     dict_from_input = ""
#     # iterate over the given text
#     for i in range(len(plaintext)):
#         ch = plaintext[i]

#         if ch == " ":
#             dict_from_input += " "
#         elif ch.isupper():
#             ans += chr((ord(ch) + n - 65) % 26 + 65)
#         else:
#             ans += chr((ord(ch) + n - 97) % 26 + 97)

#     return dict_from_input


# print(encrypt_text("stuff", 1))


from typing import List


example = ["X:-1", "Y:1", "X:-4", "B:3", "X:5"]


def convert_str_array(string_array: List[str]) -> list:
    """
    Could use some comprehension in a refactor and less if statements, but does
    the job :)
    """
    dict_from_input = {}
    for i in string_array:
        splitted = i.split(":")
        if splitted[0] in dict_from_input.keys():
            dict_from_input[splitted[0]] += int(splitted[1])
        else:
            dict_from_input[splitted[0]] = int(splitted[1])

    summed_as_list = []
    for k, v in sorted(dict_from_input.items()):
        if v == 0:
            continue
        else:
            output_string = f"{k}:{v}"
            summed_as_list.append(output_string)

    return ",".join(summed_as_list)

    # [f"{k}:{v}" if v != 0 else continue for k, v in dict_from_input.items()]
    # print(dict_from_input)


print(convert_str_array(example))

ex2 = ["Z:0", "A:-1"]

print(convert_str_array(ex2))
