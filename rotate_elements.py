def rotate_list(input_list, n):
    output_list = []
    count = len(input_list) - n
    i = 0
    while i < count:
        each_element = input_list[i]
        output_list.append(each_element)
        i = i+1
    j = 0
    while count < len(input_list):
        each_element = input_list[count]
        output_list.insert(j, each_element)
        j = j + 1
        count = count + 1



    return output_list

input_list = [1,2,3,4,5,6]
n = 4
print(rotate_list(input_list,4))





