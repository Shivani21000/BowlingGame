# BowlingGame
This project focuses on refactoring and debugging a bowling game implementation in Python. The goal is to improve the code's structure, readability, and maintainability while ensuring it correctly implements the rules of bowling.
Key Changes

Debugging
Corrected the strike condition to use the isStrike method instead of checking the frame index
1
.
Fixed a typo in the method name from stickeScore to strikeScore
1
.
Corrected the roll method to append pins to the rolls list instead of resetting it
1
.
Refactoring
Renamed the stickeScore method to strikeScore for consistency
1
.
Used more descriptive variable names like frame_index instead of frameIndex
1
.
Extracted scoring logic for strikes, spares, and open frames into separate methods
1
.
Test Cases
The project includes several test cases to ensure the correctness of the bowling game implementation:
Test Gutter Game: Verifies that a game with no pins knocked down scores zero.
Test All Ones: Ensures that knocking down one pin per roll results in a total score of 20.
Test One Spare: Confirms that a spare correctly applies bonus points from the next roll.
Test One Strike: Checks that a strike awards points plus bonuses from the next two rolls.
Test Perfect Game: Validates scoring for a perfect game (300 points).
Test All Spares: Confirms correct scoring when every frame results in a spare.
Test Mixed Game: Tests various combinations of strikes, spares, and open frames to ensure comprehensive scoring accuracy.