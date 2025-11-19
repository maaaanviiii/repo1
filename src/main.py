Args:
    age: The value to validate.

Returns:
    The validated age as an int.

Raises:
    ValueError: If `age` is not an integer in the range 1..100.
"""
if not isinstance(age, int):
    raise ValueError("Age must be an integer between 1 and 100")
if age < 1 or age > 100:
    raise ValueError("Age must be an integer between 1 and 100")
return age
