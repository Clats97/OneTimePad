import sys

def print_header():
    red = "\033[31m"
    blue = "\033[34m"
    black = "\033[30m"
    reset = "\033[0m"
    
    ascii_art = red + r""" 
    
    
██████╗ ███╗   ██╗███████╗████████╗██╗███╗   ███╗███████╗██████╗  █████╗ ██████╗ 
██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██║████╗ ████║██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║   ██║██╔██╗ ██║█████╗     ██║   ██║██╔████╔██║█████╗  ██████╔╝███████║██║  ██║
██║   ██║██║╚██╗██║██╔══╝     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔═══╝ ██╔══██║██║  ██║
╚██████╔╝██║ ╚████║███████╗   ██║   ██║██║ ╚═╝ ██║███████╗██║     ██║  ██║██████╔╝
 ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═════╝ 
                                                                                  
                     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗                    
                    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗                    
                    ██║     ██║██████╔╝███████║█████╗  ██████╔╝                    
                    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗                    
                    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║                    
                     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                    
                                                                                  """ + reset
    print(ascii_art)
    print(blue + "T H E   U N C R A C K A B L E   S U B S T I T U T I O N   C I P H E R " + red + "Version 1.00" + "\033[0m")
    print(black + "By Joshua M Clatney - Ethical Pentesting Enthusiast" + "\033[0m")
    print()

def generate_key():
    lorem_ipsum = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    )
    return lorem_ipsum * 5

def process_key(key):
    return ''.join([c for c in key.upper() if 'A' <= c <= 'Z'])

def encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if 'A' <= char <= 'Z':
            pt_val = ord(char) - ord('A')
            shift = ord(key[key_index]) - ord('A')
            ct_val = (pt_val + shift) % 26
            ciphertext += chr(ct_val + ord('A'))
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if 'A' <= char <= 'Z':
            ct_val = ord(char) - ord('A')
            shift = ord(key[key_index]) - ord('A')
            pt_val = (ct_val - shift) % 26
            plaintext += chr(pt_val + ord('A'))
            key_index += 1
        else:
            plaintext += char
    return plaintext

def main():
    print_header()
    raw_key = generate_key()
    key = process_key(raw_key)
    print("Select an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        plaintext = input("Enter plaintext: ").strip().upper()
        num_letters = sum(1 for c in plaintext if 'A' <= c <= 'Z')
        if num_letters > len(key):
            print(f"Error: The number of letters in plaintext ({num_letters}) exceeds key length ({len(key)}).")
            sys.exit(1)
        encrypted = encrypt(plaintext, key)
        print("\nEncrypted ciphertext:")
        print(encrypted)
        
    elif choice == '2':
        ciphertext = input("Enter ciphertext: ").strip().upper()
        num_letters = sum(1 for c in ciphertext if 'A' <= c <= 'Z')
        if num_letters > len(key):
            print(f"Error: The number of letters in ciphertext ({num_letters}) exceeds key length ({len(key)}).")
            sys.exit(1)
        try:
            decrypted = decrypt(ciphertext, key)
            print("\nDecrypted plaintext:")
            print(decrypted)
        except Exception as e:
            print("Decryption error:", e)
            sys.exit(1)
    else:
        print("Invalid choice. Please select 1 for encryption or 2 for decryption.")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()