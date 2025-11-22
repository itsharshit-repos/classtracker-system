# ClassTrack: Student Academic Performance Analyzer

## Overview
ClassTrack is a Python-based desktop application designed to help university students track, analyze, and visualize their academic performance. Unlike standard grade cards, it provides visual analytics to identify growth trends and compares individual performance against the class average.

## Features
* **GPA Calculation:** Automatically computes weighted SGPA based on credits and marks.
* **Visual Analytics:** Generates dynamic line graphs to visualize academic growth over semesters.
* **Peer Comparison:** Allows students to benchmark their performance against a friend (Head-to-Head).
* **Class Benchmarking:** Compares personal performance with the overall class average.
* **Future Prediction:** Uses trend analysis to predict the next semester's likely GPA.

## Technologies Used
* **Language:** Python 3.13
* **Data Analysis:** Pandas (for CSV handling and filtering)
* **Visualization:** Matplotlib (for rendering line and bar charts)
* **Storage:** CSV (Offline, persistent storage)

## Code Structure
The project is organized into modular files for better maintainability:
* **`src/main.py`**: The entry point of the application. Handles the CLI menu and user inputs.
* **`src/data_manager.py`**: Handles all file operations (reading/writing to `student_marks.csv`).
* **`src/grade_analyzer.py`**: Contains the logic for weighted GPA calculation and predictive analysis.
* **`src/visualizer.py`**: Contains Matplotlib functions to generate and display graphs.
* **`data/student_marks.csv`**: Stores the student academic records.

## How to Run (Setup Instructions)
1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/itsharshit-repos/classtracker-system.git](https://github.com/itsharshit-repos/classtracker-system.git)



1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/itsharshit-repos/classtracker-system.git](https://github.com/itsharshit-repos/classtracker-system.git)
