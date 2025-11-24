# finalproject
Final Project: Deadpool Encryption Tool

About My Project

For my final project, I created the Deadpool Encryption Tool. I wanted to build something that felt like a "spy tool" but also demonstrated the coding concepts we learned in class, like file handling, loops, and Regular Expressions (Regex).

The idea is that this is tool is for basic cybersecurity tasks: scrambling messages so they can't be read, generating strong passwords, and scanning files to find hidden contact info.

What It Does

I built three main features into this script:

1. The Scrambler (Encrypt/Decrypt)

I wrote a custom substitution cipher that shifts letters around.

How it works: You can type in a message manually or have it read automatically from a text file.

Why I made it: I wanted to show how strings can be manipulated and mapped to different characters.

2. Password Generator

This feature creates random, secure passwords.

How it works: It asks you for the length (I set a minimum of 8 for safety) and whether you want uppercase letters, numbers, or symbols.

Why I made it: To practice using the random library and input validation (making sure the user enters a valid number).

3. OSINT Scanner (The "Target" Finder)

This is probably the most complex part. It scans a text file to find email addresses and phone numbers.

How it works: It uses Regex patterns to look through a file. I made sure it can handle different phone formats (like ones with dots 555.123.4567 or parentheses).

Why I made it: To demonstrate how Python can parse through big blocks of text to find specific data patterns.

How to Run It

You don't need to install anything extra; I only used standard Python libraries (os, re, random, string).

Download newfinal.py.

Open your terminal/command prompt in that folder.

Run the script:

python newfinal.py


A Note on Test Files

To make this easy to grade/test, I wrote the script to automatically create its own test files.

When you run the program, it checks if test1.txt and test2.txt exist. If they don't, my code creates them for you immediately.

test1.txt will have dummy data for the Scanner to find.

test2.txt will have a secret message for the Encryptor to read.

How to Use the Menu

When you start the tool, just type the number for the feature you want:

Option 1 (Encryption): If you pick this, you can choose to encrypt a file. If you save the result, it creates a new file so the original isn't lost.

Option 2 (Passwords): Just follow the prompts. You can save your new password to pass.txt.

Option 3 (Scanner): You can choose "Default" to scan the test file I created, or "Custom" to paste in a path to any file on your computer.

Files Included

newfinal.py: My source code.

scan_report.txt: The program creates this if you save your scan results.

pass.txt: The program creates this if you save a password.
