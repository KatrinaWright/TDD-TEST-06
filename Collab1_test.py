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
    assert C1.function_1([1]) == 1    # Corrected, passing a list, not an int
