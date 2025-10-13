from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from semantica.TablaSimbolos import TablaSimbolos
from semantica.Id import Variable, Funcion
import copy
class Escucha(compiladoresListener):
    tabla = TablaSimbolos()
    listTdato = []
    listArgs = []
    isFuncion = 0
    indent = 1

    def enterPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Comenzando la compilacion".center(40, "*") + '\n')

    def exitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print('\n' + "Fin de la compilacion".center(40, "*"))
        self.tabla.borrarContexto()

    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        self.tabla.agregarContexto()

        # Si el bloque pertenece a una función, agrego los parámetros
        # Si el bloque pertenece a una función (int/double ...)
        padre = ctx.parentCtx
        if padre and padre.getChildCount() >= 4:
            tipo = padre.getChild(0).getText()
            if tipo in ('int', 'double'):
                # Procesar argumentos de la función
                self.exitArgs(padre.getChild(3))
                listaArgs = copy.deepcopy(self.listArgs)
                for var in listaArgs:
                    self.tabla.agregar(var)
                print(" "*self.indent + "<<< Entrando a un bloque de funcion >>>")
                self.indent+=2
            else:
                print(" "*self.indent+"<<< Entrando a un " + tipo + " >>>")
                self.indent+=2

#        self.tabla.imprimirContextos()

    def exitBloque(self, ctx: compiladoresParser.BloqueContext):
        padre = ctx.parentCtx
        if padre:
            tipo = padre.getChild(0).getText()
            if padre.getChildCount() >= 4:
                if tipo in ('int', 'double'):
                    self.indent-=2
                    # No borrar aún el contexto de función — lo hace el parser al salir de la función
                    print(" "*self.indent+"<<< Saliendo de bloque de función (no borro contexto todavía) >>>")
#                   self.tabla.imprimirContextos()
                    return
                if tipo in ('for', 'if', 'while'):
                    self.indent-=2
                    # Si no es una función (if, for, etc.), borro el contexto
                    print(" "*self.indent+"<<< Saliendo de bloque " + tipo + " >>>")
                    
            else:
                self.indent-=2
                print(" "*self.indent+"<<< Saliendo de bloque interno >>>")            
