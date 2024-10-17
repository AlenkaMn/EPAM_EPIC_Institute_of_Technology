grammar Eson;
SPACE: [ \n\r\t] -> skip;
COMMENT: '#' ~('\n'|'\r')* -> skip;

//старт
start: item EOF;

item: object ;
object: '{' pair (',' pair)* '}' ;
pair: key '=' value;

key: (WORD | FOR_DOUBLE_QUOTES);
value:
    WORD
    | array
    | dict
    | NULL
    | BOOL
    | DATE
    | DATETIME
    | TIME
    | FOR_DOUBLE_QUOTES
    | FOR_SINGLE_QUOTES
    | NUMBER
    | INTEGER
    ;

//чтобы считались и пустой словарь за словарь и пустой массив за массив
array: '[' (value (',' value )*)?','? ']';
dict: '{' (pair (',' pair)*)? ','?'}';


NULL: 'null';
BOOL: 'true' | 'false';


//дата и время
DOT: '.';
DATE: DIGIT DIGIT DIGIT DIGIT '-' ('0' [1-9] | '1' [0-2]) '-' ('0' [1-9] | [12] DIGIT | '3' [01]);
DATETIME: DATE 'T' TIME;
TIME: (('0' DIGIT) | ('1' DIGIT) | ('2' DIGIT)) ':' [0-5] DIGIT ':' ([0-5] DIGIT |FLOAT | INTEGER DOT INTEGER+);

//разные строки
FOR_DOUBLE_QUOTES: '"' (~["\\] | '\\' .)* '"';
FOR_SINGLE_QUOTES: '\'' (~['\\] | '\\' .)* '\'';
WORD: [a-zA-Z_][a-zA-Z0-9_-]*;


NUMBER: OCTAL_NUMBER | INTEGER | FLOAT | HEX;
INTEGER: [+-]?'0' | [+-]?[1-9][0-9]*;
OCTAL_NUMBER: [+-]? '0' [0-7]+ ([0-7]+)?;

INT : '0' | [1-9] DIGIT*;
EXPONENT: [eE] [+-]? DIGIT+|'e' INT+ ;
FLOAT: [+-]? INT DOT INT+? | [+-]? DOT INT+? | [+-]? INT+ DOT INT+? | [+-]? INT+ DOT EXPONENT | [+-]? INT+ DOT EXPONENT INT+ | INT DOT | [+-]? INT+ DOT INT+? EXPONENT|('+' | '-')? DIGIT* DOT DIGIT* ('e' ('+' | '-')? DIGIT+)? | DIGIT+ 'e' ('+' | '-')? DIGIT+ | DIGIT* DOT 'e' ('+' | '-')? DIGIT+;


HEX: [+-]?'0x' HEX_DIGIT+;
DIGIT: [0-9];
HEX_DIGIT: [0-9a-fA-F];
