ordenada([], []).

ordenada([X|C], L) :-
	particionar(X, C, Y, W),
	ordenada(Y, Y2),
	ordenada(W, W2),
	concatenar(Y2, [X|W2], L).
	
particionar(_, [], [], []).

particionar(X, [Y|C], [Y|Z], W) :-
	maior(X,Y),
	!,
	particionar(X, C, Z, W).
	
particionar(X, [Y|C], Z, [Y|W]) :-
	particionar(X, C, Z, W).
	
concatenar([], L, L).

concatenar([X|L], L2, [X|L3]) :-
	concatenar(L, L2, L3).
	
maior(X, Y) :- X > Y.
	

	
	
	
	
	
	
	
	
	
	