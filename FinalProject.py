import random
import string
import re
import os
import webbrowser

# My Final Project: Deadpool Encryption Tool
# I added a feature to let the user pick exactly where to save files.
# I also fixed the regex so it stops grabbing extra dots in emails and phone numbers.

# This gets the folder where this script is running
script_folder = os.path.dirname(os.path.abspath(__file__))

def get_save_path(default_path):
    # This function asks the user if they want to use a custom path
    print(f"Default path: {default_path}")
    
    # I use strip to remove extra spaces or quotes if they paste a path
    user_input = input("Enter full path (or press Enter to use default): ").strip().strip('"').strip("'")
    
    if user_input:
        # If they only typed a folder name, I need to add the filename to it
        if os.path.isdir(user_input):
            return os.path.join(user_input, os.path.basename(default_path))
        return user_input
    
    # If they didn't type anything, just use the default
    return default_path

def check_overwrite(file_path):
    # This checks if a file already exists so we don't accidentally delete it
    if os.path.exists(file_path):
        print(f"[Warning] The file '{file_path}' already exists.")
        confirm = input("Overwrite it? (y/n): ")
        if confirm.lower() != 'y':
            print("Operation canceled. File was NOT saved.")
            return False # Return False so we know not to save
    return True # Return True if it's safe to save

