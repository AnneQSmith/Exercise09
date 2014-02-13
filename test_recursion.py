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
    



