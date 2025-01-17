import sys
from typing import Dict, Tuple
import math

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    """
    Display the EmojiChef banner
    """
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
███████╗███╗   ███╗ ██████╗      ██╗██╗ ██████╗██╗  ██╗███████╗███████╗
██╔════╝████╗ ████║██╔═══██╗     ██║██║██╔════╝██║  ██║██╔════╝██╔════╝
█████╗  ██╔████╔██║██║   ██║     ██║██║██║     ███████║█████╗  █████╗  
██╔══╝  ██║╚██╔╝██║██║   ██║██   ██║██║██║     ██╔══██║██╔══╝  ██╔══╝  
███████╗██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║╚██████╗██║  ██║███████╗██║     
╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝     
{Colors.BLUE}═════════════════════════════════════════════════════════════════
        Cooking Up Delicious Emoji Encodings! 👨‍🍳 v1.0
═════════════════════════════════════════════════════════════════{Colors.ENDC}
"""
    print(banner)

class EmojiCodec:
    def __init__(self, recipe_type: str = "classic"):
        """
        Initialize the encoder with different recipe types
        
        Args:
            recipe_type: Encoding base type
        """
        self.recipe_type = recipe_type
        self._initialize_ingredients()
        
    def _initialize_ingredients(self):
        """Initialize encoding/decoding maps based on selected recipe type"""
        if self.recipe_type == "quick_bite":  # base-64
            self.emoji_map = {i: chr(0x1F345 + i) for i in range(64)}  # Food emojis
            self.bits_per_chunk = 6
            
        elif self.recipe_type == "light_meal":  # base-128
            self.emoji_map = {i: chr(0x1F3B0 + i) for i in range(128)}  # Activity emojis
            self.bits_per_chunk = 7
            
        elif self.recipe_type == "classic":  # base-256
            self.emoji_map = {i: chr(0x1F600 + i) for i in range(256)}  # Smiley emojis
            self.bits_per_chunk = 8
            
        elif self.recipe_type == "gourmet":  # base-1024
            self.emoji_map = {i: chr(0x1F900 + i) for i in range(1024)}  # Extended emojis
            self.bits_per_chunk = 10
            
        else:
            raise ValueError(f"Unknown recipe type: {self.recipe_type}")
        
        self.reverse_map = {v: k for k, v in self.emoji_map.items()}
        self.base_size = len(self.emoji_map)
        self.mask = (1 << self.bits_per_chunk) - 1
        
    def encode(self, data: str) -> str:
        """
        Encode a string into emoji representation
        """
        try:
            byte_data = data.encode('utf-8')
            result = []
            current_bits = 0
            current_value = 0
            
            for byte in byte_data:
                current_value = (current_value << 8) | byte
                current_bits += 8
                
                while current_bits >= self.bits_per_chunk:
                    current_bits -= self.bits_per_chunk
                    index = (current_value >> current_bits) & self.mask
                    result.append(self.emoji_map[index])
                    current_value &= (1 << current_bits) - 1
            
            # Handle remaining bits
            if current_bits > 0:
                index = (current_value << (self.bits_per_chunk - current_bits)) & self.mask
                result.append(self.emoji_map[index])
                
            return ''.join(result)
            
        except Exception as e:
            raise ValueError(f"Kitchen accident while encoding: {str(e)}")
    
    def decode(self, emoji_data: str) -> str:
        """
        Decode emoji representation back to original string
        """
        try:
            result = bytearray()
            current_bits = 0
            current_value = 0
            
            for emoji in emoji_data:
                value = self.reverse_map[emoji]
                current_value = (current_value << self.bits_per_chunk) | value
                current_bits += self.bits_per_chunk
                
                while current_bits >= 8:
                    current_bits -= 8
                    byte = (current_value >> current_bits) & 0xFF
                    result.append(byte)
                    current_value &= (1 << current_bits) - 1
            
            return bytes(result).decode('utf-8')
            
        except Exception as e:
            raise ValueError(f"Kitchen accident while decoding: {str(e)}")
    
    def get_stats(self, original: str, encoded: str) -> Dict[str, float]:
        """Calculate encoding statistics"""
        orig_bytes = len(original.encode('utf-8'))
        enc_len = len(encoded)
        ratio = enc_len/orig_bytes if orig_bytes > 0 else 0
        bits_per_char = math.log2(self.base_size)
        theoretical_ratio = 8/bits_per_char
        
        return {
            'original_bytes': orig_bytes,
            'encoded_length': enc_len,
            'actual_ratio': ratio,
            'theoretical_ratio': theoretical_ratio,
            'bits_per_emoji': bits_per_char
        }

def print_menu():
    """Display the interactive menu"""
    print(f"\n{Colors.GREEN}=== EmojiChef's Kitchen ==={Colors.ENDC}")
    print("1. Cook up an encoded message")
    print("2. Taste test (decode) a message")
    print("3. Change recipe type")
    print("4. Check the ingredients")
    print("5. Leave the kitchen")
    print(f"{Colors.GREEN}========================={Colors.ENDC}")

def get_valid_input(prompt: str, valid_options: list) -> str:
    """Get validated user input"""
    while True:
        choice = input(f"{Colors.CYAN}{prompt}{Colors.ENDC}").strip()
        if choice in valid_options:
            return choice
        print(f"{Colors.RED}Invalid ingredient. Please choose from {', '.join(valid_options)}{Colors.ENDC}")

def main():
    print_banner()
    codec = EmojiCodec()
    
    while True:
        print_menu()
        choice = get_valid_input("Select your cooking method (1-5): ", ['1', '2', '3', '4', '5'])
        
        if choice == '1':  # Encode
            message = input(f"\n{Colors.CYAN}Enter your message to cook: {Colors.ENDC}")
            try:
                encoded = codec.encode(message)
                stats = codec.get_stats(message, encoded)
                print(f"\n{Colors.GREEN}Fresh from the kitchen: {Colors.ENDC}{encoded}")
                print(f"{Colors.YELLOW}Original ingredients: {stats['original_bytes']} bytes")
                print(f"Cooked size: {stats['encoded_length']} emojis")
                print(f"Recipe efficiency: {stats['actual_ratio']:.2f}{Colors.ENDC}")
            except ValueError as e:
                print(f"{Colors.RED}Kitchen accident: {e}{Colors.ENDC}")
                
        elif choice == '2':  # Decode
            emoji_text = input(f"\n{Colors.CYAN}Paste the emoji dish to taste: {Colors.ENDC}")
            try:
                decoded = codec.decode(emoji_text)
                print(f"\n{Colors.GREEN}Original recipe: {Colors.ENDC}{decoded}")
            except ValueError as e:
                print(f"{Colors.RED}Tasting error: {e}{Colors.ENDC}")
                
        elif choice == '3':  # Change base
            print(f"\n{Colors.YELLOW}Available recipes:")
            print("1. Quick Bite (base-64 with food emojis)")
            print("2. Light Meal (base-128 with activity emojis)")
            print("3. Classic Recipe (base-256 with smileys)")
            print("4. Gourmet Special (base-1024 with extended set){Colors.ENDC}")
            base_choice = get_valid_input("Choose your recipe (1-4): ", ['1', '2', '3', '4'])
            recipes = {
                '1': 'quick_bite',
                '2': 'light_meal',
                '3': 'classic',
                '4': 'gourmet'
            }
            codec = EmojiCodec(recipes[base_choice])
            print(f"\n{Colors.GREEN}Now cooking with: {codec.recipe_type} recipe{Colors.ENDC}")
            
        elif choice == '4':  # Show settings
            print(f"\n{Colors.YELLOW}Current recipe: {codec.recipe_type}")
            print(f"Pantry size: {codec.base_size} ingredients")
            print(f"Bits per emoji: {math.log2(codec.base_size):.1f}")
            print(f"\nSample ingredients from current recipe:")
            sample_emojis = list(codec.emoji_map.values())[:8]
            print(f"{' '.join(sample_emojis)}{Colors.ENDC}")
            
        else:  # Exit
            print(f"\n{Colors.GREEN}Thanks for visiting EmojiChef's Kitchen! 👨‍🍳{Colors.ENDC}")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Chef had to leave early. Goodbye! 👨‍🍳{Colors.ENDC}")
        sys.exit(0)
