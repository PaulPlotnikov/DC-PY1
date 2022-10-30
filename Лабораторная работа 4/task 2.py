def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    diction = {}
    for i in str_:
        if i.isalpha() == True:
            if i in diction:
                diction[i] += 1
            else:
                diction[i] = 1
    #print ('Dictionary: \n',  str(diction))
    return(diction)

def get_dictionary(diction_):
    new_diction = {}
    max_val = max(diction_.values())
    for key in diction_:
        percentage = (diction_.get(key)/max_val)*100
        new_diction[key] = percentage
    return(new_diction)

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_dictionary(get_count_char(main_str)))

