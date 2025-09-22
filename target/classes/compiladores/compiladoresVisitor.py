# Generated from /home/agos/dhs/src/main/java/compiladores/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

package compiladores;


# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#s.
    def visitS(self, ctx:compiladoresParser.SContext):
        return self.visitChildren(ctx)



del compiladoresParser