my_list = [1, 2.3, 4, 5]
my_result = list(map(str,my_list))
print(my_result)

def remove_dash(input_text):
    return input_text.replace("-","")

string_list = ['2020-11-01','2020-11-02','2020-11-03']
string_result = list(map(remove_dash, string_list))
print(string_result)
