import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha
#usar ESTE
def main(argv):
    archivo = "input/programa.c"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    escucha = Escucha()
    parser.addParseListener(escucha)
    tree = parser.programa()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)
    
    
    #venir a esta caroeta y ejecutar
    #java -jar ~/dhs/antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor compiladores.g4 -o .
    #después me paro acá y ejecuto desde el depurador el python
    
    #EN EL LISTENER, SALIR DE UN NODO ES SALIR POR ARRIBA