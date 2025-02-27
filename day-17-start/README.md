# Quiz Game Application

## **[100 Days of Code: The Complete Python Pro Bootcamp for 2025](https://www.udemy.com/course/100-days-of-code/)**

By Dr. Angela Yu

*Day 17 of 100:* Quiz Game with Object-Oriented Programming

## Project Overview

This project implements a simple quiz game application using Object-Oriented Programming (OOP) principles. The application loads true/false questions from a data file, presents them to the user, and tracks their score throughout the quiz.

### Key Features

- **Modular Structure**: The application is organized into separate classes with distinct responsibilities
- **Question Model**: Represents individual questions with their text and correct answers
- **Quiz Brain**: Handles the logic of presenting questions and checking answers
- **Data Source**: Questions are loaded from a structured data file
- **Score Tracking**: Keeps track of correct answers and provides feedback after each question

### Components

- `question_model.py`: Defines the Question class to store question text and answers
- `quiz_brain.py`: Contains the QuizBrain class that manages the quiz logic
- `data.py`: Stores the question data in a structured format
- `main.py`: Entry point that initializes and runs the quiz

### How It Works

1. The application loads questions from the data file
2. Each question is presented to the user who inputs a True/False answer
3. The application checks the answer and provides immediate feedback
4. After all questions are answered, the final score is displayed