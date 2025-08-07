import cmath
import math
import os


def soma(a:int,b:int)->int:
    if type(a) == str:
        if("." in a): a = float(a)
        else: a = int(a)
    if type(b) == str:
        if("." in b): b = float(b)
        else: b = int(b)

    a = round(a)
    b = round(b)

    return a + b

def produto(a:int, b:int)->float:
    if type(a) == str:
        if("." in a): a = float(a)
        else: a = int(a)
    if type(b) == str:
        if("." in b): b = float(b)
        else: b = int(b)

    return a * b
    
def equacao_parabolica(a ,b ,c):
    d = (b**2) - (4*a*c)
    x0 = (-b + cmath.sqrt(d)) / (2*a)
    x1 = (-b - cmath.sqrt(d)) / (2*a)

    return x0, x1

def calculate_average(numbers): 
    return sum(numbers) / len(numbers) 
 
def is_prime(n): 
    if n <= 1: 
        return False 
    for i in range(2, int(math.sqrt(n))): 
        if n % i == 0: 
            return False 
    return True 
 
def read_file_content(path): 
    with open(path, "r") as f: 
        return f.read() 
 
def count_word_occurrences(text, word): 
    return text.lower().split().count(word.lower()) 
 
def factorial(n): 
    if n == 0: 
        return 1 
    return n * factorial(n - 1) 
 
def reverse_string(s): 
    return s[::-1] 
 
def get_environment_variable(var_name): 
    return os.environ[var_name] 
 
def divide(a, b): 
    return a / b 
 
def flatten_list(nested_list): 
    return [item for sublist in nested_list for item in sublist]
 
def authenticate_user(username, password): 
    return username == "admin" and password == "1234"