from myFunctions import soma, produto ,equacao_parabolica
# caminho feliz

# -------Adição-------
def test_soma_int():
    a = 2
    b = 3
    resultadoEsperado = 5
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_float():
    a = 0.5
    b = 0.25
    resultadoEsperado = 0
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_float_2():
    a = 0.8
    b = 0.76
    resultadoEsperado = 2
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_string():
    a = "1"
    b = "2"
    resultadoEsperado = 3
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_string_int():
    a = "1"
    b = 2
    resultadoEsperado = 3
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_int_string():
    a = 1
    b = "2"
    resultadoEsperado = 3
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_floatstring():
    a = "1.4"
    b = "2.75"
    resultadoEsperado = 4
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_floatstring_int():
    a = "1.4"
    b = 2
    resultadoEsperado = 3
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_floatstring_float():
    a = "1.4"
    b = 2.75
    resultadoEsperado = 4
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_int_floatstring():
    a = 1
    b = "2.75"
    resultadoEsperado = 4
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_float_floatstring():
    a = 1.4
    b = "2.75"
    resultadoEsperado = 4
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

# --------Produto(multiplicação)--------
def test_produto_int():
    a, b = 4, 7
    resultadoEsperado = 28
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_int_float():
    a, b = 5, 1.94
    resultadoEsperado = 9.70
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_int_string():
    a, b = 9, "11"
    resultadoEsperado = 99
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_string_int():
    a, b = "9", 6
    resultadoEsperado = 54
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_int_floatstring():
    a, b = 3, "12.99"
    resultadoEsperado = 38.97
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_floastring_int():
    a, b = "5.79", 4
    resultadoEsperado = 23.16
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_string_float():
    a, b = "3", 11.49
    resultadoEsperado = 34.47
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

# ----------------Equação quadratica ou do 2° Grau---------------- 

#def test_Equacao_P():
#    a, b, c = 3, -2, -8
#    resultadoEsperado = (complex(-4/3, 0),complex(2, 0))
#    resultado = equacao_parabolica(a ,b ,c)
#    assert resultado == resultadoEsperado

def test_equacao_parabolica_resultado_complexo():
    a, b, c = 1, 2, 5  # delta < 0 → raízes complexas
    resultado = equacao_parabolica(a, b, c)
    esperado = (
        complex(-1, 2),
        complex(-1, -2)
    )
    assert resultado == esperado

