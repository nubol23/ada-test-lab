from solution import precios, triangulo


def test_zero_price():
    for age in range(3):
        assert precios(age) == 0


def test_price_five():
    for age in range(4, 19):
        assert precios(age) == 5


def test_adult_price():
    for age in range(19, 30):
        assert precios(age) == 10


def test_triangle_two():
    expected = "*\n**"
    result = triangulo(2)
    
    assert (
        result == expected or
        result == expected+"\n"
    )


def test_triangle_five():
    expected = "*\n**\n***\n****\n*****"
    result = triangulo(5)
    
    assert (
        result == expected or
        result == expected+"\n"
    )
