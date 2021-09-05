import sys
import argparse

def rot13(mensagem):
    letras = 'abcdefghijklmnopqrstuvwxyz'

    string = ''

    #return mensagem

    for i in mensagem:
       if i in letras:
           if letras.index(i) < 13:
               string += letras[letras.index(i) + 13]
           else:
               string += letras[letras.index(i) - 13]
       elif i in letras.upper():
           if letras.upper().index(i) < 13:
               string += letras.upper()[letras.upper().index(i) + 13]
           else:
               string += letras.upper()[letras.upper().index(i) - 13]
       else:
             string += i

    return string

def main(args):
    print(rot13(args[1]))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))