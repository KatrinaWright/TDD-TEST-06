# NAME:         FIXME

# Example
def hello_world():
    return "Hello!"

def function_1(data):
    if type(data) != int:
        return None
    elif data < 1:
        return None
    elif data == 1:
        return 1
    sum = 0
    for i in range(1, data+1):
        sum += i
    return sum

def function_new_one():
    assert C1.function_2( [1] ) == 1

def main():
    print("Function 1: ", function_1(1))

main()
