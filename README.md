# Flash Card Language Learner

An interactive flash card application designed to help users learn a new language through active recall. Built with Python using Tkinter for the GUI and Pandas for data management, this app presents words in a foreign language and flips to reveal the translation, allowing users to self-assess their knowledge.

## Live Demo

![Flash Card App Demo](demo.gif)

## Key Features

-   **Active Learning:** Users are shown a French word and must recall the English translation. The card automatically flips after 3 seconds to reveal the answer.
-   **Progress Tracking:** If the user knows the word (clicks the "right" button), that word is removed from the current learning deck and saved to a separate `french_words_known.csv` file. This ensures they are only tested on words they haven't yet mastered.
-   **Data Persistence:** The application saves your progress. When you restart the app, it will only use the words you still need to learn.
-   **Restart Functionality:** A dedicated "Restart" button allows the user to reset their progress, merging all known words back into the main learning deck.
-   **Data-Driven:** The flash cards are generated from a `french_words.csv` file, making it easy to expand the vocabulary or even change the language being studied.

## Project Setup

To run this application on your local machine, follow these steps.

### Prerequisites

-   Python 3.x
-   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dheerajdhami2001-cyber/flash_card_project.git
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd flash_card_project
    ```

3.  **Install the required dependency:**
    The project uses the Pandas library for managing the vocabulary data.
    ```bash
    pip install pandas
    ```

4.  **Run the application:**
    ```bash
    python main.py
    ```

## How It Works

-   **`main.py`**: The main script containing the application's logic.
    -   **Card Shuffle (`shuffle`)**: Randomly selects a word from `data/french_words.csv`. It displays the French word and uses a `window.after()` timer to automatically flip the card to the English translation after 3 seconds.
    -   **Progress Management (`right_clicked`)**: When the user indicates they know a word, it is removed from the primary CSV file and appended to `french_words_known.csv`. This prevents the word from appearing again in the current session.
    -   **Restart Logic (`restart`)**: Merges the words from `french_words_known.csv` back into `french_words.csv` and clears the "known words" file, effectively resetting the learning deck.
    -   **UI**: The interface is built with Tkinter, using a `Canvas` to display the flipping card images and `Buttons` for user interaction.

## Acknowledgments

This project was inspired by and completed with the guidance of the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)** by Dr. Angela Yu.
