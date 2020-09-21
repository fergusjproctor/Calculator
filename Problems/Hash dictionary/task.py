objects_dict = {}
for ele in objects:
    try:
        objects_dict[ele] = ele.__hash__()
    except TypeError:
        continue


