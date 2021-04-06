
def target_word_position(input_sentence,input_word):
    return_list = []
    input_sentence_list = input_sentence.split()
    print(input_sentence_list)
    word_position = 1
    for i in input_sentence_list:
        #print(i, word_position)
        if i == input_word:
            return_list.append(word_position)
            print(i, word_position)
        word_position = word_position + 1


    return return_list


inp_sentence = "I love NJ as NJ has a lot of good restaurant within NJ"
inp_word = "NJ"
output_list = target_word_position(inp_sentence,inp_word)
print(output_list)

def convert(list_to_dict):
    new_result = iter(list_to_dict)
    result_dict = dict(zip(new_result, new_result))
    return result_dict

nr = ['I', 'love', 'NJ', 'as', 'NJ', 'has', 'a', 'lot', 'of', 'good', 'restaurant', 'within', 'NJ']
print(convert(nr))