# Feature 1: The Cipher (Scrambler)
def feature_cipher():
    print("\n--- Deadpool's File Scrambler ---")
    
    # My simple alphabet strings for substitution
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key      = "defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC"

    mode = input("Select: (1) Encrypt or (2) Decrypt: ")
    
    print("\nSource:")
    print("1. Manual Input (Type text now)")
    print("2. Internal Demo Text")
    print("3. External File (Input a file path)")
    source = input("Choice: ")
    
    text_content = ""
    file_path_in = "" 

    # Check which source the user picked
    if source == "1":
        # Let the user type until they hit enter on an empty line
        print("\n[Manual Mode] Enter text below (Press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        text_content = "\n".join(lines)

    elif source == "2":
        # Load the hardcoded text
        print("\n[System] Loading internal demo text...")
        if mode == "1":
            text_content = "The secret stash is hidden under the floorboards."
        else:
            text_content = "Wkh vhfuhw vwdvk lv klgghq xqghu wkh iooruerdugv."

    elif source == "3":
        # Read from a file on the computer
        if mode == "2":
            print("\n[TIP] Make sure to select the file ending in '_encrypted.txt'!")
        
        raw_path = input("Enter the full path of the text file: ")
        # Clean up the path input
        file_path_in = raw_path.strip().strip('"').strip("'")

        if not os.path.exists(file_path_in):
            print(f"Error: The file '{file_path_in}' was not found.")
            return

        try:
            # I use 'replace' for errors so it doesn't crash on weird characters
            with open(file_path_in, 'r', encoding='utf-8', errors='replace') as f:
                text_content = f.read()
            print(f"[System] File loaded: {len(text_content)} characters.")
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    else:
        print("Invalid source selection.")
        return

    # Check if the text is empty
    if not text_content.strip():
        print("\n[Warning] No text found to process! Operation aborted.")
        input("Press Enter to return...")
        return

    # This loop goes through every character and swaps it
    print("\nProcessing...")
    final_text = ""
    for char in text_content:
        if char in alphabet:
            if mode == "1": # Encrypt
                 index = alphabet.find(char)
                 final_text += key[index]
            else: # Decrypt
                 index = key.find(char)
                 final_text += alphabet[index]
        else:
            # If it's not a letter (like a number or space), just keep it as is
            final_text += char

    # Show a little preview
    print("\n" + "="*40)
    print("PREVIEW OF RESULT (First 100 chars):")
    print("-" * 40)
    print(final_text[:100] + ("..." if len(final_text) > 100 else ""))
    print("="*40 + "\n")

    # Figure out where to save the file
    default_save_path = ""
    if source == "3":
        # If we opened a file, try to save the new one next to it
        base_name, extension = os.path.splitext(file_path_in)
        suffix = "_encrypted" if mode == "1" else "_decrypted"
        default_save_path = f"{base_name}{suffix}{extension}"
    else:
        # Otherwise just put it in the script folder
        default_save_path = os.path.join(script_folder, "result.txt")

    if input("Do you want to save this file? (y/n): ").lower() == 'y':
        
        # Ask user for path
        final_save_path = get_save_path(default_save_path)
        
        # Check if safe to write
        if check_overwrite(final_save_path):
            try:
                with open(final_save_path, 'w', encoding='utf-8') as f:
                    f.write(final_text)
                print(f"SUCCESS! Output saved to:\n{final_save_path}")
            except Exception as e:
                print(f"Error writing new file: {e}")
    else:
        print("Save skipped.")
    
    input("\nPress Enter to return...")


# Feature 2: Password Generator
def feature_password():
    print("\n--- Password Generator ---")
    
    length = 0
    # Make sure they enter a number at least 8. 
    # UPDATED: Replaced generic input with specific instructions and error handling.
    while length < 8:
        try:
            val = input("How many characters long should the password be? (Enter a number, min 8): ")
            length = int(val)
            
            if length < 8:
                print("Too short! Please enter a number that is 8 or higher.")
        except ValueError:
            # This runs if they type text (like "ten") instead of a number
            print("Invalid input. Please type a standard number (e.g., 12).")

    use_upper = input("Include Uppercase? (y/n): ") == 'y'
    use_lower = input("Include Lowercase? (y/n): ") == 'y'
    use_nums  = input("Include Numbers? (y/n): ")   == 'y'
    use_syms  = input("Include Symbols? (y/n): ")   == 'y'

    # If they said no to everything, force lowercase so it works
    if not (use_upper or use_lower or use_nums or use_syms):
        use_lower = True

    chars = ""
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_nums:  chars += string.digits
    if use_syms:  chars += string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(chars)

    print(f"\nGenerated Password: {password}")
    
    if input("Save to file? (y/n): ") == 'y':
        
        default_save_path = os.path.join(script_folder, "pass.txt")
        final_save_path = get_save_path(default_save_path)

        if check_overwrite(final_save_path):
            try:
                with open(final_save_path, "w") as f:
                    f.write(password)
                print(f"Saved to {final_save_path}")
            except Exception as e:
                print(f"Error saving file: {e}")
        
    input("Press Enter to return...")


# Feature 3: The Scanner (OSINT)
def feature_osint():
    print("\n--- Target Scanner (OSINT) ---")
    print("Select Operation:")
    print("1. Scan Data (Internal or File)")
    print("2. LinkedIn Recon")
    print("3. Facebook Search")
    print("4. X (Twitter) Search")
    print("5. Instagram Search")
    
    op_choice = input("Choice: ")

    if op_choice == "1":
        print("\n[Scanner Selected]")
        print("1. Scan Internal Demo Data")
        print("2. Scan a Custom File Path")
        choice = input("Choice: ")

        content = ""
        source_name = "Internal Memory"

        if choice == "1":
            source_name = "Demo Data"
            content = """
            Target: Francis / Ajax
            Contact Email: francis@badguy.com
            Standard Phone: 555-867-5309
            Phone with spaces: (555) 123 4567
            Short Phone: 555-0199
            Phone with dots: 123.456.7890
            """
        elif choice == "2":
            raw_path = input("Enter the full file path to scan: ")
            target_file = raw_path.strip().strip('"').strip("'")
            source_name = target_file

            if not os.path.exists(target_file):
                print(f"Error: The file '{target_file}' is missing.")
                return

            try:
                f = open(target_file, "r", encoding='utf-8', errors='replace')
                content = f.read()
                f.close()
            except Exception as e:
                print(f"Error reading file: {e}")
                return
        else:
            print("Invalid selection.")
            return

        print("\nData Preview:")
        print("------------------------------")
        print(content[:500].strip() + ("..." if len(content) > 500 else ""))
        print("------------------------------")

        # I updated the regex patterns to be more accurate
        # Email: I make sure it doesn't pick up dots at the end (like .net...)
        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}\b'
        
        # Phone: I made sure it ends with a number so it doesn't pick up trailing dots
        phone_regex = r'[\d\-\(\)\.\s]{6,}\d'

        # I used set() to remove duplicates, then turned it back into a list
        emails = list(set(re.findall(email_regex, content)))
        raw_phones = list(set(re.findall(phone_regex, content)))

        valid_phones = []
        for p in raw_phones:
            # I count how many digits are in the phone number
            count = 0
            for char in p:
                if char.isdigit():
                    count += 1
            
            # If it has at least 5 numbers, I count it as a phone number
            if count >= 5:
                valid_phones.append(p.strip())

        print(f"\nEmails Found: {len(emails)}")
        for e in emails: print(f"- {e}")

        print(f"\nPhones Found: {len(valid_phones)}")
        for p in valid_phones: print(f"- {p}")

        if input("\nSave report? (y/n): ") == 'y':
            
            default_save_path = os.path.join(script_folder, "scan_report.txt")
            final_save_path = get_save_path(default_save_path)

            if check_overwrite(final_save_path):
                try:
                    with open(final_save_path, "w") as f:
                        f.write(f"Source: {source_name}\n")
                        f.write(f"Emails: {emails}\nPhones: {valid_phones}")
                    print(f"Report saved to {final_save_path}")
                except Exception as e:
                    print(f"Error saving report: {e}")

    elif op_choice in ["2", "3", "4", "5"]:
        target_name = input("\nEnter the name of the target: ")
        
        site = ""
        extra_query = ""
        
        # Set up the search based on what site they picked
        if op_choice == "2":
            site = "linkedin.com"
            extra_query = input("Enter company/keyword (optional): ")
        elif op_choice == "3":
            site = "facebook.com"
            extra_query = input("Enter city/keyword (optional): ")
        elif op_choice == "4":
            site = "twitter.com"
            extra_query = input("Enter handle/keyword (optional): ")
        elif op_choice == "5":
            site = "instagram.com"
            extra_query = input("Enter handle/keyword (optional): ")

        search_query = f'site:{site} "{target_name}" {extra_query}'
        
        print(f"Searching for: {search_query}")
        print("Opening browser... maximum effort!")
        
        # This opens the google search in the default browser
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        
    else:
        print("Invalid choice.")

    input("\nPress Enter to return...")


def main():
    while True:
        print("\n=== DEADPOOL TOOL ===")
        print("1. Encrypt/Decrypt")
        print("2. Password Gen")
        print("3. OSINT Scanner")
        print("4. Exit")
        
        choice = input("Choice: ")
        
        if choice == "1": 
            feature_cipher()
        elif choice == "2": 
            feature_password()
        elif choice == "3": 
            feature_osint()
        elif choice == "4": 
            break
        else: 
            print("Invalid selection.")

if __name__ == "__main__":
    main()
