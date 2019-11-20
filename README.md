# Bowling Alley

## Problem Trying to Solve
Design the entire bowling alley system. One bowling game will be played by multiple players on one lane. During the game, players and their scores will be maintained and shown by the system and winner will be declared at the end of the game. Likewise multiple games can played in parallel on multiple lanes.

![bowling](https://user-images.githubusercontent.com/45592052/69250835-6b571f00-0bd6-11ea-865b-3cc584a26e15.jpg)

### Some rules about Bowling -
- A game consists of ten (10) sets as shown in the attachment.
- In each set, the player has two opportunities to knock down ten (10)pins.
- The score for a set is the total number of pins knocked down, plus bonuses for strikes and spares.
- A spare(depicted by ‘/‘) is when the player knocks down all ten (10) pins in two tries. If there is a spare the player gets 5 bonus points.
- A strike(depicted by ‘X’) is when the player knocks down all ten (10) pins on his/her first try. If there is a strike the player gets 10 bonus points. If the person knocks down all the 10 pins in the second try,it should be considered a spare.
- In the final (10th) set an player who rolls a spare or strike is allowed to roll one extra balls to complete the set. However only a maximum of three balls can be rolled in the final set.

#### Example:
- In the attachment the player knocks 1 pin in first try and 4 in second try in the first set and the total score is 5.
- In the second set the player knocks 4 pins in first try and 5 in second try and the cumulative score is 14.
- In the third set the player knocks 6 pins in first try and the remaining 4 in second try (a spare indicated by the symbol “/“) and the cumulative score is 29 (14+10+5 bonus).
- In the forth set the player knocks 5 pins in first try and the remaining 5 in second try (a spare indicated by the symbol “/“) and the cumulative score is 44 (29+10+5 bonus).
- In the fifth set the player knocks down all 10 pins in first try(a strike indicated by the symbol “X“) and the cumulative score is 64 (44+10+10 bonus).
- In the final set the player knocks 2 in first try and the remaining 8 in second attempt (spare indicated by “/“). The player is allowed to roll an extra ball and this time knocks down 6 pins
- So In the final set he gets 21(10+5+6) points and the total tally is 136 points.

#### Points for Consideration:
- Make sure you code is modular & extensible and follows OOP best practices - good set of classes and separation of concerns.
- For the purposes of the implementation, you can use a random number between 0 to 10 to  simulate  the  score  of  each  attempt  by  the player.
- We should be able to easily plugin different strategies for score calculation. e.g. We should be able to add more strategies like strike and spare.


## Setup
```
git clone https://github.com/akshaybabu09/bowlingalley.git
cd bowlingalley
sudo apt-get update
sudo apt-get install python3.6
python3 -m venv venv
source venv/bin/activate
```

## Running the Program
```
python3 bowling_alley.py
```

## Execution Flow

Once you run the above command you will be asked a few questions.
1. Do you wish to add a new strategies? Please respond with a **Yes** or a **No**
    If **Yes**
        You will be asked the following:
        a. The number of strategies you want to add.
        b. The condition for the strategy.
        c. The bonus value.
        
![include_strategy](https://user-images.githubusercontent.com/45592052/69254938-f9ce9f00-0bdc-11ea-9ed0-d0c295eaa07a.png)
    
2. Enter the Number of Players: **X**
3. The names of those **X** players
```
Player Id, Name & Score of each player will be displayed.

The winner name will also be displayed.
```
![players_scores](https://user-images.githubusercontent.com/45592052/69255897-9b0a2500-0bde-11ea-98d1-3ccacd8fd7c6.png)

4. Do you wish to view scores of each set of every player? Please respond with a **Yes** or a **No**
    
    If **Yes**
    
        Player Name
        
        Set 1:
        Trial 1: P Points
        Trial 2: Q Points
        Set Outcome: P + Q Points
        
        Set 2:
        Trial 1: P Points
        Trial 2: Q Points
        Set Outcome: P + Q Points
        
        Set 3:
        Trial 1: P Points
        Trial 2: Q Points
        Set Outcome: P + Q Points
        
        Set 4:
        Trial 1: P Points
        Trial 2: Q Points
        Set Outcome: P + Q Points
        
        Set 5:
        Trial 1: P Points
        Trial 2: Q Points
        Set Outcome: P + Q Points
        
        Set 6:
        Trial 1: P Points
        Trial 2: Q Points
        Set Outcome: P + Q Points
        
        Set 7:
        Trial 1: P Points
        Trial 2: Q Points
        Set Outcome: P + Q Points
        
        Set 8:
        Trial 1: P Points
        Trial 2: Q Points
        Set Outcome: P + Q Points
        
        Set 9:
        Trial 1: P Points
        Trial 2: Q Points
        Set Outcome: P + Q Points
        
        Set 10:
        Trial 1: P Points
        Trial 2: Q Points
        Trial 3: S Points
        Set Outcome: P + Q Points
                
        Final Score: R Points
        
        
        Note: In the 10th Set if the player scores a strike or a spare then he/she will get a bonus try.

![ramesh](https://user-images.githubusercontent.com/45592052/69256564-a6aa1b80-0bdf-11ea-9981-c62a5f86f0d9.png)                    ![suresh](https://user-images.githubusercontent.com/45592052/69256574-ac9ffc80-0bdf-11ea-8628-23e9288873ee.png)

## Explanation

1. The points scored in a try is generated randomly using *randint()*.
    - For trial 1 the random number will be generated between 0 & 10.
    - For trial 2 the random number will be generated between 0 & (10 - points in trial 1)
    - In case of trial 3 the random number will be generated similar to that of trail 1.

2. The Player details such as PlayerId, Name, Set Scores, Final Score are stored in a dictionary.
    - In case of a multiplayer game, a list of dictionaries is maintained.

3. The strategies are stored in the form of a dictionary of dictionaries.
    - Default Strategies
      > {"strike":{"condition":"trial_1 == 10","bonus":10},"spare":{"condition":"(trial_1 + trial_2) == 10","bonus":5}}
    
    - After Including 1 strategy in the above example
      > {'strike': {'condition': 'trial_1 == 10', 'bonus': 10}, 'spare': {'condition': '(trial_1 + trial_2) == 10', 'bonus': 5}, 'XYZ': {'condition': 'trial_1 + trial_2 == 9', 'bonus': 1}}

# Thank You!
