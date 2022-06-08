## Overview
This implements a tiny command-line (CLI) application that calculates the ranking table for a league. The rules for calculating the position on the table are similar to that obtainable with football (a.k.a. soccer) leagues: a draw (tie) is worth a point and a win 3 points, while a loss earns 0 points.

Certainly, teams with the highest points appear higher in the league table, but to simplify the rules if two or more teams have the same number of points, they would be displayed in the table in alphabetical order.

## Build and Run the App Locally
I've also implemented integration with SetupTools to simplify the commands available from the app and make the app more portable. Once cloned to your machine, enter the following at the root of your project directory:
```
pip install --editable .
```
You may then familiriase yourself with the commands and options available with the app by entering the following command at the root of your project directory:
```
leaguetable --help
```
and you should see the following output:
```
Usage: leaguetable [OPTIONS]

  Reads a file or individual input containing match scores and then computes
  and outputs the resulting league table.

Options:
  -f, --scores-file FILENAME  Select a file containing scores, in seperate
                              lines, for several matches.
  -s, --scores TEXT           Enter individual match scores, each with this
                              flag.
  -o, --file-output FILENAME  File to write table to. Omit this flag to just
                              display the league table on screen.
  --help                      Show this message and exit.
  ```

## Input
Specifically, the options for submitting scores into the app are follows:
1. Using the `-s` or `--scores` option, like so:
```
leaguetable --scores "Shalke FC 32, City 42" -s "Lions 3, Snakes 3" -s "Tarantulas 1, FC Awesome 0" -s "Lions 1, FC Awesome 1" -s "Tarantulas 3, Snakes 1" -s "Lions 4, Grouches 0"
```
Similarly, you can submit the scores as a text file, say `scores.txt`, with each match score on seperate lines like so:
```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
Shalke FC 32, City 42
```
and passed to the app:
```
leaguetable -f scores.txt
```

## Output
Submitting the commands above will result in the following displayed in the terminal:
```
League Table:

1. Tarantulas, 6 pts    
2. Lions, 5 pts    
3. City, 3 pts    
4. FC Awesome, 1 pt     
5. Snakes, 1 pt     
6. Grouches, 0 pts    
7. Shalke FC, 0 pts
```
If you prefer this output to be written to a file, you will need to include the `-o` or `--file-output` option to the command while indicating/selecting an accessible and writable file on your file system, like so:
```
leaguetable --scores "Shalke FC 32, City 42" -s "Lions 3, Snakes 3" -s "Tarantulas 1, FC Awesome 0" -s "Lions 1, FC Awesome 1" -s "Tarantulas 3, Snakes 1" -s "Lions 4, Grouches 0" -o outputfile.txt
```
or:
```
leaguetable -f scores.txt -o outputfile.txt
```
## Input Precedence
If you provide both a `--scores-file` file and a `--scores` text input options to the app in one command, the `--scores-file` file will be accepted while the `--scores` input ignored.

## Unit Tests
I've also bundled unit tests in the code base, which you can exercise with the command:
```
py.test -vv
```
