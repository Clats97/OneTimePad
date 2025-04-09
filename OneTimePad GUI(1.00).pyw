import tkinter as tk
from tkinter import messagebox

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

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Uncrackable Substitution Cipher")
        self.geometry("620x600")
        self.key = process_key(generate_key())
        self.frames = {}
        for F in (HomeFrame, EncryptFrame, DecryptFrame):
            frame = F(parent=self, controller=self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)
        self.show_frame(HomeFrame)
    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ascii_art = r""" 
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
"""
        label_ascii = tk.Label(self, text=ascii_art, fg="red", font=("Courier", 9), justify="left")
        label_ascii.pack(pady=10)
        header_frame = tk.Frame(self)
        header_frame.pack(pady=5)
        label_header_blue = tk.Label(header_frame, text="T H E   U N C R A C K A B L E   C I P H E R", fg="blue", font=("Courier", 12))
        label_header_blue.pack(side="left")
        label_version_red = tk.Label(header_frame, text=" Version 1.00", fg="red", font=("Courier", 12))
        label_version_red.pack(side="left")
        label_author = tk.Label(self, text="By Joshua M Clatney - Ethical Pentesting Enthusiast", fg="black", font=("Arial", 10))
        label_author.pack(pady=5)
        label_div = tk.Label(self, text="-----------------------------------------------------")
        label_div.pack(pady=5)
        label_options = tk.Label(self, text="Select an option:", font=("Arial", 12, "bold"))
        label_options.pack(pady=5)
        btn_encrypt = tk.Button(self, text="Encrypt", width=20, command=lambda: controller.show_frame(EncryptFrame))
        btn_encrypt.pack(pady=5)
        btn_decrypt = tk.Button(self, text="Decrypt", width=20, command=lambda: controller.show_frame(DecryptFrame))
        btn_decrypt.pack(pady=5)

class EncryptFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Encrypt", font=("Arial", 14))
        label.pack(pady=10)
        label_input = tk.Label(self, text="Enter plaintext:")
        label_input.pack()
        self.text_input = tk.Text(self, height=5, width=60)
        self.text_input.pack(pady=5)
        btn_process = tk.Button(self, text="Process Encryption", command=self.process_encrypt)
        btn_process.pack(pady=10)
        label_result = tk.Label(self, text="Encrypted ciphertext:", font=("Arial", 12))
        label_result.pack()
        self.text_output = tk.Text(self, height=5, width=60, state="disabled")
        self.text_output.pack(pady=5)
        btn_home = tk.Button(self, text="Return Home", command=lambda: controller.show_frame(HomeFrame))
        btn_home.pack(pady=10)
    
    def process_encrypt(self):
        plaintext = self.text_input.get("1.0", tk.END).strip().upper()
        letter_count = sum(1 for c in plaintext if 'A' <= c <= 'Z')
        if letter_count > len(self.controller.key):
            messagebox.showerror("Input Error", f"The number of letters in plaintext ({letter_count}) exceeds key length ({len(self.controller.key)}).")
            return
        encrypted = encrypt(plaintext, self.controller.key)
        self.text_output.config(state="normal")
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, encrypted)
        self.text_output.config(state="disabled")

class DecryptFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Decrypt", font=("Arial", 14))
        label.pack(pady=10)
        label_input = tk.Label(self, text="Enter ciphertext:")
        label_input.pack()
        self.text_input = tk.Text(self, height=5, width=60)
        self.text_input.pack(pady=5)
        btn_process = tk.Button(self, text="Process Decryption", command=self.process_decrypt)
        btn_process.pack(pady=10)
        label_result = tk.Label(self, text="Decrypted plaintext:", font=("Arial", 12))
        label_result.pack()
        self.text_output = tk.Text(self, height=5, width=60, state="disabled")
        self.text_output.pack(pady=5)
        btn_home = tk.Button(self, text="Return Home", command=lambda: controller.show_frame(HomeFrame))
        btn_home.pack(pady=10)
    
    def process_decrypt(self):
        ciphertext = self.text_input.get("1.0", tk.END).strip().upper()
        letter_count = sum(1 for c in ciphertext if 'A' <= c <= 'Z')
        if letter_count > len(self.controller.key):
            messagebox.showerror("Input Error", f"The number of letters in ciphertext ({letter_count}) exceeds key length ({len(self.controller.key)}).")
            return
        try:
            decrypted = decrypt(ciphertext, self.controller.key)
        except Exception as e:
            messagebox.showerror("Decryption Error", str(e))
            return
        self.text_output.config(state="normal")
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, decrypted)
        self.text_output.config(state="disabled")

if __name__ == "__main__":
    app = Application()
    app.mainloop()