parent(queen_elizabeth, prince_charles).
parent(queen_elizabeth, princess_ann).
parent(queen_elizabeth, prince_andrew).
parent(queen_elizabeth, prince_edward).

older(prince_charles, princess_ann).
older(princess_ann, prince_andrew).
older(prince_andrew, prince_edward).

male(prince_charles).
male(prince_andrew).
male(prince_edward).
female(princess_ann).


% All children are successors (no gender consideration)
successor(X) :-
    parent(queen_elizabeth, X).

% Older child has priority for succession
better(X, Y) :-
    successor(X),
    successor(Y),
    older(X, Y).