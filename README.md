# Ball Sort Puzzle Game

A command-line implementation of the classic Ball Sort Puzzle game built using Python.

## Features

* Move balls between tubes following puzzle rules
* Color-based move validation
* Tube capacity constraints
* Win condition detection
* Input validation for source and destination tubes
* Interactive command-line gameplay

## Game Rules

1. Only the top ball of a tube can be moved.
2. A ball can be moved to:

   * An empty tube, or
   * A tube whose top ball has the same color.
3. A tube cannot exceed its maximum capacity.
4. The objective is to sort all balls so that each tube contains balls of only one color.

## Technologies Used

* Python
* Lists (Stack Data Structure)
* Functions
* Conditional Logic
* Exception Handling

## Future Enhancements

* OpenCV graphical interface
* MediaPipe hand gesture controls
* Multiple difficulty levels
* Move counter and timer
* Hint system
