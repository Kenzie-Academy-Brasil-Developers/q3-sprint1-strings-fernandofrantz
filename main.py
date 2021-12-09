# Código do dev aqui

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
        counter += 1
    return final

def standardize_text(text):
    final = ''
    splited  = text.split(' ')
    counter = 0
    for word in splited:
        if counter == 0:
            final += word.capitalize() + ' '
        elif counter <= len(splited)-2:
            final += word + ' '
        else:
            final += word
        counter += 1
    return final

def title_creator(text):
    phrase = standardize_title(text)
    return('-' * 20 + phrase + '-' * 20)






def text_merge(text_of_blog_a, text_of_blog_b):
    text_a = ''
    text_b = ''
    counter_a = 0
    counter_b = 0
    splited_a = text_of_blog_a.split()
    splited_b = text_of_blog_b.split()
    phrases_a = text_of_blog_a.split('.')
    phrases_b = text_of_blog_a.split('.')

    for phrase in phrases_a:
        dots =  phrase.split('.')
        print(dots)
        for frase in dots:
            print(standardize_text(frase))
            print('-' *30)

    final = ''
    for word in splited_a:
        if counter_a == 0:
            final += word.capitalize() + ' '
        elif counter_a < len(splited_a)-1:
            final += word + ' '
        counter_a += 1
    
    
    return final

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

merged_text = text_merge(text_of_blog_a, text_of_blog_b)
print(merged_text)
