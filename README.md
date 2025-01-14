# Card Counting Application

This is a simple card counting application built with Python using the `Tkinter` library. It helps in calculating the running and true count for card counting techniques used in blackjack. The two card counting systems implemented are **Hi-Opt II** and **Hi-Lo**.

## Features

- **Card Counting Systems**: Choose between Hi-Opt II or Hi-Lo card counting techniques.
- **Running and True Count**: Automatically calculates the running count and true count based on the selected system.
- **Deck Penetration**: Displays the current deck penetration percentage, which helps in determining how many decks have been dealt.
- **Ace Count (Hi-Opt II)**: Shows the expected and actual aces dealt in Hi-Opt II.
- **Card History**: Tracks the last 20 cards dealt.
- **Deck Count Selection**: Allows the user to set the number of decks used in the game (1 to 8 decks).
- **Reset Functionality**: Resets all counts and settings.

## Requirements

- Python 3.x
- Tkinter (usually comes with Python)

## How to Use

1. **Install Python**: If you don't already have Python installed, download and install it from [python.org](https://www.python.org/).
2. **Run the Script**: Open a terminal or command prompt, navigate to the directory where the script is located, and run the following command:
   ```bash
   python card_counter.py
