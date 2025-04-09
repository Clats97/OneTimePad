import tkinter as tk
from tkinter import messagebox

def print_ascii_art():
    art = r""" 
  ██████╗ ███╗   ██╗███████╗████████╗██╗███╗   ██╗███████╗██████╗  █████╗ ██████╗ 
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
    return art

def process_key(key):
    return ''.join([c for c in key.upper() if 'A' <= c <= 'Z'])

def generate_key():
    base_keys = {
        1: (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
            "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
            "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        ),
        2: (
            "Diazepam and other drugs in the benzodiazepine class are positive allosteric modulators no functional response alone but increase"
            "the response of the endogenous ligand of the GABAA aminobutyric acid type A receptor complex binding to a unique site on the"
            "alpha-gamma subunit interfact Diazepam interaction with these sites increases neuronal chloride ion influx upon GABA binding"
            "resulting in hyperpolarized postsynaptic membranes thus enhancing CNS depression response to endogenous GABA"
        ),
        3: (
            "distant mountains reflected purple hues against evening sky birds circled above abandoned lighthouse their calls echoing across bay"
            "fisherman repaired nets while humming forgotten melody children gathered seashells along shoreline comparing unique patterns and colors"
            "small café near dock served freshly caught fish to weary travelers lighthouse keeper recorded weather patterns in leatherbound journal"
            "waves crashed rhythmically against jagged rocks below old sailing ship appeared on horizon white sails billowing in breeze local legends"
            "spoke of treasures hidden in underwater caves nearby annual festival would begin tomorrow"
        ),
        4: (
            "university libraries housed centuries of knowledge within dusty shelves students huddled around tables frantically preparing for upcoming examinations"
            "professor lecture on renaissance art captivated normally restless audience coffee cups littered study carrels as midnight approached ancient manuscripts"
            "required special handling procedures to prevent deterioration digital archives project aimed to preserve fragile documents for future generations"
            "campus groundskeepers planted tulip bulbs that would bloom in spring renowned physicist challenged conventional theories during symposium heated debates"
            "continued long after formal discussions ended administrative offices processed scholarship applications with meticulous attention"
        ),
        5: (
            "urban gardens transformed concrete wastelands into vibrant community spaces volunteer coordinators organized weekly maintenance schedules throughout growing seasons"
            "tomato vines climbed recycled trellises while bees pollinated flowering plants children learned about sustainable agriculture through hands on activities"
            "rainwater collection systems provided irrigation during dry periods composting initiatives reduced neighborhood waste while enriching garden soil"
            "local chefs featured harvested produce in seasonal menu offerings elderly residents shared traditional farming knowledge with younger generations"
            "metal sculptures created by area artists decorated pathway entrances educational workshops covered topics from seed saving to food preservation"
        ),
        6: (
            "silent cloudy vivid musical lemon swift amber ignite pebble velvet glance timber shadow anchor gravity rapid simple copper garden olive summit desert crystal"
            "eager ocean rhythm magic honey puzzle autumn gentle future spirit crimson walnut whisper candle tulip freedom silver meadow bright pocket artist marble legend"
            "sunny velvet engine orchid quiet lunar ripple galaxy tender hollow melody secret midnight ginger cherry eager ocean rhythm magic honey puzzle autumn gentle"
            "future spirit crimson walnut whisper candle tulip freedom silver meadow bright pocket artist marble legend future spirit crimson walnut whisper candle tulip"
            "freedom silver meadow bright pocket artist marble legend"
        ),
        7: (
            "mystic canyon fossil ribbon amber flight meadow silver candle twilight river flower velvet painter galaxy sunrise pebble crystal garden voyage almond marble"
            "drift silent autumn velvet forest nectar golden feather ripple cobalt gentle harbor anchor desert tranquil palace whisper comet cinnamon sapphire shadow flame"
            "orchard secret gravity ivory blossom lunar horizon swift meadow olive engine winter amber copper rainbow spirit journey mystic canyon fossil ribbon amber"
            "flight meadow silver candle twilight river flower velvet painter galaxy sunrise pebble crystal garden voyage almond marble hello world testing alpha beta"
            "quat peroxide ammonium bleach oxivir accel rescue dog cat chien fox wonderful twilight sire"
        ),
        8: (
            "puzzle ginger pebble ivory sapphire midnight gentle timber crystal ripple almond velvet sunset marble lunar engine whisper silent galaxy crimson shadow"
            "magic nectar swift flower feather comet velvet sunrise meadow cinnamon ocean vivid puzzle melody canyon copper horizon drift forest silver autumn quiet"
            "lemon twilight anchor blossom rapid meadow honey orchid spirit palace amber desert tranquil olive river secret flame magic nectar swift flower feather"
            "comet velvet sunrise meadow cinnamon ocean vivid puzzle melody canyon copper horizon drift forest silver autumn quiet michael john tommy pavarotti"
            "why talk freddie mercury gerry rafferty night own baker street sherlock clatscope"
        ),
        9: (
            "forest vivid sapphire candle ginger pebble melody ocean anchor cinnamon garden sunset horizon amber palace ripple lunar crystal silent whisper nectar autumn"
            "velvet shadow marble flower gentle swift comet silver meadow drift blossom desert ivory almond twilight puzzle cobalt secret orchard sunrise feather honey"
            "canyon spirit rapid flame walnut olive velvet tranquil amber copper galaxy silent midnight lemon velvet shadow marble flower gentle swift comet silver"
            "meadow drift blossom desert ivory almond twilight puzzle cobalt secret orchard sunrise feather honey microscopic teleporting doctor who law and order"
            "special victims unit fuck hello sire you are the king i am the queen gay man straight man heterosexual homosequal pansexual"
        ),
        10: (
            "swift galaxy autumn feather copper gentle whisper palace marble puzzle velvet cinnamon almond lunar blossom horizon ripple sapphire canyon silent amber ivory"
            "nectar pebble crystal melody velvet forest ginger desert honey flame orchid anchor twilight meadow comet sunset secret rapid timber ocean engine olive silver"
            "tranquil vivid spirit walnut magic sunrise shadow candle cobalt drift flower amber silent palace nectar pebble crystal melody velvet forest ginger desert"
            "honey flame orchid anchor twilight meadow comet sunset secret rapid timber ocean engine olive silver a garden of pure ideology youll see why nineteen eighty"
            "four wont be like nineteen eighty four apple superbowl advertisment"
        )
    }
    keys = {}
    for k, text in base_keys.items():
        repeated = text * 5
        keys[k] = process_key(repeated)
    return keys

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
        self.title("OneTimePad Cipher GUI v1.00")
        self.geometry("620x700")
        self.keys = generate_key()
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
        ascii_art = print_ascii_art()
        label_ascii = tk.Label(self, text=ascii_art, fg="red", font=("Courier", 9), justify="left")
        label_ascii.pack(pady=10)
        header_frame = tk.Frame(self)
        header_frame.pack(pady=5)
        label_header_blue = tk.Label(header_frame, text="T H E   U N C R A C K A B L E   C I P H E R", fg="blue", font=("Courier", 12))
        label_header_blue.pack(side="left")
        label_version_red = tk.Label(header_frame, text="   Version 1.00", fg="red", font=("Courier", 12))
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
        self.text_input = tk.Text(self, height=5, width=80)
        self.text_input.pack(pady=5)
        label_key = tk.Label(self, text="Select key number:")
        label_key.pack()
        self.key_var = tk.StringVar(self)
        options = [str(num) for num in range(1, 11)]
        self.key_var.set(options[0])
        option_menu = tk.OptionMenu(self, self.key_var, *options)
        option_menu.pack(pady=5)
        btn_process = tk.Button(self, text="Encrypt", command=self.process_encrypt)
        btn_process.pack(pady=10)
        label_result = tk.Label(self, text="Encrypted ciphertext:", font=("Arial", 12))
        label_result.pack()
        self.text_output = tk.Text(self, height=5, width=80, state="disabled")
        self.text_output.pack(pady=5)
        btn_home = tk.Button(self, text="Return Home", command=lambda: controller.show_frame(HomeFrame))
        btn_home.pack(pady=10)

    def process_encrypt(self):
        plaintext = self.text_input.get("1.0", tk.END).strip().upper()
        try:
            selected = int(self.key_var.get())
        except:
            messagebox.showerror("Input Error", "Invalid key selection.")
            return
        key = self.controller.keys.get(selected, "")
        letter_count = sum(1 for c in plaintext if 'A' <= c <= 'Z')
        if letter_count > len(key):
            messagebox.showerror("Input Error", f"Letters in plaintext ({letter_count}) exceed key length ({len(key)}).")
            return
        encrypted = encrypt(plaintext, key)
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
        self.text_input = tk.Text(self, height=5, width=80)
        self.text_input.pack(pady=5)
        label_key = tk.Label(self, text="Select key number:")
        label_key.pack()
        self.key_var = tk.StringVar(self)
        options = [str(num) for num in range(1, 11)]
        self.key_var.set(options[0])
        option_menu = tk.OptionMenu(self, self.key_var, *options)
        option_menu.pack(pady=5)
        btn_process = tk.Button(self, text="Decrypt", command=self.process_decrypt)
        btn_process.pack(pady=10)
        label_result = tk.Label(self, text="Decrypted plaintext:", font=("Arial", 12))
        label_result.pack()
        self.text_output = tk.Text(self, height=5, width=80, state="disabled")
        self.text_output.pack(pady=5)
        btn_home = tk.Button(self, text="Return Home", command=lambda: controller.show_frame(HomeFrame))
        btn_home.pack(pady=10)

    def process_decrypt(self):
        ciphertext = self.text_input.get("1.0", tk.END).strip().upper()
        try:
            selected = int(self.key_var.get())
        except:
            messagebox.showerror("Input Error", "Invalid key selection.")
            return
        key = self.controller.keys.get(selected, "")
        letter_count = sum(1 for c in ciphertext if 'A' <= c <= 'Z')
        if letter_count > len(key):
            messagebox.showerror("Input Error", f"Letters in ciphertext ({letter_count}) exceed key length ({len(key)}).")
            return
        try:
            decrypted = decrypt(ciphertext, key)
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