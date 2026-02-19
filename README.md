# Python Learning Repository
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/maidla63/Python)

This repository is a collection of Python scripts developed as part of a programming course. The files demonstrate a progression of learning, covering fundamental concepts, graphical drawing, file operations, and a simple game. The comments and some variable names are in Estonian.

## Key Features

*   **Core Python Concepts:** Scripts cover fundamental topics including variables, data types, loops (`for`), conditional statements (`if/else`), functions, lists, and dictionaries.
*   **Turtle Graphics:** Extensive use of the `turtle` module to create various drawings, such as geometric patterns, a flower (`nr0.2.1.1.py`), the Olympic rings (`nr02.py`), and creative visualizations.
*   **File Handling:** The `ylikooli yl/` directory contains exercises focused on reading data from `.txt` files to perform tasks like processing lists of names, music tracks, and financial data.
*   **Interactive Scripts:** Many scripts are interactive, prompting the user for input to perform calculations, select options, or control the behavior of the program.
*   **Simple Game:** `nr15.py` is a complete, playable Pong-style game built with the `turtle` module. It features scoring, keyboard controls for the paddle, and increasing difficulty as the score rises.
*   **System Operations:** The `nr17.py` script demonstrates using the `os` and `datetime` modules to interact with the file system, creating directories based on the current date.

## Repository Structure

The repository is organized into the following sections:

*   **Root Directory**: Contains a series of numbered exercises (`nr01.py` - `nr17.py`) that build on each other in complexity. It also includes review scripts like `Kordamine2.py`.
*   **`E õpe/`**: A folder with additional `turtle` graphics exercises.
*   **`ylikooli yl/`**: Contains scripts for university-level assignments that primarily focus on file I/O. This directory also houses the `.txt` data files required by these scripts.

## Usage

Each Python script is self-contained and can be run from the command line.

```bash
# Navigate to the repository directory
cd maidla63-python

# Run a script from the root directory
python nr15.py

# Run a script from a subdirectory
python "ylikooli yl/nr03.1.py"
```

Note that scripts within the `ylikooli yl/` directory are designed to read data from accompanying `.txt` files within the same folder.