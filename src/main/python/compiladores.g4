grammar compiladores;
fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

NUMERO: DIGITO+ | DIGITO+ '.' DIGITO+;

INT: 'int' ;
FLOAT: 'float' ;
CHAR: 'char' ;
STRING: 'string' ;
VOID: 'void' ;
IF: 'if' ;
ELSE: 'else' ;
FOR: 'for' ;
WHILE: 'while' ;
RETURN: 'return' ;

WS : [ \t\r\n] -> skip ;
EQ: '=';
EQQ: '==';
NE: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
MAS: '+';
MENOS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
AND: '&&';
ORR: '||';
NOT: '!';
PA: '(';
PC: ')';
LLA: '{';
LLC: '}';
PYC: ';';
COMA: ',';
SHL: '<<';   // shift left
SHR: '>>';   // shift right
TERNARIO: '?';
DOS_PUNTOS: ':';
ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;
OTRO : . ;

/*si quisiera hacer balance de paréntesis
s: PA s PC s
  | 
  ;*/

//tengo q detectar para ver q NOT solo me haya armado un arbol correcto si NOT q también NOT me haya quedado cadenas sin leer en el buffer pq eso es un error q el arbol NOT me muestra



/*TENER EN CUENTA QUE SÍ ES VÁLIDA LA ANIDACION SIN PARÉNTESIS ORR SEA
if (a)
  while (x)
    if (AND)
      for (d)
        x=1; */
programa: instrucciones EOF;

instrucciones: instruccion instrucciones
            |;

instruccion: declaracion PYC
	| asignacion PYC
	| retornar PYC
	| i_if
	| i_for
	| i_while
	| funcion
	| call_funcion PYC
	| proto_funcion PYC
	| bloque;

bloque: LLA instrucciones LLC ;

valor: NUMERO | ID;

tipo: INT | FLOAT | CHAR | STRING | VOID;

operador: EQQ | NE | GT | LT | GE | LE;

declaracion: tipo ID definicion lista_var;

lista_var: COMA ID definicion lista_var
          | COMA definicion lista_var
          | ;

definicion: EQ oplo |;

asignacion: ID EQ oplo;

//----------OPERACIONES ARITMETICAS AND LÓGICAS-------------------------------------------------------

oplo: logic_termino logic_expr
    | ternario;

logic_expr: ORR logic_termino logic_expr |;

logic_termino: logic_factor logic_term;

logic_term: AND logic_factor logic_term |;

logic_factor: opar | comp | (PA oplo PC);

comp: opar operador opar | comp operador comp;

opar: termino exp;

exp: MAS termino exp 
    | MENOS termino exp 
    | SHL termino
    | SHR termino
    |;

termino: factor term;

term: MULT factor term | DIV factor term | MOD factor term |;

factor: ((MENOS |) NUMERO)
	| ((MENOS |) ID)
	| call_funcion
	| PA opar PC;

//----------FUNCIONES----------------------------------------

proto_funcion: tipo ID PA args PC;

funcion: tipo ID PA args PC bloque;

retornar: RETURN oplo;

call_funcion: ID PA send_args PC;

args: tipo arg lista_args
    | ;

lista_args: | COMA tipo arg lista_args;

arg: ID |;

send_args: opar lista_send_args;

lista_send_args: COMA opar lista_send_args |;

//----------ESTRUCTURAS DE CONTROL AND CONDICIONALES--------------

i_while: WHILE PA oplo PC instrucciones;

i_if: IF PA oplo PC bloque ( | i_else);

i_else: ELSE bloque;

i_for:
	FOR PA (asignacion | declaracion) PYC oplo PYC asignacion PC instrucciones;

ternario: logic_termino logic_expr TERNARIO oplo DOS_PUNTOS oplo;


