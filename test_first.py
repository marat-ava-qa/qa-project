def is_adult(age):
    return age >= 18

def test_is_adult():
    assert is_adult(25) 
    
def test_minor():
    assert not is_adult(10)
    
def test_boundary():
    assert is_adult(18)