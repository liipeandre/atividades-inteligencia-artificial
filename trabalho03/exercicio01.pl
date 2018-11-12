remover_elementos(_,[],[]).

remover_elementos(X, [X|C], L) :- 
	remover_elementos(X, C, L).

remover_elementos(X, [Y|C], [Y|C2]) :-
	X \== Y,
	remover_elementos(X, C, C2).

	
elem_repetidos([], []).

elem_repetidos([X|C], [X|C2]) :-
	remover_elementos(X, C, L),
	elem_repetidos(L, C2).
	
	