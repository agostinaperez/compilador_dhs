# Generated from /home/agos/dhs/src/main/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#valor.
    def visitValor(self, ctx:compiladoresParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tipo.
    def visitTipo(self, ctx:compiladoresParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#operador.
    def visitOperador(self, ctx:compiladoresParser.OperadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lista_var.
    def visitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#definicion.
    def visitDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#oplo.
    def visitOplo(self, ctx:compiladoresParser.OploContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#logic_expr.
    def visitLogic_expr(self, ctx:compiladoresParser.Logic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#logic_termino.
    def visitLogic_termino(self, ctx:compiladoresParser.Logic_terminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#logic_term.
    def visitLogic_term(self, ctx:compiladoresParser.Logic_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#logic_factor.
    def visitLogic_factor(self, ctx:compiladoresParser.Logic_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#comp.
    def visitComp(self, ctx:compiladoresParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#opar.
    def visitOpar(self, ctx:compiladoresParser.OparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#exp.
    def visitExp(self, ctx:compiladoresParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#termino.
    def visitTermino(self, ctx:compiladoresParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#term.
    def visitTerm(self, ctx:compiladoresParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#proto_funcion.
    def visitProto_funcion(self, ctx:compiladoresParser.Proto_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#funcion.
    def visitFuncion(self, ctx:compiladoresParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#retornar.
    def visitRetornar(self, ctx:compiladoresParser.RetornarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#call_funcion.
    def visitCall_funcion(self, ctx:compiladoresParser.Call_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#args.
    def visitArgs(self, ctx:compiladoresParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lista_args.
    def visitLista_args(self, ctx:compiladoresParser.Lista_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#arg.
    def visitArg(self, ctx:compiladoresParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#send_args.
    def visitSend_args(self, ctx:compiladoresParser.Send_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lista_send_args.
    def visitLista_send_args(self, ctx:compiladoresParser.Lista_send_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#i_while.
    def visitI_while(self, ctx:compiladoresParser.I_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#i_if.
    def visitI_if(self, ctx:compiladoresParser.I_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#i_else.
    def visitI_else(self, ctx:compiladoresParser.I_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#i_for.
    def visitI_for(self, ctx:compiladoresParser.I_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#ternario.
    def visitTernario(self, ctx:compiladoresParser.TernarioContext):
        return self.visitChildren(ctx)



del compiladoresParser