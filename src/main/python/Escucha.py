from copy import copy
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from semantica.TablaSimbolos import TablaSimbolos
from semantica.Id import Id, Variable, Funcion


class Escucha(compiladoresListener):
    tabla = TablaSimbolos()
    listTdato = []
    listArgs = []

    def enterPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Comenzando la compilacion".center(40, "*") + '\n')

    def exitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print('\n' + "Fin de la compilacion".center(40, "*"))
        self.tabla.borrarContexto()

    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        self.tabla.agregarContexto()

    def exitBloque(self, ctx: compiladoresParser.BloqueContext):
        self.tabla.borrarContexto()

    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        #me fijo en la tabla de simbolos si ya existe la variable en el contexto actual, si no existe la agrego
        if self.tabla.buscarLocal(ctx.getChild(1).getText()) == False:
            tdato = str(ctx.getChild(0).getText())
            # si hay mas de una variable en la declaracion, guardo el tipo de dato en una lista
            self.listTdato.append(tdato)
            name = str(ctx.getChild(1).getText()) #saco tamb el nombre de la variable y desp la creo
            nuevaVar = Variable(name, tdato)
            # el child(2) es el del "= valor" o sea q si existe es pq la variable se inicializo y pongo inicializado en true
            if (str(ctx.getChild(2).getText()) != ''):
                nuevaVar.setInicializado()
        else:
            print("Variable " + ctx.getChild(1).getText() +
                  " existente en el contexto")
            return
        self.tabla.agregar(nuevaVar)
        print('Nuevo simbolo: ' + nuevaVar.nombre + ' agregado')

        self.listTdato.pop() #borro el tipo de dato de la lista pq ya la agregue a la tabla

        return

    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        #busco que la variable exista en algun contexto
        contexto = self.tabla.buscar(ctx.getChild(0).getText())
        if contexto == None:
            print('LA VARIABLE NO ESTA DEFINIDA, NO SE REALIZO LA ASIGNACION')
            return
        for var in contexto.getSimbolos(): #recorro las variables del contexto actual y busco la q estoy asignando
            if var == ctx.getChild(0).getText():
                varActualizada = Variable( #vuelvo a guardar la variable con el mismo nombre y tipo de dato pero inicializada en true
                    contexto.getSimbolos()[var].nombre, contexto.getSimbolos()[var].tdato, True)
                self.tabla.actualizar(varActualizada)
                print('Variable ' + varActualizada.nombre + ' actualizada')
            

    def exitProto_funcion(self, ctx: compiladoresParser.Proto_funcionContext):
        self.listArgs.clear()
        #mientas no exista la funcion en el contexto actual, la agrego
        if self.tabla.buscar(ctx.getChild(1).getText()) == False:
            tdato = ctx.getChild(0).getText()
            nombre = ctx.getChild(1).getText()
            #paso los argumentos a la lista de argumentos. Acá actualizo la lista listArgs y después la copio en listaArgs
            self.exitArgs(ctx.getChild(3))
            listaArgs = copy.deepcopy(self.listArgs)
            nuevaFuncion = Funcion(nombre, tdato, listaArgs)
            self.tabla.agregar(nuevaFuncion)
            print('Nuevo simbolo ' + nuevaFuncion.nombre + ' agregado')
        else:
            print('SIMBOLO YA DEFINIDO')

   
    def exitArgs(self, ctx: compiladoresParser.ArgsContext):
        #es una funcion para recorrer los argumentos de la funcion y guardarlos en la lista listArgs
        # si no hay argumentos, salgo
        if ctx.getChildCount() != 0:
            nombre = ctx.getChild(1).getText()
            tdato = ctx.getChild(0).getText()
            nuevoArg = Variable(nombre, tdato)
            self.listArgs.append(nuevoArg)
            self.exitLista_args(ctx.getChild(2))

    def exitLista_args(self, ctx: compiladoresParser.Lista_argsContext):
        #funcion recursiva para recorrer la lista de argumentos, si no hay más argumentos vuelve para arriba a exitArgs
        if ctx.getChildCount() != 0:
            nombre = ctx.getChild(2).getText()
            tdato = ctx.getChild(1).getText()
            nuevoArg = Variable(nombre, tdato)
            self.listArgs.append(nuevoArg)
            self.exitLista_args(ctx.getChild(3))