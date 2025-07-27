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

def function_2(data):
    if data == 1:
        return 1
    return sum([i for i in data])
    

def main():
    print("Function 1: ", function_1(1))

main()
