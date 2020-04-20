import generator_instancji as gi

def longest_in_seq(sequence):
    longest_substr = ''
    tmp_substr = ''
    for id, letter in enumerate(sequence):
        if id > 0:
            if letter == sequence[id-1]:
                tmp_substr += letter
            else:
                if len(tmp_substr) > len(longest_substr):
                    longest_substr = tmp_substr
                tmp_substr = letter
        else:
            longest_substr = letter
            tmp_substr = letter

    return longest_substr, len(longest_substr)


generated_string = gi.create_word()

txt, length = longest_in_seq("banannnnannnnnnnnnanananananaaaanaxxxxxxxxxxy")
print("test, dl:", txt, length)