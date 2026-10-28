my_int = 42
my_float = 3.14
my_string = "hello"
my_bool = True
my_none = None

# Step 2: value and type, one line per variable
print(my_int, type(my_int))
print(my_float, type(my_float))
print(my_string, type(my_string))
print(my_bool, type(my_bool))
print(my_none, type(my_none))

# 7 / 2     -> float  (/ always returns a float, even 6 / 2 gives 3.0)
# 7 // 2    -> int    (floor division of two ints gives an int)
# "7" * 2   -> str    (string repetition: "77")
# 3 > 2     -> bool   (comparisons return True or False)
print(type(7 / 2))
print(type(7 // 2))
print(type("7" * 2))
print(type(3 > 2))