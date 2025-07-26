# NAME:         FIXME

# Example
def hello_world():
    return "Hello!"

def function_1(data):
    
    """
    Write a function ```squared_sum``` that takes an array of numbers as a parameter and returns the sum of each number in the array squared:

| **Example call** | **Returns** |
| -------------- | --------- |
| `squared_sum ([])` | `0` |
| `squared_sum ([5, -2, 3])` | `38` |
| `squared_sum ([-3, 4])` | `25` |
| `squared_sum ([7, -1, 15, 0])` | `275` |

_**Hint**: use the accumulator / aggregator pattern of a variable & for loop over a range_
    """
    
    total = 0
    for num in data:
        total += num ** 2
    return total


def main():
    print("Function 1: ", function_1([1]))   # Corrected, passing a list not an int

main()
