# Football-Simulator
**By Nathan Blanchard and Skyler Heininger**

This was my first significant coding project that I created as a final project the class `Computer Programming I` at UVM
with my roomate Skyler Heininger. The code is a little messy, and it is by no means perfect, but this was a fun
introduction to the world of programming!

Welcome to Football-Simulator, a text-based football game where you compete against the computer in a series of 3 games.
The objective for each game is to be the first to score three touchdowns and emerge victorious!

## Getting Started
Running this program is straightforward. Simply follow the on-screen instructions, and the help function at the start
can be used to display information about the game.

### User Authentication and Save-states
If you indicate that you have played before, you'll be prompted to enter a username and password stored in the
`savestates.txt` file. This file is formatted for efficient data retrieval and storage, and it allows the user to pick up
where they left off in a previous game.

### Selecting a Team
Each team has distinct offensive and defensive statistics, try different teams to figure out which best 
matches your play-style! The bracket consists of three randomly selected teams.

### Gameplay
When it is your turn, you will be presented with four options for plays:
- Run
- Short pass
- Long pass
- Hail mary

Each option is increasingly risky, but the chance of gaining a significant number of yards is also greater.

### Important Notes
1. **Empty Bracket:** If a user loads a save with no remaining teams in the bracket, no further games will be played.
2. **Saved Data:** Only essential aspects of each game are saved, including remaining teams in the bracket and games won. 
3. **Saving Games:** A game will only be saved if the bracket is finished or completed. Failure to save in this manner will
result in data loss from the `savestates.txt` file.
4. **Time Delay:** To enhance the user experience, there is a deliberate time delay between various aspects of gameplay.
This ensures players have sufficient time to read and absorb the outcomes of each play, especially those of the computer.
