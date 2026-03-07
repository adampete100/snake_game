# Overview

This project was something simple to give me a better understanding of how game development works. Given that I don't know how to use programs for more polished projects like unreal Engine, Godot, or Unity, I decided to make a game through the pygame framework.

The game I developed is a simple snake game, with a way to store a high score, and it uses some basic royalty free music for the gameplay, and a short tune that plays after the player loses. It follows all the rules of snake, those being:
- Eat fruits (in this case the red dots that appear randomly) to grow the snake
- Don't run the snake into the walls
- Don't run the snake into itself
to move the snake, players just press the arrow keys in the corresponding direction for the snake to move said direction.

In writing this game, my goal was to gain a better understanding of how to develop graphics, write logic, and debug a game on a basic level. This project taught me those things, and some extra things that are important. For example, making the game run at a specific speed so it's playable (otherwise it'll run as fast as the computer will let it, making it unplayable usually), displaying text on the game window, and how to play music.

{add youtube link here}
[Software Demo Video](http://youtube.link.goes.here)


# Install Instructions
To play the game after cloning the repository to your computer, please do the following:
1. Install VSCode if you don't already have it, along with the python extension via the extensions menu shortcut on the sidebar
2. Run the following command to install the Pygame-ce dependency: pip install pygame-ce (if this doesn't work, try pip3 instead of pip)
3. Click the file option in the top-left menu bar, and click open folder to choose the folder you cloned the repository to (or extracted the zip to)
4. Click the play button in the top right of the vscode window (below the minimizne and close buttons), and the game will start. Enjoy!


# Development Environment

For this project, I used the VSCode IDE, the Python language, and the Pygame framework library for Python. I also utilized some extra system modules, like the random module (to choose a random spawn location for the fruit in the game) and time module (to ensure the game ran at a playable speed).


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Pygame Documentation](https://www.pygame.org/docs/)
* [Pygame Subreddit (to look for answers for issues)](https://www.reddit.com/r/pygame/)
* [GeeksforGeeks Pygame tutorials](https://www.geeksforgeeks.org/python/pygame-tutorial/)


# Future Work

* Create an input buffer for better snake movement
* Add sound effects for eating fruit, and beating a high score
* Implement other level maps, and a starting menu to select them from
* Add more interesting background colors/images
* Allow the user to change the color of the snake and/or apple