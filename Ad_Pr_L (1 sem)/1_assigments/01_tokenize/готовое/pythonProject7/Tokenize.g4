lexer grammar Tokenize;


WS : [ \t\r\n]+ -> skip;

// 1 пункт
DIGIT : [0-9];
HEX_DIGIT : [0-9a-fA-F];

INTEGER : '0' | [1-9] DIGIT*; // Целые числа без ведущих нулей
ZERO_INTEGER : '0' DIGIT; // Целые числа с ведущими нулями
HEX_INTEGER : '0x' HEX_DIGIT+;

PLUS : '+';
MINUS : '-';

SIGNED_INTEGER : (PLUS | MINUS) (INTEGER | ZERO_INTEGER);
SIGNED_HEX_INTEGER : (PLUS | MINUS) HEX_INTEGER;


// 2 пункт
WORD: [a-zA-Z]+ ([a-zA-Z]*[0-9]+[a-zA-Z]*)? ; // Слова состоящие из латинских букв


// 3 пункт
INT_NUMBER: INTEGER EXPONENT? ;
EXPONENT: [eE] [+-]? DIGIT+|'e' INTEGER+ ;
FLOAT: [+-]? INTEGER DOT INTEGER+? | [+-]? DOT INTEGER+? | [+-]? INTEGER+ DOT INTEGER+? | [+-]? INTEGER+ DOT EXPONENT | [+-]? INTEGER+ DOT EXPONENT INTEGER+;
DOP_FLOAT: [+-]? INTEGER DOT | [+-]? INTEGER+ DOT INTEGER+? EXPONENT;
DOT: '.';

// 4 пункт
SK: '\'"\''   ;
SLASH           : '/' ;
BACK_SLASH      : '\\';
SKOBOCHKA       : '"' ;
SINGLE_QUOTE    : '\'' ;

TWO_DIGIT       : DIGIT DIGIT ;


GENERAL_SYMBOL  :  SLASH | BACK_SLASH | SINGLE_QUOTE | SKOBOCHKA;



ESCAPED_CHAR : '\\' [nrt\\'"]
            | '\\u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT //  \uXXXX
            | ~[\\\r\n\t'"] ;

SINGLE_QUOTE_TOKEN : '\'' (ESCAPED_CHAR | '\\' '\'') '\''; // Single-quoted tokens
DOUBLE_QUOTE_TOKEN : '"' (ESCAPED_CHAR | '\\' '"')* '"'; // Double-quoted tokens

TOKEN : SINGLE_QUOTE_TOKEN | DOUBLE_QUOTE_TOKEN;


// 4 пункт (даты)

DATE_FORMAT: DIGIT DIGIT DIGIT DIGIT '-' ('0' [1-9] | '1' [0-2]) '-' ('0' [1-9] | [12] DIGIT | '3' [01]);


// 5 пукт время
TIME: HOURS ':' MINUTES ':' ( SECONDS | FLOAT | INTEGER DOT INTEGER+ ) ;

fragment HOURS: ('0' [0-9]) | ('1' [0-9]) | ('2' [0-3]);
fragment MINUTES: [0-5] DIGIT;
fragment SECONDS: [0-5] DIGIT;


// 6 пункт дата и время
DATETIME: DATE_FORMAT 'T' TIME;



// 7 пункт продолжительность

SPECIAL_DUR_FLOAT: [+-]? INTEGER DOT INTEGER+? | [+-]? DOT INTEGER+? | [+-]? INTEGER+ DOT INTEGER+? | [+-]? INTEGER DOT;
DURATION: [+-]? (SPECIAL_DUR_FLOAT | INTEGER) ('ns' | 'us' | 'ms' | 's' | 'm' | 'h') | ('ns' | 'us' | 'ms' | 's' | 'm' | 'h') [+-]? (SPECIAL_DUR_FLOAT | INTEGER) ('ns' | 'us' | 'ms' | 's' | 'm' | 'h') | 'd' '-' INTEGER;


// 8 пункт спец слова с _/-

SPECIAL_WORDS: WORD '_' (WORD | INTEGER);
S_W_2: WORD '-' INTEGER;











