def rectangle(length, width):
    # Check if both length and width are integers
    if not (isinstance(length, int) and isinstance(width, int)):
        return "Enter valid values!"

    # Inner function to calculate area
    def area():
        return length * width

    # Inner function to calculate perimeter
    def perimeter():
        return 2 * (length + width)

    # Return the result string
    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

# Test Code
print(rectangle('2', 10))