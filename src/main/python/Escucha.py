from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
#A TODOS LOS DATOS TIPO CTX.GETTEXT() LOS OBTENGO EN LAS EXIT
class Escucha (compiladoresListener):
    indent = 1
    declaracion = 0
    
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Comienza el parsing")
        
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Finaliza el parsing")
        print("Cantidad de declaraciones: " + str(self.declaracion))
        
    def enterIwhile(self, ctx:compiladoresParser.I_whileContext):
        print(" "*self.indent + "Comienza un while")
        self.indent = self.indent + 1
        
    def exitIwhile(self, ctx:compiladoresParser.I_whileContext):
        self.indent = self.indent - 1
        print(" "*self.indent + "Finaliza un while")
        
    def enterI_if(self, ctx:compiladoresParser.I_ifContext):
        print(" "*self.indent + "Comienza un if")
        self.indent = self.indent + 1
        
    def exitI_if(self, ctx:compiladoresParser.I_ifContext):
        self.indent = self.indent - 1
        print(" "*self.indent + "Finaliza un if")
        
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        self.declaracion += 1
    
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        print("Declaracion -> [" + ctx.getText() +"] ")
    
