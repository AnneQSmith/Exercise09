import recursion

def test_factorial():
    a = 5
    out = recursion.factorial(a)
    assert out == 120

def test_multiply_list():
    l = range(1,6)
    out = recursion.multiply_list(l)
    assert out == 120

def test_count_list():
    l = range(5)
    out = recursion.count_list(l)
    assert out == 5

def test_sum_list():
    l = range(5)
    out = recursion.sum_list(l)
    assert out == 10

def test_reverse():
    l = range(5)
    out = recursion.reverse(l)
    assert out == [4,3,2,1,0]

def test_fibonacci():
    n = 5
    out = recursion.fibonacci(n)
    assert out == 8
    n = 6
    out = recursion.fibonacci(n)
    assert out == 13


def test_find():
    l = ['a','b','c','d']
    i = 'e'
    out = recursion.find(l,i)
    assert out == None

    i = 'a'
    out = recursion.find(l,i)
    assert out == True

# def test_palindrome():
#     str = 'evil'
#     out = recursion.palindrome(str)
#     assert out == False
#     str = 'abccba'
#     out = recursion.palindrome(str)
#     assert out == True










