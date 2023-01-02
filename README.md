# Snake

The classic game Snake implemented in Python.

## Description

Eat as much fruit as you can without eating yourself! Be careful, eating makes you grow.

## Todo
    * No game over yet, just reset snake and fruit
    * Add a score for each fruit
    * Clean up snake creation in Snake init() call a method on win that creates the snake
    * Remove some unused variables in snake/segment i.e. index, tail
    * Refactor the move_head in segment
    * Clean up class properties, some have _ but are accessed outside class
    * Checking the fruit x y % 20 == 0 is very inefficent, fix the randomint call
        so it only generates %20 == 0 results
    * Might be because of this that fruit still spawns on snake body

## Getting Started

### Dependencies

* None

### Executing program

Can only be run from source code right now, using main.py

## Authors

Ryan Day 

## Acknowledgments

* Readme template: [README-Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
