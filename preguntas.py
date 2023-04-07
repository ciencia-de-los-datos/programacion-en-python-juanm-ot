"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
data= open("data.csv", "r").readlines()
data

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sum_second_column=0
    for lines in data:
        lines=lines.split('\t')
        sum_second_column= sum_second_column + int(lines[1])

    return sum_second_column
    


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    dictionary = {}  

    for letter in data:
        letter = letter.split('\t')
        letter = letter[0]
        if letter[0] in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    outcome = sorted(dictionary.items())

    return outcome 


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    dictionary = {} 

    for letter in data:
      letter = letter.split('\t')
      key = letter[0]
      count = int(letter[1])
      if key in dictionary:
        dictionary[key] += count
      else:
        dictionary[key] = count
     
    outcome = sorted(dictionary.items())

    return outcome


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    dictionary = {} 

    for line in data:
      line = line.split('\t')
      date = line[2].split('-')
      month = date[1]
      if month in dictionary:
        dictionary[month] += 1
      else:
        dictionary[month] = 1

    outcome = sorted(dictionary.items())

    return  outcome


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    dictionary= {}  

    for line in data:
        line=line.split('\t')
        letter=(line[0])
        num=int(line[1])
        if letter in dictionary:
          dictionary[letter].append(num)
        else:
          dictionary[letter]=[num]
    
    
    outcomes  = []
    for letter, lista in dictionary.items():
          tupla_outcome = (letter, max(lista), min(lista))
          outcomes.append(tupla_outcome)

    return sorted(outcomes)  


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    dictionary = {}

    for line in data:
      line = line.strip().split('\t')
      column_5 = line[4]
      tuplas = column_5.split(",")
      for tupla in tuplas:
          key, (value) = tupla.split(":")
          if key in dictionary:
            dictionary[key].append(int(value))
          else:
            dictionary[key]=[int(value)]

    outcomes = []
    for key, value in dictionary.items():
          tupla_outcome = (key, min(value), max(value))
          outcomes.append(tupla_outcome)


    return sorted(outcomes)


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    dictionary = {}

    for line in data:
      line = line.strip().split('\t')
      number = line[1]
      letter = line[0]
      if number in dictionary:
        dictionary[number].append(letter)
      else:
        dictionary[number] = [letter]

    outcomes = []
    for number,letters in dictionary.items():
        tupla_outcomes = (int(number),letters)
        outcomes.append(tupla_outcomes)

    return  sorted(outcomes)


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    dictionary = {}

    for line in data:
      line = line.strip().split('\t')
      number = line[1]
      letter = line[0]
      if number in dictionary:
        dictionary[number].append(letter)
      else:
        dictionary[number]=[letter]
    outcomes=[]
    for number,letters in dictionary.items():
        tupla_outcomes = (int(number),sorted(list(set(letters))))
        outcomes.append(tupla_outcomes)

    return sorted(outcomes)


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dictionary = {}

    for line in data:
      line = line.strip().split('\t')
      column_5 = line[4]
      tuplas = column_5.split(",")
      for tupla in tuplas:
          key, value = tupla.split(":")
          if key in dictionary:
            dictionary[key]+=1
          else:
            dictionary[key] = 1

    sorted_dictionary = sorted(dictionary.items())

    new_dictionary = {}

    for item in sorted_dictionary:
      new_dictionary[item[0]] = item[1]


    return new_dictionary


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    dictionary = {} 

    list = []
    for line in data:
      line=line.strip().split('\t')
      letter=line[0]
      column_4=len(line[3].split(","))
      column_5=len(line[4].split(","))
      dictionary[letter] = (column_4, column_5)
      list.append((letter, column_4, column_5))
    
    return list


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    dictionary = {}
    new_dictionary = {}

    for line in data:
      line = line.strip().split('\t')
      letter =line[3].split(",")
      num = int(line[1])
      dictionary = {element: num for element in letter}
      for element, value in dictionary.items():
        if element in new_dictionary:
          new_dictionary[element]+=value
        else:
          new_dictionary[element]=value
    ordered_dict_items = sorted(new_dictionary.items())

    ordered_dict = {}
    for item in ordered_dict_items:
      ordered_dict[item[0]] = item[1]
    ordered_dict = dict(ordered_dict)

    return ordered_dict



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    dictionary={}
    new_dictionary={}

    for line in data:
      line = line.strip().split('\t')
      key = line[0]
      tuplas = line[4].split(",")
      num_list = []
      for element in tuplas:
        num_list.append(int(element.split(":")[1]))
      if key in new_dictionary:
          dictionary[key].extend(num_list)
      else:
          dictionary[key]= num_list
      for key, num_list in dictionary.items():
        new_dictionary[key] = sum(num_list)

    ordered_dict_items = sorted(new_dictionary.items())

    ordered_dict = {}
    
    for item in ordered_dict_items:
      ordered_dict[item[0]] = item[1]
    ordered_dict = dict(ordered_dict)
    
    return ordered_dict
