las palabras reservadas no van en la tabla de simbolos pero si va todo lo definido x el usuario, y tiene una tabla de simbolos x cada contexto. LOs identificacores son tipo variable o tipo funcion

en el analisis semantico me deberian saltar cosas del estilo asignar un float a un string sin convertir o llamar funcion de un obj q no existe o etc
necesito atributos de los símbolos y reglas semanticas
ej
declaracion: tipo IP PYC; -> regla semantica sería
si (id no existe) {lo agrego a la tabla de simbolos} else {ERROR SEMANTICO (id ya existe)}

cuando entro a un bloque agrego contexto a la tabla de simbolos, cuando me voy se lo saco.