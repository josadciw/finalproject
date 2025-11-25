# finalproject
Deadpool Encryption Tool (Final Project)
Welcome to my Final Project! This is a multi-purpose Python tool designed for "Maximum Effort." It helps you protect your secrets, generate uncrackable passwords, and scan for information on targets.

I wrote this script to be interactive, so just run it and follow the prompts on the screen!

What This Tool Does
1. The Cipher (Scrambler)
This feature takes normal text and scrambles it so nobody else can read it. It uses a custom alphabet key to swap letters.

Encrypt: Turns readable text into gibberish.

Decrypt: Turns the gibberish back into readable text.

Sources: You can type text manually, use the internal demo text, or load a text file from your computer.

2. Password Generator
Stop using "password123"! This tool builds a strong, random password for you.

You choose the length (minimum 8 characters).

You pick what to include: Uppercase, Lowercase, Numbers, and Symbols.

It saves the password to a file so you don't forget it.

3. The Scanner (OSINT)
This is the "Target Scanner." It looks through data to find contact information using specific patterns (Regex).

Data Scan: It reads through text and pulls out Emails and Phone Numbers. I fixed the code so it stops grabbing extra dots or weird characters at the end of emails.

Web Recon: You can pick a target name, and the tool will automatically open a Google search specifically for LinkedIn, Facebook, X (Twitter), or Instagram to find them.

How to Test It (Important!)
I have included a specific file called Vaderinfo.txt in this folder.

Use this file to test Feature 3 (The Scanner).

When the tool asks for a file path, enter the path to Vaderinfo.txt.

You will see how the tool ignores the junk text and extracts only the valid emails and phone numbers!

Improvements & Fixes
Custom Saving: I added a feature that lets you pick exactly where you want to save your files. You can type a specific folder path, or just hit Enter to save it in the default spot.

Regex Update: I updated the pattern matching so it catches phone numbers with dots (123.456.7890) but ignores random numbers that aren't phones.

How to Run
Make sure you have Python installed.

Open your terminal or command prompt.

Run the script:

Bash

python FinalProject.py
Follow the menu options (1, 2, or 3).

Note: Be careful when overwriting files—the tool will warn you if a file already exists!

Disclaimer: This is for educational purposes only. Don't use the OSINT scanner to be a creep.
