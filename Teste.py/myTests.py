from myFunctions import soma, produto, equacao_parabolica, calculate_average, is_prime, read_file_content, count_word_occurrences, factorial, reverse_string, get_environment_variable, divide, flatten_list, authenticate_user
import pytest
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

#---------Calcular a media-----------

def test_threeint():
    numbers = 6, 8, 7
    esperado = 7
    resultado = calculate_average(numbers)
    assert esperado == resultado

def test_fourint():
    numbers = 4, 7, 9, 9
    esperado = 7.25
    resultado = calculate_average(numbers)
    assert esperado == resultado

def test_int_float_float():
    numbers = 6, 9.5, 8.5
    esperado = 8
    resultado = calculate_average(numbers)
    assert esperado == resultado

#--------Numero primo--------

def test_N_Primo():
    n = 5
    esperado = True
    resultado = is_prime(n)
    assert esperado == resultado

def test_N_Primo2():
    n = 9
    esperado = True
    resultado = is_prime(n)
    assert esperado == resultado

def test_N_Primo3():
    n = -4
    esperado = False
    resultado = is_prime(n)
    assert esperado == resultado

def test_N_Primo4():
    n = 0
    esperado = False
    resultado = is_prime(n)
    assert esperado == resultado

def test_N_Primo5():
    n = 27
    esperado = False
    resultado = is_prime(n)
    assert esperado == resultado

#------------Ler arquivo------------

def test_read_file(tmp_path):
    test_file = tmp_path / "teste.txt"
    esperado = "Boa tarde fulano."
    test_file.write_text(esperado,encoding="utf-8")
    resultado = read_file_content(test_file)
    assert esperado == resultado
    
#---------contagem de palavras---------

def test_count_word():
    text = "Bom dia, boa tarde ou boa noite"
    word = "boa"
    esperado = 2
    resultado = count_word_occurrences(text, word)
    assert esperado == resultado

#-------------Fatorial--------------

def test_factorial():
    n = 0
    esperado = 1
    resultado = factorial(n)
    assert esperado == resultado

def test_factorial2():
    n = 1
    esperado = 1
    resultado = factorial(n)
    assert esperado == resultado

#-----------string reversa------------

def test_string_reversa():
    s = "anotaram a data da maratona"
    esperado = "anotaram ad atad a maratona"
    resultado = reverse_string(s)
    assert esperado == resultado

#------------get_variable-------------

def test_get_environment_variable():
    var_name = ["Home"]
    esperado = "Home"
    resultado = get_environment_variable(var_name)
    assert esperado == resultado

#--------------divisão----------------

def test_divisao():
    a, b = 8, 4
    esperado = 2
    resultado = divide(a, b)
    assert esperado == resultado

def test_divisao2():
    a, b = 54, 8
    esperado = 6.75
    resultado = divide(a, b)
    assert esperado == resultado
#---------------flatten_list---------------

def test_flatten():
    nested_list = [[1,2], [3,4,5], [6, 7, 8, 9]]
    esperado = [1,2,3,4,5,6,7,8,9]
    resultado = flatten_list(nested_list)
    assert esperado == resultado

#----------Auteticação de usuario----------

def test_Autenticar():
    username, password = "admin", "1234"
    esperado = True
    resultado = authenticate_user(username, password)
    assert esperado == resultado