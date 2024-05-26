grammar Juvenalia;

prog: stat*  EOF 
    ;

stat:	WRITE ID		#write
	| READ ID   		#read
    | expr              # exprression
 	| ident '=' expr		#assign
    | ID '[' INT ']' '=' expr #elementAssign
    | ident '=' arrayAssign  #arrAssign
    | repeatStm                #repeatStatement
    | ifStm                 #ifStatement
    | function              #funcDecl
    | structDecl            #structDeclaration
    | structFieldAssign     #structFieldAssignment
    | structAssign          #structAssignmet
    | classDecl             #classDeclaration
    | classAssign           #classAssignment
    ;

arrayAssign: '[' factor (',' factor)* ']';

expr: condXorStm OrOper condXorStm 
    | condXorStm
    ;

condXorStm: condStmAnd XorOper condStmAnd
    | condStmAnd
    ;

condStmAnd: condStmRel AndOper condStmRel
    | condStmRel
    ;

condStmRel: addExpr RelOper addExpr
    | addExpr
    ;

addExpr: multExpr AddOper multExpr
    | multExpr
    ;

multExpr: negFactor MultOper negFactor
    | negFactor
    ;

negFactor: NegOper factor 
    | factor
    ;


factor: INT
    | FLOAT
    | STRING
    | BOOL
    | ID
    | arrayAccess
    | funcCall
    | structFieldAccess
    | methodCall
    ;


ifStm: IF '(' expr ')' '{' blockIf '}' ;

blockIf: stat* ;

repeatStm: REPEAT repNum '{' blockRepeat '}'  
    ;

repNum: factor 
    ;

blockRepeat: stat* 
    ;

function: FUNCTION funType funName '{' blockFun '}' ;

blockFun: stat* ;





classDecl: CLASS className '{' blockClass '}'  ;

blockClass: structVarDecl* method*  ;

method: methodType methodName '{' blockMethod '}'  ;

blockMethod: stat*  ;

methodType: type ;

methodName: ID ;

className: ID ;

methodCall: ID '.' ident '()' ;

classAssign: ident '=' CLASS className ;




structDecl: STRUCT structName '{' blockStruct '}' ;

blockStruct: structVarDecl* ;

structVarDecl: ident ;

structAssign: ident '=' STRUCT structName;

structFieldAssign: ID '.' ident '=' expr ;

structFieldAccess: ID '.' ident ;

arrayAccess: ID '[' INT ']';

funcCall: ID '()' 
    ;

ident: ID (':' type)?;

type: 'float32' | 'float64' | 'int32' | 'int64' | 'bool' | 'str';

funType: type 
    ;

funName: ID 
    ;
structName: ID
    ;

WRITE:	'write' 
   ;

READ:	'read' 
   ;

IN: 'in';

REPEAT: 'rep';

IF: 'if';

FUNCTION: 'func'
    ;

CLASS: 'class'  ;

STRUCT: 'struct' ;
   

INT:   [0-9]+
    ;

FLOAT: [0-9]+ '.' [0-9]+
    ;

BOOL    : 'true' | 'false';

AddOper: '+' | '-'
    ;

MultOper: '*' | '/'
    ;

NegOper: '!'
    ;

RelOper: '==' | '!=' | '<' | '>' | '<=' | '>='
    ;

AndOper: '&&'
    ;

OrOper: '||'
    ;

XorOper: '^^'
    ;

ID:   [a-zA-Z]+
   ;

STRING :  '"' [a-zA-Z0-9 \t\n*+-]+ '"';

NEWLINE:	'\r'? '\n'
    ;

WS : [\r\n \t]+ -> skip;

