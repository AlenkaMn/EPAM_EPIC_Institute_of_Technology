
int: N;
array[1..N, 1..N] of 0..1: a;


array[1..N] of var 0..1: in_clique;


constraint
  forall (i, j in 1..N where i < j) (
    (in_clique[i] = 1 /\ in_clique[j] = 1) -> a[i, j] = 1
  );


var int: clique_size = sum(in_clique);

solve maximize clique_size;


output ["\(clique_size) "]
       ++ [ show([i | i in 1..N where in_clique[i] = 1])];
