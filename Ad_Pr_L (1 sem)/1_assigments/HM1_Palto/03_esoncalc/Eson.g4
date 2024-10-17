grammar Eson;
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~('\n'|'\r')* -> skip;


start: item EOF;

item: object;
object: '{' pair (',' pair)* '}';
pair: key '=' value;

key: (WORD | FOR_DOUBLE_QUOTES);

value:
    WORD
    | array
    | dict
    | BOOL
    | DATE
    | DATETIME
    | TIME
    | FOR_DOUBLE_QUOTES
    | FOR_SINGLE_QUOTES
    | NUMBER
    | NULL
    | expr;


//чтобы считались и пустой словарь за словарь и пустой массив за массив
array: '[' (value (',' value )*)?','? ']';
dict: '{' (pair (',' pair)*)? ','?'}';


//дата и время
DOT: '.';
DATE: DIGIT DIGIT DIGIT DIGIT '-' ('0' [1-9] | '1' [0-2]) '-' ('0' [1-9] | [12] DIGIT | '3' [01]);
DATETIME: DATE 'T' TIME;
TIME: (('0' DIGIT) | ('1' DIGIT) | ('2' DIGIT)) ':' [0-5] DIGIT ':' ([0-5] DIGIT |FLOAT | INT DOT INT+);


NULL: 'null';
BOOL: 'true' | 'false';


SIN: 'sin';
COS: 'cos';

//разные строки
FOR_DOUBLE_QUOTES: '"' (~["\\] | '\\' .)* '"';
WORD: [a-zA-Z_][a-zA-Z0-9_-]*;
FOR_SINGLE_QUOTES: '\'' (~['\\] | '\\' .)* '\'';


expr: 
    expr '+' term
    | expr '-' term
    | term;

term: 
    term '*' factor
    | term '/' factor
    | factor;
    
factor:
     '+' factor
     | '-' factor
     | primary;

primary: 
       NUMBER 
       | '(' expr ')' 
       | SIN '(' expr ')'
       | COS '(' expr ')';

NUMBER: FLOAT | INT | HEX | OCTAL_NUMBER;

DIGIT: [0-9];

INT: '0' | [0-9] DIGIT*;
HEX: [+-]?'0x' [0-9a-fA-F]+;
OCTAL_NUMBER: [+-]? '0' [0-7]+ ([0-7]+)?;
FLOAT: (DIGIT+ '.' DIGIT* | '.' DIGIT+) (('e' | 'E') ('+' | '-')? DIGIT+)? | DIGIT+ ('e' | 'E') ('+' | '-')? DIGIT+;

