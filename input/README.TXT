Reglas del c q tiene que implementar mi compilador y tokens que debe capturar
-enteror (negativos y positivos)
-ID (variables y funciones)
-palabras reservadas: if, for, while
-paréntesis
-punto y coma
-declaracion de variables
-opreacion aritmetica logica
-caracteres de agrupacion

NO HACEMOS PRINTS

x ahora no puedo ejecutar
las reglas gramaticales en antlr se parecen a las expresiones regulares pero no es lo mismo,
la gramatical es recursiva y las ER son iterativas
TENEMOS Q USAR RECURSIVIDAD, NO ITERATIVIDAD


ACTIVIDAD 1:
Crear las expresiones regulares para capturar tokens de tipo:
 1- Enteros (positivos y negativos)
 2- ID (varibles y funciones)
 3- Palabras reservadas: if, else, for y while
 4- Caracterer operador: +, -, *, /, =
 5- Caracterer agrupacion: {, }, [, ], (, )
 6- Caracterer punto y coma: ;

 ACT 2:
 Sobre las reglas gramaticales vistas en clases
construya las siguientes:

a) return
b) declaraciones
    1) con asignación simple -> int x = 0;
    2) como lista de variables -> int x, y, z;
    3) como lista con asignaciones -> int x = 0, y, z = x;
b) while

NO HACER DO WHILE NI HACER SWITCH, NI FOR EACH
PROTOTIPOS Y DEFINICION DE FUNCIONES