#        self.tabla.imprimirContextos()
        self.tabla.borrarContexto()

    def exitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        #me fijo en la tabla de simbolos si ya existe la variable en el contexto actual, si no existe la agrego
        if self.tabla.buscarLocal(ctx.getChild(1).getText()) == False:
            tdato = str(ctx.getChild(0).getText())
            # si hay mas de una variable en la declaracion, guardo el tipo de dato en una lista
            self.listTdato.append(tdato)
            name = str(ctx.getChild(1).getText()) #saco tamb el nombre de la variable y desp la creo
            nuevaVar = Variable(name, tdato)
            # esto es un re quilombo pero basicamente quiero distinguir si es una asignacion comun o un llamado a funcion
            #o sea distinguir entre "int a = 5;" y "int a = funcion(1,2);". Pq call_function tiene 4 hijos exactos entonces intento llegar al factor
            #pq factor puede ser, entre otras cosas, un call_function o un valor. Si es un call_function tiene 4 hijos, si es un valor no
            #declaracion-> get definicion -> get oplo -> get logic_termino -> get logic_factor -> get opar -> get termino -> get factor -> get call_function
            is_call_funcion = False
            child = ctx
            try:
                # Navego de forma segura hasta el posible call_function
                child = ctx.getChild(2)
                for _ in range(10):
                    if child is not None and hasattr(child, 'getChild') and child.getChildCount() > 0:
                        child = child.getChild(0)
                    else:
                        break
                if child is not None and hasattr(child, 'getChildCount') and child.getChildCount() == 4:
                    is_call_funcion = True
            except Exception:
                is_call_funcion = False
            if not is_call_funcion:
            # el child(2) es el del "= valor" o sea q si existe es pq la variable se inicializo y pongo inicializado en true
                if (str(ctx.getChild(2).getText()) != ''):
                    nuevaVar.setInicializado()
            else:
                # si es llamado a funcion, se actualiza cuando se comprueba que los tipos de datos son iguales (variable y retorno)
                self.tabla.agregar(nuevaVar)
                print(" "*self.indent+'Nuevo simbolo: ' + nuevaVar.nombre + ' agregado')
                self.listTdato.append(nuevaVar.nombre)
                self.listTdato.append(nuevaVar.tdato)
                self.isFuncion = 1
                self.exitCall_funcion(ctx.getChild(2).getChild(1).getChild(0).getChild(
                    0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0))
                return
        else:
            print(" "*self.indent+"Variable " + ctx.getChild(1).getText() +
                  " existente en el contexto")
            return
        self.tabla.agregar(nuevaVar)
        print(" "*self.indent+'Nuevo simbolo: ' + nuevaVar.nombre + ' agregado')

        self.listTdato.pop() #borro el tipo de dato de la lista pq ya la agregue a la tabla

        return

    def exitLista_var(self, ctx: compiladoresParser.Lista_varContext):
        #es recursiva y puede estar en nulo así q pregunto primero
        if ctx.getChildCount() != 0:
            if self.tabla.buscarLocal(ctx.getChild(1).getText()) == False: #busco el id en mi contexto local
                # como el Listener recorre el arbol de abajo hacia arriba, obtenemos el tipo
                # de dato subiendo el contexto hacia la declaracion
                if len(self.listTdato) == 0: #si esto es 0 significa q no sé el tipo todavía. vo
                    auxCtx = ctx
                    while (auxCtx.parentCtx.getChild(0).getText() == ','): #si el padre
                        auxCtx = auxCtx.parentCtx
                    self.listTdato.append(
                        auxCtx.parentCtx.getChild(0).getText())

                tdato = self.listTdato.pop()
                self.listTdato.append(tdato)
                name = str(ctx.getChild(1).getText())
                nuevaVar = Variable(name, tdato)
                # Si el 3er hijo en la declaracion es distinto de vacio, existe definicion
                if (str(ctx.getChild(2).getText()) != ''):
                    nuevaVar.setInicializado()
            else:
                print(" "*self.indent+"Variable " + ctx.getChild(1).getText() +
                      " existente en el contexto")
                return
            self.tabla.agregar(nuevaVar)
            print(" "*self.indent+'Nuevo simbolo: ' + nuevaVar.nombre + ' agregado')

            self.listTdato.pop()

        return

    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        # 1Obtener nombre de variable destino (a asignar)
        nombre_var = ctx.getChild(0).getText()
        contexto = self.tabla.buscar(nombre_var)

        if not contexto:
            print(" "*self.indent+"LA VARIABLE"+ nombre_var + "NO ESTÁ DEFINIDA")
            return

        var_destino = None
        for var in contexto.getSimbolos().values():
            if var.nombre == nombre_var:
                var_destino = var
                break

        # detecto si el lado derecho es una llamada a función
        rhs = ctx.getChild(2)  # lado derecho de la asignación
        nodo = rhs
        call_funcion_encontrada = None

        while nodo is not None and hasattr(nodo, 'getChildCount') and nodo.getChildCount() > 0:
            if nodo.getRuleIndex() == compiladoresParser.RULE_call_funcion:
                call_funcion_encontrada = nodo
                break
            nodo = nodo.getChild(0)

        if call_funcion_encontrada:
            # Guardo datos para validar dentro de exitCall_funcion
            self.listTdato.append(nombre_var)
            self.listTdato.append(var_destino.tdato)
            self.isFuncion = 1

            # Llamo a exitCall_funcion para procesar la función
            self.exitCall_funcion(call_funcion_encontrada)

            # Limpio bandera y lista de argumentos
            self.isFuncion = 0
            self.listArgs.clear()
            self.listTdato.clear()
            return

        # Si no es función, actualizo la variable normalmente
        varActualizada = Variable(var_destino.nombre, var_destino.tdato, True)
        self.tabla.actualizar(varActualizada)
        print(" "*self.indent+"Variable " +varActualizada.nombre + " actualizada con expresión normal")


    def exitCall_funcion(self, ctx: compiladoresParser.Call_funcionContext):
        # ID PA send args PC, busco primero si existe, si no aviso
        contexto = self.tabla.buscar(ctx.getChild(0).getText())
        
        if contexto == False:
            print(" "*self.indent+"FUNCION INEXISTENTE")
            return

        if self.isFuncion == 1:
