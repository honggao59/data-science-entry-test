
def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if the key already exists
    if key in dct:
        # Print the original value
        print(dct[key])
    # Update (or insert) the key-value pair
    dct[key] = value
    return dct



# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

# Scenario 1: Starting from an empty dictionary
result1 = update_dictionary({}, "name", "Alice")
print("Updated dictionary:", result1)
# Output:
# Updated dictionary: {'name': 'Alice'}


# Scenario 2: Updating an existing key ("age")
result2 = update_dictionary({"age": 25}, "age", 26)
print("Updated dictionary:", result2)
# Output:
#   25
#   Updated dictionary: {'age': 26}
