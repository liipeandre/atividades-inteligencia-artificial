intercaladas(L, [], L):- !.
intercaladas([], L, L):- !.
intercaladas([X|L1], [Y|L2], [X,Y|L3]):-
	intercaladas(L1, L2, L3).