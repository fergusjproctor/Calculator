edit_list = object_list.copy()
i = 0
while i < len(edit_list):
    try:
        edit_list[i] = edit_list[i].__hash__()
        i += 1
    except TypeError:
        edit_list.remove(edit_list[i])
dict_ = {}
for ele in edit_list:
    if ele not in dict_.keys():
        dict_[ele] = edit_list.count(ele)
print(sum(dict_[ele] for ele in dict_ if dict_[ele] > 1))
