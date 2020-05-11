d = {"name": "Anton",
     "cities": {"Moscow": "Moscow", "Piter": "Piter"},
     "Gender": "Male",
     }

unpacked_dictionary = {}


def unpack_all_keys(dictionary, empty_dict):
    if isinstance(dictionary, dict):
        for key, value in dictionary.items():
            empty_dict.update({key: value})
            unpack_all_keys(value, empty_dict)

    return empty_dict


print(unpack_all_keys(d, unpacked_dictionary))
