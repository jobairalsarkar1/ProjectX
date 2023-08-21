def filter_fields(arr, filter_arr):
    res_arr = []
    for field in arr:
        if field.name not in filter_arr:
            res_arr.append(field.name)

    return res_arr