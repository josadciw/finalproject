import random
import string
import re
import os
import webbrowser

# Final Project: Deadpool Encryption Tool
# UPDATED: Added Result Preview to verify decryption works before saving.

script_folder = os.path.dirname(os.path.abspath(__file__))

# Feature 1: Substitution Cipher
def feature_cipher():
    print("\n--- Deadpool's File Scrambler ---")
    
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key      = "defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC"

    # Ask the user for the mode
    mode = input("Select: (1) Encrypt or (2) Decrypt: ")
    
    # Ask the user for the source
    print("\nSource:")
    print("1. Manual Input (Type text now)")
    print("2. Internal Demo Text")
    print("3. External File (Input a file path)")
    source = input("Choice: ")
    
    text_content = ""
    file_path_in = "" 

    # --- SOURCE HANDLING ---
    if source == "1":
        # Manual Input
        print("\n[Manual Mode] Enter text below (Press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        text_content = "\n".join(lines)

    elif source == "2":
        # Internal Demo
        print("\n[System] Loading internal demo text...")
        if mode == "1":
            text_content = "The secret stash is hidden under the floorboards."
        else:
            text_content = "Wkh vhfuhw vwdvk lv klgghq xqghu wkh iooruerdugv."

    elif source == "3":
        # External File Input
        if mode == "2":
            print("\n[TIP] Make sure to select the file ending in '_encrypted.txt'!")
        
        raw_path = input("Enter the full path of the text file: ")
        file_path_in = raw_path.strip().strip('"').strip("'")

        if not os.path.exists(file_path_in):
            print(f"Error: The file '{file_path_in}' was not found.")
            return

        try:
            # errors='replace' ensures we read the file even if encoding is weird
            with open(file_path_in, 'r', encoding='utf-8', errors='replace') as f:
                text_content = f.read()
            print(f"[System] File loaded: {len(text_content)} characters.")
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    else:
        print("Invalid source selection.")
        return

    # --- SAFETY CHECK: EMPTY INPUT ---
    if not text_content.strip():
        print("\n[Warning] No text found to process! Operation aborted.")
        input("Press Enter to return...")
        return

    # --- PROCESSING LOOP ---
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
            final_text += char

    # --- RESULT PREVIEW (New!) ---
    # This proves the logic worked before we even try to save the file
    print("\n" + "="*40)
    print("PREVIEW OF RESULT (First 100 chars):")
    print("-" * 40)
    print(final_text[:100] + ("..." if len(final_text) > 100 else ""))
    print("="*40 + "\n")

    # --- OUTPUT HANDLING ---
    
    # Case A: File Source (Auto-Save to NEW file)
    if source == "3":
        base_name, extension = os.path.splitext(file_path_in)
        suffix = "_encrypted" if mode == "1" else "_decrypted"
        new_file_path = f"{base_name}{suffix}{extension}"
        
        # Overwrite protection
        if os.path.exists(new_file_path):
            print(f"[Warning] The file '{new_file_path}' already exists.")
            confirm = input("Overwrite it? (y/n): ")
            if confirm.lower() != 'y':
                print("Operation canceled. File was NOT saved.")
                return

        try:
            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(final_text)
            print(f"SUCCESS! Output saved to:\n{new_file_path}")
        except Exception as e:
            print(f"Error writing new file: {e}")

    # Case B: Manual/Demo Source (Ask user for filename)
    else:
        if input("Save result to file? (y/n): ") == 'y':
            name = input("Enter name for NEW output file (e.g., result.txt): ")
            save_path = os.path.join(script_folder, name)
            
            try:
                f = open(save_path, "w", encoding='utf-8')
                f.write(final_text)
                f.close()
                print(f"File saved to {script_folder}")
            except Exception as e:
                print(f"Error saving file: {e}")
    
    input("\nPress Enter to return...")


# Feature 2: Password Generator
def feature_password():
    print("\n--- Password Generator ---")
    
    length = 0
    while length < 8:
        try:
            length = int(input("Enter length (min 8): "))
        except:
            pass 

    use_upper = input("Include Uppercase? (y/n): ") == 'y'
    use_lower = input("Include Lowercase? (y/n): ") == 'y'
    use_nums  = input("Include Numbers? (y/n): ")   == 'y'
    use_syms  = input("Include Symbols? (y/n): ")   == 'y'

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
        p_path = os.path.join(script_folder, "pass.txt")
        if os.path.exists(p_path):
            if input("pass.txt exists. Overwrite? (y/n): ").lower() != 'y':
                print("Save canceled.")
                return

        try:
            f = open(p_path, "w")
            f.write(password)
            f.close()
            print("Saved to pass.txt")
        except Exception as e:
            print(f"Error saving file: {e}")
        
    input("Press Enter to return...")


# Feature 3: OSINT Scanner
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

        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        phone_regex = r'[\d\-\(\)\.\s]{7,}'

        emails = list(set(re.findall(email_regex, content)))
        raw_phones = list(set(re.findall(phone_regex, content)))

        valid_phones = []
        for p in raw_phones:
            digit_count = sum(c.isdigit() for c in p)
            if digit_count >= 5:
                valid_phones.append(p.strip())

        print(f"\nEmails Found: {len(emails)}")
        for e in emails: print(f"- {e}")

        print(f"\nPhones Found: {len(valid_phones)}")
        for p in valid_phones: print(f"- {p}")

        if input("\nSave report? (y/n): ") == 'y':
            r_path = os.path.join(script_folder, "scan_report.txt")
            if os.path.exists(r_path):
                if input("scan_report.txt exists. Overwrite? (y/n): ").lower() != 'y':
                    print("Save canceled.")
                    return

            try:
                f = open(r_path, "w")
                f.write(f"Source: {source_name}\n")
                f.write(f"Emails: {emails}\nPhones: {valid_phones}")
                f.close()
                print("Report saved.")
            except Exception as e:
                print(f"Error saving report: {e}")

    elif op_choice in ["2", "3", "4", "5"]:
        target_name = input("\nEnter the name of the target: ")
        
        site = ""
        extra_query = ""
        
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

if __name__ == "__main__":
    main()