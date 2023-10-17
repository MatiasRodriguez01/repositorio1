import pytest
# import funciones_clase12
from funciones_clase12 import *

# EJERCICIO 1:
@pytest.mark.parametrize("dni, boo",[
    ("45360660", True),
    ("4536066", True),
    ("453606", False),
    ("343565654", False),
    ("34343543543", False),
    ("34424324", True),
    ("21312", False)
])


def test_quality_document(dni, boo):
    assert quality_document(dni) == boo

# EJERCICIO 2:

@pytest.mark.parametrize("work, number", [
    ("matias rodriguez", 9),
    ("jose de la cuna del norte", 5),
    ("Metallica", None),
    ("tecnicatura de programacion ", 0) 
])

def test_quality_letter(work, number):
    assert quality_letter(work) == number


# EJERCICIO 4:

@pytest.mark.parametrize("numero1, numero2, boolean", [
    (4, 2, True),
    (23, 2, False),
    (345, 15, True),
    (7634, 26, False)
])

def test_multiplos(numero1, numero2, boolean):
    assert multiplos(numero1, numero2) == boolean


# EJERCICIO 5:

@pytest.mark.parametrize("temMax, temMin, resultado",[
    (12, 32, 22.0),
    (12.7, 32.1, 22.4),
    (29.9, 35.2, 32.5),
    (23.8, 29.31, 26.6)
])

def test_temp_mediun(temMax, temMin, resultado):
    assert temp_mediun(temMax, temMin) == resultado

# EJERCICIO 6:

@pytest.mark.parametrize("nombre, espacios", [
    ("hola", "h o l a "),
    ("muestra el codigo", "m u e s t r a   e l   c o d i g o "),
    ("suerte en el parcial", "s u e r t e   e n   e l   p a r c i a l "),
    ("codigo,python", "c o d i g o , p y t h o n ")
])

def test_espace_word(nombre, espacios):
    assert espace_word(nombre) == espacios

# EJERCICIO 7:

@pytest.mark.parametrize("lista, menor, mayor",[
    ([6, 3, 2, 7, 9], 2, 9),
    ([12, 32, 54, 76, 12], 12, 76),
    ([12331, 3212, 5234, 7676, 9812], 3212, 12331),
    ([1212, 3122, 54323, 2336, 3213], 1212, 54323),
    ([112, 322, 543, 231, 212], 112, 543)
])

def test_element_min_and_max(lista, menor, mayor):
    assert element_max_and_min(lista) == (menor, mayor)


# EJERCICIO 9: 

@pytest.mark.parametrize("usuario, contrasenia, valor",[
    ("usuario1", "asdasd", True),
    ("usuario1", "ASDASD", False),
    ("wewer", "fefere", False),
    ("matute", "12349", False),
    ("usuario2", "asdfg", False)
])

def test_login(usuario, contrasenia, valor):
    assert login(usuario, contrasenia) == valor

# EJERCICIO 14:

@pytest.mark.parametrize("numero, valor",[
    (1, False),
    (2, True), 
    (3, True), 
    (12, False),
    (30, False),
    (31, True),
    (76, False)
])

def test_primo(numero, valor):
    assert primo(numero) == valor

 
