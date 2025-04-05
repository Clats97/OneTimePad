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
    print(blue + "T H E   U N C R A C K A B L E   S U B S T I T U T I O N   C I P H E R       Version 1.00" + "\033[0m")
    print(black + "By Joshua M Clatney - Ethical Pentesting Enthusiast" + "\033[0m")
    print()

def process_key(key):
    return ''.join([c for c in key.upper() if 'A' <= c <= 'Z'])

def generate_key():
    """
    Generates a dictionary of keys.
    Key 1 is the original lorem ipsum paragraph.
    Keys 2 to 10 are the additional paragraphs provided.
    Each key is repeated 5 times.
    """
    base_keys = {
        1: (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
            "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
            "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        ),
        2: (
            "Diazepam and other drugs in the benzodiazepine class are positive allosteric modulators no functional response alone but increase "
            "the response of the endogenous ligand of the GABAA aminobutyric acid type A receptor complex binding to a unique site on the "
            "alpha-gamma subunit interfact Diazepam interaction with these sites increases neuronal chloride ion influx upon GABA binding "
            "resulting in hyperpolarized postsynaptic membranes thus enhancing CNS depression response to endogenous GABA"
        ),
        3: (
            "distant mountains reflected purple hues against evening sky birds circled above abandoned lighthouse their calls echoing across bay "
            "fisherman repaired nets while humming forgotten melody children gathered seashells along shoreline comparing unique patterns and colors "
            "small café near dock served freshly caught fish to weary travelers lighthouse keeper recorded weather patterns in leatherbound journal "
            "waves crashed rhythmically against jagged rocks below old sailing ship appeared on horizon white sails billowing in breeze local legends "
            "spoke of treasures hidden in underwater caves nearby annual festival would begin tomorrow"
        ),
        4: (
            "university libraries housed centuries of knowledge within dusty shelves students huddled around tables frantically preparing for upcoming examinations "
            "professor lecture on renaissance art captivated normally restless audience coffee cups littered study carrels as midnight approached ancient manuscripts "
            "required special handling procedures to prevent deterioration digital archives project aimed to preserve fragile documents for future generations "
            "campus groundskeepers planted tulip bulbs that would bloom in spring renowned physicist challenged conventional theories during symposium heated debates "
            "continued long after formal discussions ended administrative offices processed scholarship applications with meticulous attention"
        ),
        5: (
            "urban gardens transformed concrete wastelands into vibrant community spaces volunteer coordinators organized weekly maintenance schedules throughout growing seasons "
            "tomato vines climbed recycled trellises while bees pollinated flowering plants children learned about sustainable agriculture through hands on activities "
            "rainwater collection systems provided irrigation during dry periods composting initiatives reduced neighborhood waste while enriching garden soil "
            "local chefs featured harvested produce in seasonal menu offerings elderly residents shared traditional farming knowledge with younger generations "
            "metal sculptures created by area artists decorated pathway entrances educational workshops covered topics from seed saving to food preservation"
        ),
        6: (
            "ancient forests contained ecosystems that scientists had barely begun to understand towering redwoods created their own weather patterns through transpiration processes "
            "mushroom varieties spread underground networks connecting seemingly separate organisms researchers documented previously unknown insect species during expeditions "
            "wildlife biologists tracked migration patterns through remote camera systems conservation efforts focused on protecting critical habitat from development threats "
            "indigenous communities maintained traditional relationships with forest resources fallen logs provided essential nutrients as they slowly decomposed "
            "seasonal changes transformed forest floor into constantly evolving landscapes fire ecology studies revealed regenerative cycles"
        ),
        7: (
            "technological innovations dramatically altered communication patterns between generations social media platforms created both connections and divisions within family structures "
            "grandparents learned video calling applications to maintain relationships with distant grandchildren digital literacy programs targeted older adults facing technological barriers "
            "screen time recommendations evolved as research revealed complex impacts on development virtual reality applications offered immersive educational experiences across subject areas "
            "privacy concerns prompted legislative reforms regarding data collection practices artificial intelligence assistants became commonplace in homes and businesses "
            "remote work opportunities expanded geographic possibilities for many professionals"
        ),
        8: (
            "traditional craftsmanship persisted despite industrial manufacturing dominance apprenticeship programs preserved specialized techniques through direct mentorship "
            "artisans combined historical methods with contemporary design approaches hand thrown pottery reflected individual expressions through subtle variations "
            "woodworkers selected materials based on grain patterns and structural properties textile artists incorporated natural dyes harvested from local plants "
            "metal forging required precise temperature control and timing glass blowing studios attracted visitors fascinated by transformation process "
            "cultural heritage museums documented craft evolution through historical examples market demand for handmade items fluctuated with economic conditions"
        ),
        9: (
            "culinary traditions revealed historical migrations through ingredient combinations and techniques regional cooking methods adapted to available resources and environmental conditions "
            "family recipes transmitted cultural identity across generations fermentation practices preserved seasonal abundance while creating complex flavors "
            "market vendors arranged produce displays with artistic consideration restaurant kitchens operated with choreographed precision during busy service periods "
            "cooking instruction incorporated scientific principles behind traditional methods food security initiatives addressed systemic inequalities in nutritional access "
            "agricultural practices directly influenced flavor profiles in resulting dishes celebration meals marked important transitions through symbolic offerings"
        ),
        10: (
            "ocean exploration revealed ecosystems thriving in seemingly impossible conditions underwater volcanic vents supported life forms with unique biological adaptations "
            "research vessels collected data through sophisticated sensing equipment marine biologists documented behavior patterns among pod dwelling mammals "
            "conservation agreements attempted to address international fishing concerns coral reef degradation accelerated with changing ocean temperatures "
            "coastal communities developed resilience strategies for rising sea levels plastic pollution affected marine life throughout food chain "
            "underwater archaeology revealed historical shipwrecks preserved in deep water environments wave energy technologies offered sustainable power generation possibilities"
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

def main():
    print_header()
    keys = generate_key()  # keys is a dictionary with keys 1-10
    print("Select an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        plaintext = input("Enter plaintext: ").strip().upper()
        print("\nAvailable keys:")
        for num, key_text in keys.items():
            preview = key_text[:40] + "..." if len(key_text) > 40 else key_text
            print(f"{num}. {preview}")
        try:
            selected_key = int(input("Select the key number to use: ").strip())
            if selected_key not in keys:
                print("Invalid key selection.")
                sys.exit(1)
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the key.")
            sys.exit(1)
            
        key = keys[selected_key]
        num_letters = sum(1 for c in plaintext if 'A' <= c <= 'Z')
        if num_letters > len(key):
            print(f"Error: The number of letters in plaintext ({num_letters}) exceeds key length ({len(key)}).")
            sys.exit(1)
        encrypted = encrypt(plaintext, key)
        print("\nEncrypted ciphertext:")
        print(encrypted)
        
    elif choice == '2':
        ciphertext = input("Enter ciphertext: ").strip().upper()
        print("\nAvailable keys:")
        for num, key_text in keys.items():
            preview = key_text[:40] + "..." if len(key_text) > 40 else key_text
            print(f"{num}. {preview}")
        try:
            selected_key = int(input("Select the key number to use: ").strip())
            if selected_key not in keys:
                print("Invalid key selection.")
                sys.exit(1)
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the key.")
            sys.exit(1)
            
        key = keys[selected_key]
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