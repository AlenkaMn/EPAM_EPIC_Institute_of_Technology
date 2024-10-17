int: total_chips = 105;
array[1..total_chips] of var 0..1: chips;  

constraint forall(i in 1..total_chips-4) (
    sum(j in i..i+4) (chips[j]) >= 2
);


var int: max_white_chips = sum(i in 1..total_chips) (1 - chips[i]);

solve maximize max_white_chips;

output ["Maximum white chips: ", show(max_white_chips)];
