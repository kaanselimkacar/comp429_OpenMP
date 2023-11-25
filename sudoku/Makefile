gcc: sudoku_solver.c
	gcc -o sudoku_solver sudoku_solver.c -fopenmp -lm
	
clean:   
	rm -f sudoku_solver

easy: gcc
	./sudoku_solver 9 grids/3x3_easy.csv

hard1: gcc
	./sudoku_solver 16 grids/4x4_hard_1.csv


hard2: gcc
	./sudoku_solver 16 grids/4x4_hard_2.csv


hard3: gcc
	./sudoku_solver 16 grids/4x4_hard_3.csv
