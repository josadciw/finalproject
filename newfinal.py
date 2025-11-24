import random
import string
import re
import os
import webbrowser  # Required for opening the browser in Feature 3

# Final Project: Deadpool Encryption Tool
# This script includes three features: Encryption, Password Generation, and OSINT Scanning.

# Get the directory where this script is running to ensure files are saved correctly
script_folder = os.path.dirname(os.path.abspath(__file__))

# Define the filenames for the test files
file1_path = os.path.join(script_folder, "test1.txt")
file2_path = os.path.join(script_folder, "test2.txt")


# Function to automatically create the text files needed for the project
def create_test_files():
    print(f"\n[System] Current working folder: {script_folder}")

    # Create test1.txt with dummy data for the OSINT scanner to find
    f = open(file1_path, "w")
    f.write("Target: Francis / Ajax\n")
    f.write("Contact Email: francis@badguy.com\n")
    f.write("Standard Phone: 555-867-5309\n")
    f.write("Phone with spaces: (555) 123 4567\n") 
    f.write("Short Phone: 555-0199\n")
    f.write("Phone with dots: 123.456.7890\n")
    f.close()
    print("test1.txt created/updated successfully.")

    # Create test2.txt to be used for the Encryption feature
    if not os.path.exists(file2_path):
        f = open(file2_path, "w")
        f.write("The secret stash is hidden under the floorboards.")
        f.close()
        print("test2.txt created successfully.")


