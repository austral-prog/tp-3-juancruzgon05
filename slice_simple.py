def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.
    texto= "Awesome"
    print(texto.lower()[0:3])
    print(texto.lower()[2:5])
    print(texto.lower()[0:4]+ texto.lower()[-3:])


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
