mylist = [1, 2.3, 4, 5]
result = list(map(str, mylist))
print(result)

def remove_char(input_text):
    return input_text.replace("-","")

string_list = ['2020-11-01', '2020-11-02', '2020-11-03']
string_result = list(map(remove_char, string_list))
print(string_result)


