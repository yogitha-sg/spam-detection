# Spam Message Detection

## Description

This project detects whether a text message is Spam or Not Spam using basic Natural Language Processing techniques.

## Technologies Used

- Python
- Regular Expressions
- Natural Language Processing

## How It Works

The system checks the input message for commonly used spam-related keywords such as:

- win
- prize
- free
- offer
- urgent
- click
- reward

If multiple spam-related keywords are detected, the message is classified as Spam.

## How to Run

```bash
python spam_detection.py