# Feature 1: Substitution Cipher (Encrypts and Decrypts text)
def feature_cipher():
    print("\n--- Deadpool's File Scrambler ---")
    
    # Define the standard alphabet and the shifted key for substitution
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key      = "defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC"

    # Ask the user for the mode
    mode = input("Select: (1) Encrypt or (2) Decrypt: ")
    
    # Ask the user for the source of the text
    source = input("Source: (1) Manual Input or (2) Read 'test2.txt': ")
    
    text_content = ""

    if source == "1":
        # Multiline Input Support
        print("Enter text (Press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        # Join the lines back together with newline characters
        text_content = "\n".join(lines)
    else:
        # Check if file exists before reading
        if os.path.exists(file2_path):
            f = open(file2_path, "r")
            text_content = f.read()
            f.close()
        else:
            print("Error: test2.txt missing.")
            return

    # Loop through each character to encrypt or decrypt it
    final_text = ""
    for char in text_content:
        if char in alphabet:
            # If mode is 1, we encrypt (shift forward using key)
            if mode == "1":
                 index = alphabet.find(char)
                 final_text += key[index]
            # If mode is 2, we decrypt (reverse using alphabet)
            else:
                 index = key.find(char)
                 final_text += alphabet[index]
        else:
            # If character is not a letter (like a space or number), keep it as is
            final_text += char

    # Display the result
    print(f"\n--- RESULT ---\n{final_text}\n--------------")
    
    # Ask if the user wants to save the result to a new file
    if input("Save to file? (y/n): ") == 'y':
        name = input("Enter filename: ")
        f = open(os.path.join(script_folder, name), "w")
        f.write(final_text)
        f.close()
        print("File saved.")
    
    input("Press Enter to return...")


# Feature 2: Password Generator
def feature_password():
    print("\n--- Password Generator ---")
    
    # Get the desired length from the user (validation loop)
    length = 0
    while length < 8:
        try:
            length = int(input("Enter length (min 8): "))
        except:
            pass # Ignore non-number inputs and loop again

    # Ask for character types
    use_upper = input("Include Uppercase? (y/n): ") == 'y'
    use_lower = input("Include Lowercase? (y/n): ") == 'y'
    use_nums  = input("Include Numbers? (y/n): ")   == 'y'
    use_syms  = input("Include Symbols? (y/n): ")   == 'y'

    # Ensure at least lowercase is selected if user picked nothing
    if not (use_upper or use_lower or use_nums or use_syms):
        use_lower = True

    # Build the list of allowed characters
    chars = ""
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_nums:  chars += string.digits
    if use_syms:  chars += string.punctuation

    # Generate the random password
    password = ""
    for i in range(length):
        password += random.choice(chars)

    print(f"\nGenerated Password: {password}")
    
    # Option to save the password
    if input("Save to file? (y/n): ") == 'y':
        f = open(os.path.join(script_folder, "pass.txt"), "w")
        f.write(password)
        f.close()
        print("Saved to pass.txt")
        
    input("Press Enter to return...")


# Feature 3: OSINT Scanner (Finds emails/phones OR searches Social Media)
def feature_osint():
    print("\n--- Target Scanner (OSINT) ---")
    print("Select Operation:")
    print("1. Scan Local File (Emails/Phones)")
    print("2. LinkedIn Recon")
    print("3. Facebook Search")
    print("4. X (Twitter) Search")  # <--- NEW
    print("5. Instagram Search")    # <--- NEW
    
    op_choice = input("Choice: ")

    # --- OPTION 1: SCAN LOCAL FILE ---
    if op_choice == "1":
        print("\n[File Scanner Selected]")
        print("1. Default (test1.txt)")
        print("2. Custom File Path")
        choice = input("Choice: ")

        # Set the file path based on user choice
        target_file = file1_path

        if choice == "2":
            raw_path = input("Enter the full file path to scan: ")
            # .strip() removes extra spaces and quotation marks often added by 'Copy Path'
            target_file = raw_path.strip().strip('"').strip("'")

        # Verify the file exists
        if not os.path.exists(target_file):
            print(f"Error: The file '{target_file}' is missing. Target lost.")
            return

        # Open and read the file content
        try:
            f = open(target_file, "r", encoding='utf-8', errors='ignore')
            content = f.read()
            f.close()
        except Exception as e:
            print(f"Error reading file: {e}")
            return

        # Display content for verification (truncated if too long)
        print("\nFile Contents (Preview):")
        print("------------------------------")
        print(content[:500] + ("..." if len(content) > 500 else ""))
        print("------------------------------")

        # Regex pattern for Email addresses
        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        
        # Regex pattern for Phone numbers
        phone_regex = r'[\d\-\(\)\.\s]{7,}'

        # Find matches and remove duplicates using set()
        emails = list(set(re.findall(email_regex, content)))
        raw_phones = list(set(re.findall(phone_regex, content)))

        # Filter phone numbers to ensure they have enough digits
        valid_phones = []
        for p in raw_phones:
            # Count actual digits in the string
            digit_count = 0
            for char in p:
                if char.isdigit():
                    digit_count += 1
            
            # Only keep it if it looks like a real number (5+ digits)
            if digit_count >= 5:
                valid_phones.append(p.strip())

        # Display findings
        print(f"\nEmails Found: {len(emails)}")
        for e in emails: print(f"- {e}")

        print(f"\nPhones Found: {len(valid_phones)}")
        for p in valid_phones: print(f"- {p}")

        # Save the report to a file
        if input("\nSave report? (y/n): ") == 'y':
            f = open(os.path.join(script_folder, "scan_report.txt"), "w")
            f.write(f"Source: {target_file}\n")
            f.write(f"Emails: {emails}\nPhones: {valid_phones}")
            f.close()
            print("Report saved.")

    # --- SOCIAL MEDIA SEARCH HELPER ---
    elif op_choice in ["2", "3", "4", "5"]:
        target_name = input("\nEnter the name of the target: ")
        
        site = ""
        site_name = ""
        extra_query = ""
        
        if op_choice == "2":
            site = "linkedin.com"
            site_name = "LinkedIn"
            extra_query = input("Enter company/keyword (optional): ")
        elif op_choice == "3":
            site = "facebook.com"
            site_name = "Facebook"
            extra_query = input("Enter city/keyword (optional): ")
        elif op_choice == "4":
            site = "twitter.com"
            site_name = "X (Twitter)"
            extra_query = input("Enter handle/keyword (optional): ")
        elif op_choice == "5":
            site = "instagram.com"
            site_name = "Instagram"
            extra_query = input("Enter handle/keyword (optional): ")

        print(f"\n[{site_name} Recon Selected]")
        
        # Construct the Google Dork query
        search_query = f'site:{site} "{target_name}" {extra_query}'
        
        print(f"Searching for: {search_query}")
        print("Opening browser... maximum effort!")
        
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        
    else:
        print("Invalid choice.")

    input("\nPress Enter to return...")


# Main Menu Loop
def main():
    # Initialize the test files when program starts
    create_test_files()

    while True:
        print("\n=== DEADPOOL TOOL ===")
        print("1. Encrypt/Decrypt")
        print("2. Password Gen")
        print("3. OSINT Scanner")
        print("4. Exit")
        
        c = input("Choice: ")
        
        if c == "1": 
            feature_cipher()
        elif c == "2": 
            feature_password()
        elif c == "3": 
            feature_osint()
        elif c == "4": 
            break
        else: 
            print("Invalid selection.")

# Run the main function
if __name__ == "__main__":
    main()
