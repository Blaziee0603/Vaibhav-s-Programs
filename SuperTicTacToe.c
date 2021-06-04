#include <stdio.h>
#include <stdlib.h>

/* The player whose turn it is to play next */
int Player;

/* The number of moves made */
int Moves;

/* The board.  0 represents no piece, 1 player 1's piece, 2 player 2's piece. */
int Board[15][15];
/* Note that as this is C, all array indices count from zero rather than 1. */

/* Initialise the board to all 0's */
void InitBoard(void) {
	int i, j;
	for (i = 0; i < 15; i++) for (j = 0; j < 15; j++) Board[i][j] = 0;
	Moves = 0;
}

/* Show the board in the required format */
void ShowBoard(void) {
	int i, j;
	for (i = 0; i < 15; i++) {
		for (j = 0; j < 15; j++)
			if (Board[i][j] == 0) printf(".");
			else if (Board[i][j] == 1) printf("X");
			else if (Board[i][j] == 2) printf("O");
		printf("\n");
	}
}

/* Test whether the current move wins the game */
int WinsGame(int i0, int j0) {
	int i, j;

	/* Test horizontal lines of 5 pieces including the current one */
	i = i0;
	j = j0 - 4; if (j < 0) j = 0;
	while ((j <= j0) && (j <= 3)) {
		if ((Board[i][j] == Board[i0][j0]) &&
			(Board[i][j + 1] == Board[i0][j0]) &&
			(Board[i][j + 2] == Board[i0][j0]) &&
			(Board[i][j + 3] == Board[i0][j0]) &&
			(Board[i][j + 4] == Board[i0][j0]))
			return 1;

		/* Not won - try the next starting position */
		j++;
	}

	/* Test vertical lines of 5 pieces including the current one */
	j = j0;
	i = i0 - 4; if (i < 0) i = 0;
	while ((i <= i0) && (i <= 2)) {
		if ((Board[i][j] == Board[i0][j0]) &&
			(Board[i + 1][j] == Board[i0][j0]) &&
			(Board[i + 2][j] == Board[i0][j0]) &&
			(Board[i + 3][j] == Board[i0][j0]) &&
			(Board[i + 4][j] == Board[i0][j0]))
			return 1;

		/* Not won - try the next starting position */
		i++;
	}

	/* Test \-diagonal lines of 5 pieces including the current one */
	j = j0 - 4; i = i0 - 4;
	while ((j < 0) || (i < 0)) { j++; i++; };
	while ((i <= i0) && (i <= 2) && (j <= j0) && (j <= 3)) {
		if ((Board[i][j] == Board[i0][j0]) &&
			(Board[i + 1][j + 1] == Board[i0][j0]) &&
			(Board[i + 2][j + 2] == Board[i0][j0]) &&
			(Board[i + 3][j + 3] == Board[i0][j0]) &&
			(Board[i + 4][j + 4] == Board[i0][j0]))
			return 1;

		/* Not won - try the next starting position */
		j++; i++;
	}

	/* Test /-diagonal lines of 5 pieces including the current one */
	j = j0 + 4; i = i0 - 4;
	while ((j > 6) || (i < 0)) { j--; i++; };
	while ((i <= i0) && (i <= 2) && (j >= j0) && (j >= 3)) {
		if ((Board[i][j] == Board[i0][j0]) &&
			(Board[i + 1][j - 1] == Board[i0][j0]) &&
			(Board[i + 2][j - 2] == Board[i0][j0]) &&
			(Board[i + 3][j - 3] == Board[i0][j0]) &&
			(Board[i + 4][j - 4] == Board[i0][j0]))
			return 1;

		/* Not won - try the next starting position */
		j--; i++;
	}

	/* No, this has not won the game */
	return 0;
}

/* Apply the rules to make the next move, and exit if the game is over */
void DoMove(void) {
	int i, j;

	/* Rule 1 - if we can win immediately, do so. */
	for (j = 0; j < 15; j++) {
		if (Board[0][j] == 0) {
			/* Find the first place that we can go */
			i = 0;
			while ((i < 15) && (Board[i][j] == 0)) i++;
			i--;

			/* See if going here wins */
			Board[i][j] = Player;
			if (WinsGame(i, j)) {
				ShowBoard();
				printf("Player %d wins\n", Player);
				exit(0);
			}
			else
				/* Erase this move and try the next */
				Board[i][j] = 0;
		}
	}

	/* Rule 2 - if the other player can win immediately, go there. */
	for (j = 0; j < 15; j++) if (Board[0][j] == 0) {
		/* Find the first place that we can go */
		i = 0;
		while ((i < 15) && (Board[i][j] == 0)) i++;
		i--;

		/* See if going here would win for the other player */
		Board[i][j] = 3 - Player;
		if (WinsGame(i, j)) {
			/* We go there */
			Board[i][j] = Player;
			return;
		}
		else
			/* Erase this move and try the next */
			Board[i][j] = 0;
	}

	/* Rule 3 - go in first available space. */
	for (j = 0; j < 15; j++) if (Board[0][j] == 0) {
		/* Find the first place that we can go */
		i = 0;
		while ((i < 15) && (Board[i][j] == 0)) i++;
		i--;

		Board[i][j] = Player;
		return;
	}
}

/* Function to solve Q2a */
void Q2a(void) {
	char c;
	int n, count, i, j;
	Player = 1;
	InitBoard();

	/* Play the initial sequence of moves */

	/* Read the number of initial moves */
	scanf("%d", &n);

	/* Do the initial moves */
	for (count = 0; count < n; count++) {
		/* Get the column for the next move */
		scanf("%d", &j);
		/* Reduce by 1 since we're counting from 0, but the question counts from 1 */
		j--;

		/* Find the next position we can go */
		i = 0;
		while ((i < 15) && (Board[i][j] == 0)) i++;
		i--;

		Board[i][j] = Player;
		Player = 3 - Player;
		Moves++;
	}
	ShowBoard();

	/* The main loop where we get an instruction and process it */
	while (Moves < 225) {
		scanf("%c", &c);
		if ((c == 'n') || (c == 'N')) {
			/* Play the next move */
			DoMove();
			ShowBoard();
			Moves++;
			Player = 3 - Player;
		}
		else if ((c == 'r') || (c == 'R')) {
			while (Moves < 225) {
				DoMove();
				Moves++;
				Player = 3 - Player;
			}
		}
	}

	/* Neither player has won and the board is now full. */
	ShowBoard();
	printf("Draw\n");
	scanf("%c", &c);
}

/* Count of the number of combinations for Q2d */
long Npatterns;

/* Recursive helper function to count the number of combinations for Q2d */
void TryPos(int Column, int Remaining) {
	int This;
	if (Column == 8) {
		if (Remaining == 0) {
			/* This is a valid pattern with all 21 pieces placed, so add to the count */
			Npatterns++;
		}
	}
	else {
		/* Try to place between 0 and 6 pieces in Column, then recurse to try the next */
		This = 0;
		while ((This <= 15) && (This <= Remaining)) {
			TryPos(Column + 1, Remaining - This);
			This++;
		}
	}
}

/* Function to solve Q2d */
void Q2d(void) {
	Npatterns = 0;
	TryPos(1, 21);
	printf("Number of distinct patterns for Q2d is %d\n", Npatterns);
}

/* Main function called from the command-line */
void main(void) {
	Q2a();		/* Edit this line to Q2d() to solve 2d */
}
/* End of program */