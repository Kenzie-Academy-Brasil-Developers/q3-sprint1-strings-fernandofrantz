# Código do dev aqui

from typing import final


def standardize_names(name):
    final = ''
    counter = 0
    splited_name = name.split()
    for space in splited_name:
        if counter < (len(splited_name) -1):
            final = final + space + '-'
        else:
            final = final + space
        counter += 1
    print(final)
    return final

def standardize_title(title):
    final = ''
    splited  = title.split(' ')
    counter = 0
    for word in splited:
        if counter < (len(splited) -1):
            final += word.capitalize() + ' '
        else:
            final += word.capitalize()
    print(final)
    return final


text = """
a famosa atriz Constance Rattigan recebe uma encomenda
desagradável: uma lista com números de telefone de
pessoas que morreram recentemente. é uma coisa assustadora,
considerando que os nomes das poucas pessoas vivas presentes
na lista estão assinalados em vermelho com uma cruz. O da
própria Constance é um deles.
"""
def standardize_text(text):
    final = ''
    split = text.split('.')
    for phrase in split:
        formated = (phrase[1:])
        final += formated.capitalize() + '. '

    print(final)
    return final


text = "pense num deserto"
def title_creator(text):
    phrase = standardize_title(text)
    print('-' * 20 + phrase + '-' * 20)
    return('-' * 20 + phrase + '-' * 20)



text_of_blog_a = """
na Londres do pós-guerra, a escritora     Juliet tenta encontrar
uma   trama para seu novo livro. ela recebe ajuda por meio de uma
   carta de um      desconhecido, um nativo da ilha de Guernsey,
em cujas mãos havia chegado um livro    que há tempos tinha
pertencido    a Juliet.
"""

text_of_blog_b = """
O romance "Cinco Quartos de Laranja" é como   um vinho intenso e
delicado.    usando metáforas culinárias, personagens peculiares
 e acontecimentos sobrenaturais,      Harris cria uma história
complexa e      bela ao mesmo tempo.
"""

def text_merge(text_of_blog_a, text_of_blog_b):
    text_a = ''
    text_b = ''
    counter_a = 0
    counter_b = 0
    splited_a = text_of_blog_a.split()
    splited_b = text_of_blog_b.split()
    for space in splited_a:
        if counter_a < (len(splited_a) -1):
            text_a = text_a + space + ' '
        else:
            text_a = text_a + space
        counter_a += 1
    for space in splited_b:
        if counter_b < (len(splited_b) -1):
            text_b = text_b + space + ' '
        else:
            text_b = text_b + space
        counter_a += 1

    formated_a = standardize_text(text_a)
    formated_b = standardize_text(text_b)

    final = formated_a + formated_b

    print(final)
    return final

text_merge(text_of_blog_a, text_of_blog_b)