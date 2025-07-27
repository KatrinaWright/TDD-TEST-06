import Collab1 as C1;

# Example Passing Test
def test_hello_pass():
    assert C1.hello_world() == "Hello!"

# Example Failed Test
# Uncomment, run once & then comment out again
#def test_hello_fail():
#    assert C1.hello_world() == "Hello World!"

#########################
#  HW Assignment Tests  #
#########################

# Problem 1 Tests
def test_function_one():
    assert C1.function_1( 1 ) == 1

def test_function_nine():
    assert C1.function_1( 9 ) == 45

def test_function_neg():
    assert C1.function_1( -2 ) == None

def test_function_two():
    assert C1.function_1( 2 ) == 3

def test_function_str():
    assert C1.function_1( "six" ) == None

# Problem 2 Tests
def test_new_one():
    assert C1.function_2( [1] ) == 1

