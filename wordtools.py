from unit_tester import test
import string

#prob 8 of chapter 12

def cleanword(palabra):
    newWord = ''
    for i in palabra:
        if i not in string.punctuation:
            newWord += i
    return newWord

def has_dashdash(palabra):
    if palabra.find('--') == -1:
        return False
    else:
        return True

def extract_words(palabra):
    newWord = ''
    if palabra.find('--') >= 0:
        ubica = palabra.find('--')
        newWord = palabra[:ubica] + ' ' + palabra[ubica:]
    else:
        newWord = palabra
        
    newWord = cleanword(newWord)
    newWord = newWord.lower().split()
    return newWord

def wordcount(palabra, lista):
    count = 0
    for i in lista:
        if i == palabra:
            count += 1
    return count

def wordset(lista):
    nuevoLista = []
    for i in sorted(lista):
        if i not in nuevoLista:
            nuevoLista.append(i)
    return nuevoLista

def longestword(lista):
    grande = 0
    for i in lista:
        if len(i) > grande:
            grande = len(i)
    return grande


