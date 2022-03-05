def test_incr(asmt):
    assert asmt.incr(3) == 4

def test_square(asmt):
    assert asmt.square(3) == 9

def test_incorrect_code(asmt):
    assert asmt.incorrect_code() == True

def test_non_existant_func(asmt):
    assert asmt.some_func() == True

def test_missing_arg(asmt):
    assert asmt.incr() == 0
