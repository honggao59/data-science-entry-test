
def swap(x, y):
    """
    Task 1
    - Swap the values of x and y using only x and y as variables (no third variable).
    - x and y must be numeric (int or float).
    - Return -1 if either x or y is not numeric.
    - Otherwise, print the swapped values.
    """
    # 1) Check that both x and y are numeric (int or float)
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    # 2) Swap using arithmetic (no third variable)
    x = x + y
    y = x - y
    x = x - y

    # 3) Print the swapped values
    print(x, y)


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

# Scenario 1: non-numeric + numeric
result1 = swap("Apple", 10)
print("Returned:", result1)
# output:
#   Returned: -1

# Scenario 2: both numeric
result2 = swap(9, 17)
print("Returned:", result2)
# output:
#   17 9
#   Returned: None
