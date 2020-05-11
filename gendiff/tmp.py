d = {"name1": "Anton",
     "name2": "Vasya",
     "cities": {"Moscow": "Moscow", "Piter": "Piter"},
     "Gender": "Male",
     "Gender2": "Female"
     }


d2 = {"name1": "Anton",
     "name2": "Vasya2",
     "cities": {"Moscow": "Moscow", "Piter": "Piter2"},
     "Gender": "Male",
     }

unpacked_dictionary = {}

test1 = {
  "common": {
    "setting1": "Value 1",
    "setting2": "200",
    "setting3": "true",
    "setting6": {
      "key": "value"
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar"
  },
  "group2": {
    "abc": "12345"
  }
}
test2 = {
  "common": {
    "setting1": "Value 1",
    "setting3": "true",
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    }
  },

  "group1": {
    "foo": "bar",
    "baz": "bars"
  },

  "group3": {
    "fee": "100500"
  }
}


def unpack_all_keys(dictionary, empty_dict):
    if isinstance(dictionary, dict):
        for key, value in dictionary.items():
            empty_dict.update({key: value})
            unpack_all_keys(value, empty_dict)

    return empty_dict


def test(before, after):
    for key, value in before.items():
        if isinstance(value, (dict, list)):
            if key not in after:
                print("{} removed".format(key))
                continue
            test(value, after[key])
        else:
            if key in after:
                print("dict1:{} = {}, dict2:{}".format(key, value, after[key]))
            else:
                print("dict1:{} = {}".format(key, value))


test(test1, test2)