#acá es como q creo una variable var q no desaparece cuando salgo el for
            for var in contexto.getSimbolos().values():
                if var.nombre == ctx.getChild(0).getText():
                    break
            #guardo los valores en var auxiliares y los borro de la pila
            tdato = self.listTdato.pop()
            nombre = self.listTdato.pop()
            if var.tdato == tdato:
                print(" "*self.indent+'La asignacion de: ' + nombre
                      + ' es posible')
                varActualizada = Variable(nombre, tdato, True)
                self.tabla.actualizar(varActualizada)
                print(" "*self.indent+"Variable " + nombre + " actualizada mediante funcion " + var.nombre)
            else:
                print(" "*self.indent+'La asignacion de: ' +
                      nombre + ' no es posible: Error de tipo de dato')

            self.isFuncion = 0
            return

        funcionVar = Funcion('', '', [])
        for var in contexto.getSimbolos().values():
            if var.nombre == ctx.getChild(0).getText():
                funcionVar = var
                break

        self.exitSend_args(ctx.getChild(2))

        if len(funcionVar.args) != len(self.listArgs):
            print(" "*self.indent+'Faltan parametros en la llamada de funcion')
            return

        for var1, var2 in zip(funcionVar.args, self.listArgs):

            if var1.tdato != var2.tdato:
                print(" "*self.indent+'Error: el parametro ' + var2 +
                      ' no es del tipo esperado')
                return

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
            print(" "*self.indent+'Nuevo simbolo ' + nuevaFuncion.nombre + ' agregado')
        else:
            print(" "*self.indent+'SIMBOLO YA DEFINIDO')

    def exitFuncion(self, ctx: compiladoresParser.FuncionContext):
        self.listArgs.clear()

        tdato = ctx.getChild(0).getText()
        nombre = ctx.getChild(1).getText()
        self.exitArgs(ctx.getChild(3))
        listaArgs = copy.deepcopy(self.listArgs)
        funcionVar = Funcion(nombre, tdato, listaArgs)
        funcionVar.setAccedido()

        contexto = self.tabla.buscar(nombre)

        # Si no existio prototipo de la funcion, se agrega a la tabla de simbolos
        if contexto == False:
            self.tabla.agregar(funcionVar)
            print(" "*self.indent+'Nuevo simbolo: ' + funcionVar.nombre + ' agregado')
            return

        # Si existe prototipo, verifico que la implementacion se corresponda
        for var in contexto.getSimbolos().values():
            if var.nombre == funcionVar.nombre:
                if var.tdato == funcionVar.tdato:
                    for arg1, arg2 in zip(var.args, funcionVar.args):
                        # En caso que el prototipo tenga nombre en el argumento
                        if arg1.nombre != '':
                            if arg1.nombre == arg2.nombre:
                                if arg1.tdato == arg2.tdato:
                                    pass
                                else:
                                    print(" "*self.indent+
                                        'LA IMPLEMENTACION DE ' + funcionVar.nombre + ' NO SE CORRESPONDE CON EL PROTOTIPO')
                                    return
                            else:
                                print(" "*self.indent+
                                    'LA IMPLEMENTACION DE ' + funcionVar.nombre + ' NO SE CORRESPONDE CON EL PROTOTIPO')
                                return
                    print(" "*self.indent+'La implementacion de ' + funcionVar.nombre +
                          ' se corresponde con su prototipo')
                    return

        print(" "*self.indent+
            'LA IMPLEMENTACION DE ' + funcionVar.nombre + ' NO SE CORRESPONDE CON EL PROTOTIPO')
        return

    def exitRetornar(self, ctx: compiladoresParser.RetornarContext):

        funcionCtx = ctx.parentCtx
        while True:
            if funcionCtx.getChild(0).getText() != 'int':
                if funcionCtx.getChild(0).getText() != 'double':
                    funcionCtx = funcionCtx.parentCtx
                else:
                    break
            else:
                break

        # Navegación segura para obtener el nombre
        child = ctx
        try:
            child = ctx.getChild(1)
            for _ in range(9):
                if child is not None and hasattr(child, 'getChild') and child.getChildCount() > 0:
                    child = child.getChild(0)
                else:
                    break
            nombre = child.getText() if child is not None else ""
        except Exception:
            nombre = ""

        if not nombre.replace('.', '', 1).isdigit():
            contexto = self.tabla.buscar(nombre)

            if contexto == False:
                print(" "*self.indent+'SIMBOLO ' + nombre + ' NO DEFINIDO')
                return

            for var in contexto.getSimbolos().values():
                if var.nombre == nombre:
                    break
        else:
            if '.' in nombre:
                var = Variable(nombre, 'double')
            else:
                var = Variable(nombre, 'int')

        if var.tdato == funcionCtx.getChild(0).getText():
            print(" "*self.indent+'El tipo de dato retornado por ' +
                  funcionCtx.getChild(1).getText() + ' es correcto')

        else:
            print(" "*self.indent+'El tipo de dato retornado por ' +
                  funcionCtx.getChild(1).getText() + ' no es correcto')

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

    def exitSend_args(self, ctx: compiladoresParser.Send_argsContext):
        self.listArgs.clear()
        if ctx.getChildCount() == 0:
            return

        nombre = str()
        if ctx.getChild(0).getChild(0).getChild(0).getChildCount == 2:
            nombre = ctx.getChild(0).getChild(
                0).getChild(0).getChild(1).getText()
        elif ctx.getChild(0).getChild(0).getChild(0).getChild(0).getChildCount() == 0:
            nombre = ctx.getChild(0).getChild(
                0).getChild(0).getChild(0).getText()

        if not nombre.replace('.', '', 1).isdigit():

            contexto = self.tabla.buscar(nombre)

            if contexto == False:
                print(" "*self.indent+'PARAMETRO ' + nombre + ' NO DEFINIDO')
                return

            for var in contexto.getSimbolos().values():
                if var.nombre == nombre:
                    self.listArgs.append(var)
        else:
            if '.' in nombre:
                var = Variable(nombre, 'double')
                self.listArgs.append(var)
            else:
                var = Variable(nombre, 'int')
                self.listArgs.append(var)

        self.exitLista_send_args(ctx.getChild(1))

        return

    def exitLista_send_args(self, ctx: compiladoresParser.Lista_send_argsContext):
        if ctx.getChildCount() == 0: #si no hay mas argumentos, salgo
            return

        nombre = str()
        if ctx.getChild(1).getChild(0).getChild(0).getChildCount == 2:
            nombre = ctx.getChild(1).getChild(
                0).getChild(0).getChild(1).getText()
        elif ctx.getChild(1).getChild(0).getChild(0).getChild(0).getChildCount() == 0:
            nombre = ctx.getChild(1).getChild(
                0).getChild(0).getChild(0).getText()

        # Se verifica que no sea un numero
        if not nombre.replace('.', '', 1).isdigit():

            contexto = self.tabla.buscar(nombre)

            if contexto == False:
                print(" "*self.indent+'PARAMETRO ' + nombre + ' NO DEFINIDO')
                return

            for var in contexto.getSimbolos().values():
                if var.nombre == nombre:
                    self.listArgs.append(var)
                    break

        # En caso de ser un numero, verificamos si es entero o decimal
        else:
            if '.' in nombre:
                var = Variable(nombre, 'double')
                self.listArgs.append(var)
            else:
                var = Variable(nombre, 'int')
                self.listArgs.append(var)

        if ctx.getChild(2).getChildCount() != 0:
            self.exitLista_send_args(ctx.getChild(1))

        return
    
    def enterI_while(self, ctx:compiladoresParser.I_whileContext):
        print(" "*self.indent + "<<< Entrando a un bloque while >>>")
        self.indent+=2
    
    def enterI_for(self, ctx:compiladoresParser.I_forContext):
        print(" "*self.indent + "<<< Entrando a un bloque for >>>")
        self.indent+=2