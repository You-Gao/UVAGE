'''
Name / ID: You Gao | djx3rn
Name / ID: Tiffany Cheung | vzs9mw

-Game Idea:
    The game is called snake, a player uses the arrow / wasd keys to control a snake - like figure around the
board and tries to feed it so that it grows. If it runs into the walls / moves off the screen or bites itself the game ends and you start over. The main goal being to survive and to grow the snake as large as possible before that happens.

-User Input:
    Keyboard input, supports either WASD or arrow key
    uvage.is_pressing()

-Game Over:
    Ends the game once the snake bites itself
    snake.touches(snake, -25, -25, ) * only if it fully chomps on itself

-Graphics / Images:
    Snake, Power - Ups, Apple, Game - Over, Leaderboard, & Buttons
    Adobe Illustrator or Free - Images

-Collectibles:
    Power - ups that alter the game state, *speed - up, *slow - down, *shield - once, etc.
    Spawn in random collectibles on an unoccupied square in the game

-Restart from Game Over:
    A button that allows for the game to restart which shows up after ‘continue’ on the leaderboard
    Reset the game state of every object to the initial states

-Sprite Animation:
    Drawing animation for the snake, coin, & apple
    Create an animation with a counter to track which animation should be shown

-Inter - Session Progress:
    A high - score leaderboard that pops ups after the game over
    open(‘file’, ‘a’) writes with a specific format
    open(‘file’ ‘r’)  return the highest 5 for the leaderboard
'''
