inserir_ord(X, [], [X]) :- !. 

inserir_ord(X, [Y|C], [X|[Y|C]]) :- 
	X =< Y, 
	!.
	
inserir_ord(X, [Y|C], [Y|C2]) :- 
	inserir_ord(X, C, C2).