a_list = [1, 3, "test", 4.5, True]
a_tuple = (2, 4, "example", 3.5, False)
my_last_element = a_list[-1]
a_dict = {"key1": "value1", "key2": 42, "key3": [1, 2, 3]}
part_of_the_list = a_list[1:4]
a_dict["key4"] = "new_value"

def main():
    print("List:", a_list)
    print("Tuple:", a_tuple)
    print("Last element of the list:", my_last_element)
    print("Dictionary:", a_dict)
    print("Sliced part of the list (index 1 to 3):", part_of_the_list)
    print("Updated dictionary with new key-value pair:", a_dict)

if __name__ == "__main__":
    main()