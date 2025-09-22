# Generated from /home/agos/dhs/src/main/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#valor.
    def enterValor(self, ctx:compiladoresParser.ValorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#valor.
    def exitValor(self, ctx:compiladoresParser.ValorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#tipo.
    def enterTipo(self, ctx:compiladoresParser.TipoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tipo.
    def exitTipo(self, ctx:compiladoresParser.TipoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#operador.
    def enterOperador(self, ctx:compiladoresParser.OperadorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#operador.
    def exitOperador(self, ctx:compiladoresParser.OperadorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lista_var.
    def enterLista_var(self, ctx:compiladoresParser.Lista_varContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lista_var.
    def exitLista_var(self, ctx:compiladoresParser.Lista_varContext):
        pass


    # Enter a parse tree produced by compiladoresParser#definicion.
    def enterDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#definicion.
    def exitDefinicion(self, ctx:compiladoresParser.DefinicionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#oplo.
    def enterOplo(self, ctx:compiladoresParser.OploContext):
        pass

    # Exit a parse tree produced by compiladoresParser#oplo.
    def exitOplo(self, ctx:compiladoresParser.OploContext):
        pass


    # Enter a parse tree produced by compiladoresParser#logic_expr.
    def enterLogic_expr(self, ctx:compiladoresParser.Logic_exprContext):
        pass

    # Exit a parse tree produced by compiladoresParser#logic_expr.
    def exitLogic_expr(self, ctx:compiladoresParser.Logic_exprContext):
        pass


    # Enter a parse tree produced by compiladoresParser#logic_termino.
    def enterLogic_termino(self, ctx:compiladoresParser.Logic_terminoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#logic_termino.
    def exitLogic_termino(self, ctx:compiladoresParser.Logic_terminoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#logic_term.
    def enterLogic_term(self, ctx:compiladoresParser.Logic_termContext):
        pass

    # Exit a parse tree produced by compiladoresParser#logic_term.
    def exitLogic_term(self, ctx:compiladoresParser.Logic_termContext):
        pass


    # Enter a parse tree produced by compiladoresParser#logic_factor.
    def enterLogic_factor(self, ctx:compiladoresParser.Logic_factorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#logic_factor.
    def exitLogic_factor(self, ctx:compiladoresParser.Logic_factorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#comp.
    def enterComp(self, ctx:compiladoresParser.CompContext):
        pass

    # Exit a parse tree produced by compiladoresParser#comp.
    def exitComp(self, ctx:compiladoresParser.CompContext):
        pass


    # Enter a parse tree produced by compiladoresParser#opar.
    def enterOpar(self, ctx:compiladoresParser.OparContext):
        pass

    # Exit a parse tree produced by compiladoresParser#opar.
    def exitOpar(self, ctx:compiladoresParser.OparContext):
        pass


    # Enter a parse tree produced by compiladoresParser#exp.
    def enterExp(self, ctx:compiladoresParser.ExpContext):
        pass

    # Exit a parse tree produced by compiladoresParser#exp.
    def exitExp(self, ctx:compiladoresParser.ExpContext):
        pass


    # Enter a parse tree produced by compiladoresParser#termino.
    def enterTermino(self, ctx:compiladoresParser.TerminoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#termino.
    def exitTermino(self, ctx:compiladoresParser.TerminoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#term.
    def enterTerm(self, ctx:compiladoresParser.TermContext):
        pass

    # Exit a parse tree produced by compiladoresParser#term.
    def exitTerm(self, ctx:compiladoresParser.TermContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#proto_funcion.
    def enterProto_funcion(self, ctx:compiladoresParser.Proto_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#proto_funcion.
    def exitProto_funcion(self, ctx:compiladoresParser.Proto_funcionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#funcion.
    def enterFuncion(self, ctx:compiladoresParser.FuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#funcion.
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#retornar.
    def enterRetornar(self, ctx:compiladoresParser.RetornarContext):
        pass

    # Exit a parse tree produced by compiladoresParser#retornar.
    def exitRetornar(self, ctx:compiladoresParser.RetornarContext):
        pass


    # Enter a parse tree produced by compiladoresParser#call_funcion.
    def enterCall_funcion(self, ctx:compiladoresParser.Call_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#call_funcion.
    def exitCall_funcion(self, ctx:compiladoresParser.Call_funcionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#args.
    def enterArgs(self, ctx:compiladoresParser.ArgsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#args.
    def exitArgs(self, ctx:compiladoresParser.ArgsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lista_args.
    def enterLista_args(self, ctx:compiladoresParser.Lista_argsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lista_args.
    def exitLista_args(self, ctx:compiladoresParser.Lista_argsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#arg.
    def enterArg(self, ctx:compiladoresParser.ArgContext):
        pass

    # Exit a parse tree produced by compiladoresParser#arg.
    def exitArg(self, ctx:compiladoresParser.ArgContext):
        pass


    # Enter a parse tree produced by compiladoresParser#send_args.
    def enterSend_args(self, ctx:compiladoresParser.Send_argsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#send_args.
    def exitSend_args(self, ctx:compiladoresParser.Send_argsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lista_send_args.
    def enterLista_send_args(self, ctx:compiladoresParser.Lista_send_argsContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lista_send_args.
    def exitLista_send_args(self, ctx:compiladoresParser.Lista_send_argsContext):
        pass


    # Enter a parse tree produced by compiladoresParser#i_while.
    def enterI_while(self, ctx:compiladoresParser.I_whileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#i_while.
    def exitI_while(self, ctx:compiladoresParser.I_whileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#i_if.
    def enterI_if(self, ctx:compiladoresParser.I_ifContext):
        pass

    # Exit a parse tree produced by compiladoresParser#i_if.
    def exitI_if(self, ctx:compiladoresParser.I_ifContext):
        pass


    # Enter a parse tree produced by compiladoresParser#i_else.
    def enterI_else(self, ctx:compiladoresParser.I_elseContext):
        pass

    # Exit a parse tree produced by compiladoresParser#i_else.
    def exitI_else(self, ctx:compiladoresParser.I_elseContext):
        pass


    # Enter a parse tree produced by compiladoresParser#i_for.
    def enterI_for(self, ctx:compiladoresParser.I_forContext):
        pass

    # Exit a parse tree produced by compiladoresParser#i_for.
    def exitI_for(self, ctx:compiladoresParser.I_forContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ternario.
    def enterTernario(self, ctx:compiladoresParser.TernarioContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ternario.
    def exitTernario(self, ctx:compiladoresParser.TernarioContext):
        pass



del compiladoresParser