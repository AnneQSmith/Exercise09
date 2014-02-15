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
    assert out == 5
    n = 7
    out = recursion.fibonacci(n)
    assert out == 13
    n = 1
    out = recursion.fibonacci(n)
    assert out == 1
    n = 2
    out = recursion.fibonacci(n)
    assert out == 1

def test_find():
    l = ['a','b','c','d']
    i = 'e'
    out = recursion.find(l,i)
    assert out == None

    i = 'a'
    out = recursion.find(l,i)
    assert out == i

    i = 'd'
    out = recursion.find(l,i)
    assert out == i

def test_palindrome():
     str = 'evil'
     out = recursion.palindrome(str)
     assert out == False
     str = 'abccba'
     out = recursion.palindrome(str)
     assert out == True
     str = 'a'
     out = recursion.palindrome(str)
     assert out == True
     str = 'abcba'
     out = recursion.palindrome(str)
     assert out == True
     str = 'abcdefgfedcba'
     out = recursion.palindrome(str)
     assert out == True
     str = 'abcdcb'
     out = recursion.palindrome(str)
     assert out == False

def test_fold_paper():

    w = 10
    h = 5
    
    folds = 2
    out = recursion.fold_paper(w,h,folds)
    assert out == (5.0,2.5)

    folds = 1
    out = recursion.fold_paper(w,h,folds)
    assert out == (5.0,5.0)

    folds = 3
    out = recursion.fold_paper(w,h,folds)
    assert out == (2.5,2.5)
    
    folds = 4
    out = recursion.fold_paper(w,h,folds)
    assert out == (2.5,1.25)

    folds = 0
    out = recursion.fold_paper(w,h,folds)
    assert out == (w,h)

def test_count_up():
    target = 10
    n = 0
    recursion.count_up(target,n)


def test_hanoi():
    T1 = [5,4,3,2,1]
    T2 = []
    T3 = []
    recursion.hanoi(len(T1), T1, T2, T3)
    assert T2 == [5,4,3,2,1]
    assert T1 == []
    assert T3 == []
    










