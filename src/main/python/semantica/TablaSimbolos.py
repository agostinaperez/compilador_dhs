from semantica.Contexto import Contexto

class TablaSimbolos:
    _instance = None
    _ctx = []

    def __new__(cls):
        if TablaSimbolos._instance is None:
            TablaSimbolos._instance = object.__new__(cls)
            TablaSimbolos._ctx.append(Contexto())
        return (TablaSimbolos._instance)

    def getContextos(self):
        return TablaSimbolos._ctx

    # si ingreso a un bloque meto un contexto nueno en la lista
    def agregarContexto(self):
        TablaSimbolos._ctx.append(Contexto())

    # Cada vez que salgo de un bloque, se elimina el contexto de la lista
    def borrarContexto(self):
        TablaSimbolos._ctx.pop()

    # Agrego un ID en el ultimo contexto (el de id -1)
    # la deñ diccionario entrada es {nombreId, Id}
    def agregar(self, variable):
        TablaSimbolos._ctx[-1].agregarSimbolo(variable)

    def actualizar(self, variable):
        TablaSimbolos.buscar(TablaSimbolos, variable.nombre).agregarSimbolo(variable)

    # Para el ultimo contexto, busco nombre del id x key. devuelv bool

    def buscarLocal(self, nombre):
        if nombre in TablaSimbolos._ctx[-1].getSimbolos():
            return TablaSimbolos._ctx[-1]
        return False

    # Buscamos la key en todos los contextos para cosas globales
    def buscar(self, nombre) -> Contexto:
        for context in TablaSimbolos._ctx[::-1]:
            if nombre in context.getSimbolos():
                return context
        return False