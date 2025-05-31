def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    # 1) Validate that lst is indeed a list
    if not isinstance(lst, list):
        return -1

    # 2) Iterate through lst and replace occurrences in place
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    # 3) Return the modified list
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

# Scenario 1: numeric list
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Scenario 1 Output:", result1)
# Scenario 1 Output: [1, 5, 3, 4, 5, 5]


# Scenario 2: string list
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Scenario 2 Output:", result2)
# Scenario 2 Output: ['orange', 'banana', 'orange']

