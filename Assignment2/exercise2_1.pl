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

% Eligible for succession if child of queen elizabeth
successor(X) :- parent(queen_elizabeth, X).

% Male has priority for succession
better(X, Y) :-
    male(X), female(Y).

% Comparing 2 males, the older has priority for succession
better(X, Y) :-
    male(X), male(Y),
    older(X, Y).

% Comparing 2 females, the older has priority for succession
better(X, Y) :-
    female(X), female(Y),
    older(X, Y).