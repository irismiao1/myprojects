# Hextrix112

Hextrix is a game similar to Tetris in the sense that the player will be given
predetermined pieces and must fill up empty rows to earn points. The board
itself is a 4x4 hexagonal grid with empty cells being hexagons. There are 5
hexagonal pieces in total and 3 random pieces will be displayed at the bottom
for the player to use at all times. 
There are two modes to the game, Single Player and Multiplayer. In Single Player,
the objective is just to fill up as many rows as you can with the given pieces.
You reach Game Over if the 3 pieces cannot fit anywhere in the empty cells of 
the board. In Multiplayer, two players take turns placing the pieces on the board
and the objective is to fill up as many rows as well. Game Over is reached if
one of the player's 3 choices cannot fit in the empty cells, however that does
not determine the winner. The higher scoring player wins the round. 
If the player (whether in Single or Multiplayer mode) decides to place a piece 
in the "Next Best Move" box, located at the bottom right of the window, cells
will be highlighted, revealing the best possible move for that piece. This is 
calculated based on the relationship between the piece and the state of the 
game. After viewing the next best move(s), the player may place the piece in one
of the highlighted positions.

Hextrix can be ran in a general text editor. It utilizes cmu_112_graphics and 
tkinter.

Shortcut Commands: "h" for help, "1" for single player, "2" for multiplayer,
"r" to restart.
