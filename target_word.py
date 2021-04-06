import numpy as np
def target_word_position(input_sentence,input_word):
    return_list = []
    input_sentence_list = input_sentence.split()
    #print(input_sentence_list)
    word_position = 1
    for i in input_sentence_list:
        #print(i, word_position)
        if i == input_word:
            return_list.append(word_position)
            #print(i, word_position)
        word_position = word_position + 1

    print(input_word," ",return_list)
    return return_list

def convert(input_string):
    new_dict = {}
    input_sentence_list = input_string.split()
    #print(input_sentence_list)
    x = np.array(input_sentence_list)
    unique_word_list = np.unique(x)
    #print(unique_word_list)
    for each_word in unique_word_list:
        word_position = target_word_position(input_string,each_word)
        count_word = len(word_position)
        #print(each_word, " ", word_position," ",count_word)
        new_dict[each_word] = count_word
    return new_dict







inp_sentence = "I love NJ as NJ has a lot of good restaurant within NJ"
inp_word = "NJ"
#output_list = target_word_position(inp_sentence,inp_word)
#print(output_list)
print(convert(inp_sentence))

