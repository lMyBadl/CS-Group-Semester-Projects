1. Project Setup
    - [x] Install Python and Pygame.
    - [x] Create a project folder with the following structure:
    - [ ] /assets: Store card images, sounds, and fonts.
    - [ ] /src: Python scripts for game logic and UI.

2. Game Logic
    Card and Deck Management:
    - [ ] Create a Card class for attributes like rank, suit, and value.
    - [ ] Create a Deck class to generate multiple decks (depending on the level).
    - [ ] Implement functions to shuffle, deal, and manage the deck.

    (Follow Wikipedia page for game logic and then add options for "home" rules)
    Trump Suit Logic:
    - [ ] Define logic to set the trump suit dynamically based on the starting card or current round rules.
    
    Player and Team Setup:
    - [ ] Create Player and Team classes to track players' hands, scores, and tricks won.
    - [ ] Assign players to teams (opposite players form teams).

    Trick    -Taking Mechanics:
    - [ ] Define rules for valid plays (following suit, trumping, etc.).
    - [ ] Implement logic to determine the winner of each trick.

    Scoring and Progression:
    - [ ] Track the number of tricks won by each team.
    - [ ] Implement the promotion/demotion system (levels) based on points scored.
    - [ ] Handle the special cards (2s, Jokers) and their effects on gameplay.

3. User Interface (UI)
    Game Table:
    - [ ] Design a visual table layout for 4 players.
    - [ ] Display each player’s cards and the current trick on the table.

    Card Display:
    - [ ] Load card images for all ranks and suits.
    - [ ] Add animations for dealing cards and playing tricks.

    Player Actions:
    - [ ] Allow players to select cards from their hand.
    - [ ] Add buttons for actions like "Play," "Pass," or "End Turn."

    Scoreboard and Level Display:
    - [ ] Show the current scores, tricks won, and player/team levels.

    Game Messages:
    - [ ] Display messages for turn indicators, invalid moves, and round results.

4. Gameplay Flow
    Start New Game:
    - [ ] Initialize players, teams, and the deck.
    - [ ] Deal cards to players and determine the initial trump suit.

    Rounds and Turns:
    - [ ] Implement the turn order for 4 players.
    - [ ] Manage the flow of each trick (playing cards, validating moves, determining trick winner).

    Round End:
    - [ ] Calculate the winning team of the round.
    - [ ] Update scores and levels based on the number of tricks won.

    Game End:
    - [ ] Set conditions for when the game ends (e.g., a team reaching a certain level or score).

5. Multiplayer Functionality (Optional)
    - [ ] Add local multiplayer support for 4 players on one machine.

    Implement online multiplayer:
    - [ ] Use Python's socket library to create a server    -client model.
    - [ ] Enable real    -time gameplay for remote players.

6. Audio and Visual Effects
    - [ ] Add sound effects for:
    - [ ] Dealing cards.
    - [ ] Playing cards.
    - [ ] Winning/losing tricks.

    Implement animations:
    - [ ] Smooth transitions for cards played.
    - [ ] Highlight the current trick's winning card.

7. Game State Management
    Save/Load Game:
    - [ ] Implement functionality to save the game state and load it later.

    Pause/Resume Game:
    - [ ] Add a pause menu with options to resume or quit.

8. Testing and Debugging
    Test individual components:
    - [ ] Card generation and dealing.
    - [ ] Valid move checks.
    - [ ] Trick    -winning logic.

    Debug UI elements:
    - [ ] Ensure smooth interactions and transitions.
    - [ ] Verify correct card displays and animations.

    Playtest:
    - [ ] Run the game multiple times to ensure rules and progression work as intended.

9. Documentation
    - [ ] Write clear inline comments in the code.

    Create a README with:
    - [ ] Game rules for Sheng Ji.
    - [ ] Instructions to run the program.
    - [ ] Features and screenshots.

10. Polish and Optimization
    Add a main menu:
    - [ ] Options for new game, instructions, and exit.

    Create an end    -game screen:
    - [ ] Display the winning team and final scores.

    Optimize performance:
    - [ ] Ensure smooth animations and gameplay.

    Package the game:
    - [ ] Use tools like PyInstaller to create an executable.
