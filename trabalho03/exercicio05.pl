subculturas([X|C], L) :-
	subculturas(C, L1),
	busca(X, L1, L).
	

busca(X, [], [X]).

busca(X, [C|R], L) :-
	intersecao(X, C1),
	uniao(X, C1, L1),
	busca(X, R, L).
	
busca(X, [C1, R1], L) :-
	busca(X, R1, L).