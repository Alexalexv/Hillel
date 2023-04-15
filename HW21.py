import json

lst_of_dict = []

with open('users.txt', 'r') as f:
    for line in f:
        if len(line.strip()) > 0:
            line_lst = line.split(sep=';')
            name = line_lst[0].strip()
            if line_lst[1].isdecimal():
                age = int(line_lst[1])
            else:
                age = ''
            phones_lst_raw = line_lst[2]
            phones_lst_raw = phones_lst_raw.split(sep=',')
            phones_lst = []
            for i in phones_lst_raw:
                i = i.strip()
                phones_lst.append(i)
            phones_str = ','.join(phones_lst)
            with open('users_out.txt', 'a') as f2:
                f2.write(f'{name};{age};{phones_str}\n')

            if age == '':
                age_dict = None
            else:
                age_dict = age
            if phones_lst[0] == '':
                phones_dict = []
            else:
                phones_dict = phones_lst
            dict_ = {"name": name, "age": age_dict, "phones": phones_dict}
            lst_of_dict.append(dict_)

print(lst_of_dict)

with open('users.json', 'w') as fj:
    json.dump(lst_of_dict, fj)


