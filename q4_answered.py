
def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string; if it is not, return -1.
    - Return the reversed string.
    """
    # 1) Ensure s is a string
    if not isinstance(s, str):
        return -1

    # 2) Reverse the string using slicing
    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

# Scenario 1: "Hello World"
result1 = string_reverse("Hello World")
print("Reversed:", result1)
# output:
# Reversed: dlroW olleH

# Scenario 2: "Python"
result2 = string_reverse("Python")
print("Reversed:", result2)
# output:
# Reversed: nohtyP
