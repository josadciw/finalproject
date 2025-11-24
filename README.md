# finalproject
Deadpool Encryption Tool

Hi! This is my final project. I built a Python tool inspired by Deadpool that handles a few different security tasks. It is designed to be a "Swiss Army knife" for basic encryption and recon.

What it does

I packed three main features into this script:

1. File Scrambler (Encrypt/Decrypt)

This tool lets you hide messages so others can't read them.

Encrypt: You type in text (it supports multiple lines now!) or load it from a file, and the script scrambles the letters using a substitution cipher.

Decrypt: You can turn the scrambled text back into readable English.

It automatically saves your secret messages to a file if you want.

2. Password Generator

Stop using "password123"!

This feature creates strong, random passwords for you.

The user input for the password generator is number input only (to define the length).

It then generates the password using the specified input you decided.

3. OSINT Scanner (The Recon Tool)

This is for gathering information ("Open Source Intelligence"). It has two modes:

Local Scan: You give it a text file, and it digs through it to find and list any Email Addresses or Phone Numbers hiding inside.

Social Media Search: You enter a target's name, and the script opens your web browser to search for their profiles on LinkedIn, Facebook, X (Twitter), and Instagram. It uses Google "dorks" to find the specific profiles without needing to log in.

How to use it

Make sure you have Python installed.

Download the newfinal.py file.

Run it in your terminal or command prompt:

python newfinal.py


Follow the menu options on the screen!

Note

The script automatically creates some dummy files (test1.txt and test2.txt) in the same folder so you can test out the features right away without needing your own files.

Disclaimer: This is for educational purposes only. Don't use the OSINT scanner to be a creep.
