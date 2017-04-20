# battleship
In order to execute this program, one need the following: 
- Python 2.7 installed

To run the battleship program, enter the following command: 

`python Run.py`

Tests can be executed with the following command: 

`python -m unittest Battleshiptests`

The program is implemented with optional sleep functionality, to slow down the game speed. 
In order to adjust the game speed, please change the line 
`run.run_battleship(0)` in `Run.py` to a speed(measured in seconds) i.e `run.run_battleship(1)`

When the program is executing. The output is printed in `battleship.log`
To get a live output of the gameplay with a game speed= 1 move per second. Do the following: 

1. Make sure that the run_battleship function call in Run.py is set to run.run_battleship(1)
2. Go to the program directory and execute the program.  
    - `cd ~/src/main/`
    - `python Run.py`    
3. Tail the battleship log file to get live output
    - `tail -f battleship.log`





