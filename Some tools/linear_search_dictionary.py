def linear_search_dictionary(dictionary, target_value):
    for x in range(len(dictionary)):
        if dictionary[x] == target_value:
            print("Found at index", x)
            return x
        print("Target is not in the list")
    return None 

dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(dictionary, 5)
linear_search_dictionary(dictionary, 3)
linear_search_dictionary(dictionary, 8)