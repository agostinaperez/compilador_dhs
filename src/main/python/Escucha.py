from copy import copy
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from semantica.TablaSimbolos import TablaSimbolos
from semantica.Id import Variable, Funcion
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
                #pedirlke a la tabla de simbolos el objeto con este id y de ahí saco el tió de dato independientemente dek contexto
                if self.tabla.buscar(var) != var.tdato:
                    print('Error: la variable ' + var +
                          ' no es del tipo esperado')
                    return
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
            
            
     # def exitLista_var(self, ctx: compiladoresParser.Lista_varContext):
    #     if ctx.getChildCount() != 0:
    #         if self.tabla.buscarLocal(ctx.getChild(1).getText()) == False:
    #             # como el Listener recorre el arbol de abajo hacia arriba, obtengo el tipo
    #             # de dato subiendo el contexto hacia la declaracion
    #             if len(self.listTdato) == 0:
    #                 auxCtx = ctx
    #                 while (auxCtx.parentCtx.getChild(0).getText() == ','):
    #                     auxCtx = auxCtx.parentCtx
    #                 self.listTdato.append(
    #                     auxCtx.parentCtx.getChild(0).getText())

    #             tdato = self.listTdato.pop()
    #             self.listTdato.append(tdato)
    #             name = str(ctx.getChild(1).getText())
    #             nuevaVar = Variable(name, tdato)
    #             # again, si hay un child(2) es pq la variable se inicializo
    #             if (str(ctx.getChild(2).getText()) != ''):
    #                 nuevaVar.setInicializado()
    #         else:
    #             print("Variable " + ctx.getChild(1).getText() +
    #                   " existente en el contexto")
    #             return
    #         self.tabla.agregar(nuevaVar)
    #         print('Nuevo simbolo: ' + nuevaVar.nombre + ' agregado')

    #         self.listTdato.pop()

    #     return
    
     # def exitCall_funcion(self, ctx: compiladoresParser.Call_funcionContext):
    #     contexto = self.tabla.buscar(ctx.getChild(0).getText()) #busco la funcion en la tabla de simbolos tipo q la haya definido!

    #     if contexto == False:
    #         print('FUNCION INEXISTENTE')
    #         return

    #     newFuncion = Funcion('', '', []) #sin nombre ni tipo de dato ni argumentos
    #     for var in contexto.getSimbolos().values():
    #         if var.nombre == ctx.getChild(0).getText():
    #             newFuncion = var
    #             break

    #     self.exitSend_args(ctx.getChild(2))

    #     if len(newFuncion.args) != len(self.listArgs):
    #         print('Faltan parametros en la llamada de funcion')
    #         return

    #     for var1, var2 in zip(newFuncion.args, self.listArgs):
    #         if var1.tdato != var2.tdato:
    #             print('Error: el parametro ' + var2 +
    #                   ' no es del tipo esperado')
    #             return
    
    
     # def exitFuncion(self, ctx: compiladoresParser.FuncionContext):
    #     self.listArgs.clear()

    #     tdato = ctx.getChild(0).getText()
    #     nombre = ctx.getChild(1).getText()
    #     self.exitArgs(ctx.getChild(3))
    #     listaArgs = copy.deepcopy(self.listArgs)
    #     funcionVar = Funcion(nombre, tdato, listaArgs)
    #     funcionVar.setAccedido()

    #     contexto = self.tabla.buscar(nombre)

    #     # Si no existio prototipo de la funcion, se agrega a la tabla de simbolos
    #     if contexto == False:
    #         self.tabla.agregar(funcionVar)
    #         print('Nuevo simbolo ' + funcionVar.nombre + ' agregado')
    #         return

    #     # Si existe prototipo, verifico que la implementacion se corresponda
    #     for var in contexto.getSimbolos().values():
    #         if var.nombre == funcionVar.nombre:
    #             if var.tdato == funcionVar.tdato:
    #                 for arg1, arg2 in zip(var.args, funcionVar.args):
    #                     # En caso que el prototipo tenga nombre en el argumento
    #                     if arg1.nombre != '':
    #                         if arg1.nombre == arg2.nombre:
    #                             if arg1.tdato == arg2.tdato:
    #                                 pass
    #                             else:
    #                                 print(
    #                                     'LA IMPLEMENTACION DE ' + funcionVar.nombre + ' NO SE CORRESPONDE CON EL PROTOTIPO')
    #                                 return
    #                         else:
    #                             print(
    #                                 'LA IMPLEMENTACION DE ' + funcionVar.nombre + ' NO SE CORRESPONDE CON EL PROTOTIPO')
    #                             return
    #                 print('La implementacion de ' + funcionVar.nombre +
    #                       ' se corresponde con su prototipo')
    #                 return

    #     print(
    #         'LA IMPLEMENTACION DE ' + funcionVar.nombre + ' NO SE CORRESPONDE CON EL PROTOTIPO')
    #     return

#para cuando llamo a una funcion y le paso parametros
    # def exitSend_args(self, ctx: compiladoresParser.Send_argsContext):
    #     self.listArgs.clear()
    #     if ctx.getChildCount() == 0:
    #         return

    #     nombre = str()
    #     if ctx.getChild(0).getChild(0).getChild(0).getChildCount == 2:
    #         nombre = ctx.getChild(0).getChild(
    #             0).getChild(0).getChild(1).getText()
    #     elif ctx.getChild(0).getChild(0).getChild(0).getChild(0).getChildCount() == 0:
    #         nombre = ctx.getChild(0).getChild(
    #             0).getChild(0).getChild(0).getText()

    #     contexto = self.tabla.buscar(nombre)

    #     if contexto == False:
    #         print('PARAMETRO ' + nombre + ' NO DEFINIDO')
    #         return

    #     for var in contexto.getSimbolos().values():
    #         if var.nombre == nombre:
    #             self.listArgs.append(var)

    #     self.exitLista_send_args(ctx.getChild(1))

    #     return

    # def exitLista_send_args(self, ctx: compiladoresParser.Lista_send_argsContext):
    #     if ctx.getChildCount() == 0:
    #         return

    #     nombre = str()
    #     if ctx.getChild(1).getChild(0).getChild(0).getChildCount == 2:
    #         nombre = ctx.getChild(1).getChild(
    #             0).getChild(0).getChild(1).getText()
    #     elif ctx.getChild(1).getChild(0).getChild(0).getChild(0).getChildCount() == 0:
    #         nombre = ctx.getChild(1).getChild(
    #             0).getChild(0).getChild(0).getText()

    #     contexto = self.tabla.buscar(nombre)

    #     if contexto == False:
    #         print('PARAMETRO ' + nombre + ' NO DEFINIDO')
    #         return

    #     for var in contexto.getSimbolos().values():
    #         if var.nombre == nombre:
    #             self.listArgs.append(var)
    #             break

    #     if ctx.getChild(2).getChildCount() != 0:
    #         self.exitLista_send_args(ctx.getChild(1))

    #     return