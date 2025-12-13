import pytest


@pytest.mark.smoke
def test_fucntion_one():
    print("Hello world")
    a = 5
    b = 6
    assert a < b
    print("Inside 1")

@pytest.mark.regression
def test_fucntion_two():
    print("Hi there")
    print("Inside 2")

@pytest.mark.smoke
def test_fucntion_three():
    print("Bye world")
    a = 7
    b = 6
    assert a > b
    print("Inside 3")


@pytest.mark.parametrize("username,password",[("aarun","123"),("varun","456"),("tarun","789"),("sarun","101")])
def test_fucntion_four(username,password):
    print(username+"-"+password)


    