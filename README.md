# 👨‍🍳 EmojiChef v1.0 | CurlyFries

Welcome to EmojiChef's Kitchen, where plain text gets cooked into delicious [emoji](https://home.unicode.org/emoji/) encodings! EmojiChef is a Python-based text encoder that transforms your messages into tasty emoji representations using various "recipe" types. Our kitchen serves up both classic and gourmet emoji dishes, with a focus on efficiency and flavor!

*Note: This is version 1.0 of EmojiChef aka CurlyFries. For advanced features like file handling, compression, and batch processing, please see [EmojiChef v2.1 👀](https://github.com/FreddyRodgers/emojichef)*

For peer review: [mathematic principles and encoding theory](docs/emojichef-math.md) supporting EmojiChef

## Quick Start

```python
from emojichef-v1 import EmojiCodec

# Create a codec with default settings
codec = EmojiCodec()

# Encode a message
message = "Hello, World!"
encoded = codec.encode(message)
print(f"Encoded: {encoded}")

# Decode the message
decoded = codec.decode(encoded)
print(f"Decoded: {decoded}")
```

## Features

### Recipe Types (Encoding Bases)

1. **Quick Bite (Base-64)** 🍅
   - Uses food emojis
   - Range: 0x1F345-0x1F384
   - Best for small messages
   - Example: `"Hi" → 🍅🍆🍇`

2. **Light Meal (Base-128)** 🎰
   - Uses activity emojis
   - Range: 0x1F3B0-0x1F42F
   - Good for medium messages
   - Example: `"Hi" → 🎰🎱`

3. **Classic Recipe (Base-256)** 😀
   - Uses smiley emojis
   - Range: 0x1F600-0x1F6FF
   - Efficient for ASCII text
   - Example: `"Hi" → 😀😃`

4. **Gourmet Special (Base-1024)** 🤠
   - Uses extended emoji set
   - Range: 0x1F900-0x1F9FF
   - Best compression ratio
   - Example: `"Hi" → 🤠`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/FreddyRodgers/emojichef-v1.git
cd emojichef-v1
```

2. Ensure you have Python 3.6 or later installed:
```bash
python --version
```

3. No additional dependencies required! The script uses only Python standard library.

## Usage

Run the script:
```bash
python emojichef-v1.py
```

## Interactive Menu

```
=== EmojiChef's Kitchen ===
1. Cook up an encoded message
2. Taste test (decode) a message
3. Change recipe type
4. Check the ingredients
5. Leave the kitchen
=========================
```

### Menu Options

1. **Cook (Encode)**
   ```
   > Select your cooking method (1-5): 1
   > Enter your message to cook: Hello, World!
   
   Fresh from the kitchen: 😀😃😄😁😆😅
   Original ingredients: 13 bytes
   Cooked size: 6 emojis
   Recipe efficiency: 0.46
   ```

2. **Taste Test (Decode)**
   ```
   > Select your cooking method (1-5): 2
   > Paste the emoji dish to taste: 😀😃😄😁😆😅
   
   Original recipe: Hello, World!
   ```

3. **Change Recipe**
   ```
   > Select your cooking method (1-5): 3
   
   Available recipes:
   1. Quick Bite (base-64 with food emojis)
   2. Light Meal (base-128 with activity emojis)
   3. Classic Recipe (base-256 with smileys)
   4. Gourmet Special (base-1024 with extended set)
   ```

4. **Check Ingredients**
   ```
   > Select your cooking method (1-5): 4
   
   Current recipe: classic
   Pantry size: 256 ingredients
   Bits per emoji: 8.0
   
   Sample ingredients:
   😀 😃 😄 😁 😆 😅 😂 🤣
   ```

## API Reference

### EmojiCodec Class

```python
class EmojiCodec:
    def __init__(self, recipe_type: str = "classic"):
        """
        Initialize encoder with specified recipe type
        
        Args:
            recipe_type: "quick_bite", "light_meal", "classic", or "gourmet"
        """
        pass
    
    def encode(self, data: str) -> str:
        """
        Encode a string into emoji representation
        
        Args:
            data: Input string to encode
            
        Returns:
            Emoji-encoded string
        """
        pass
    
    def decode(self, emoji_data: str) -> str:
        """
        Decode emoji representation back to original string
        
        Args:
            emoji_data: Emoji string to decode
            
        Returns:
            Decoded string
        """
        pass
    
    def get_stats(self, original: str, encoded: str) -> Dict[str, float]:
        """
        Calculate encoding statistics
        
        Returns:
            Dictionary containing:
            - original_bytes: Original size in bytes
            - encoded_length: Number of emojis
            - actual_ratio: Actual compression ratio
            - theoretical_ratio: Theoretical compression ratio
            - bits_per_emoji: Bits represented per emoji
        """
        pass
```

## Usage Examples

### Basic Text Encoding

```python
# Create codec with default settings (classic recipe)
codec = EmojiCodec()

# Encode text
message = "Hello, World!"
encoded = codec.encode(message)
print(f"Encoded: {encoded}")  # Output: 😀😃😄😁😆😅

# Decode text
decoded = codec.decode(encoded)
print(f"Decoded: {decoded}")  # Output: Hello, World!
```

### Using Different Recipes

```python
# Quick Bite (Base-64)
quick_codec = EmojiCodec("quick_bite")
encoded = quick_codec.encode("Hi!")
print(encoded)  # Output: 🍅🍆🍇

# Light Meal (Base-128)
light_codec = EmojiCodec("light_meal")
encoded = light_codec.encode("Hi!")
print(encoded)  # Output: 🎰🎱

# Gourmet Special (Base-1024)
gourmet_codec = EmojiCodec("gourmet")
encoded = gourmet_codec.encode("Hi!")
print(encoded)  # Output: 🤠
```

### Getting Statistics

```python
codec = EmojiCodec()
message = "Hello, World!"
encoded = codec.encode(message)
stats = codec.get_stats(message, encoded)

print(f"Original size: {stats['original_bytes']} bytes")
print(f"Encoded size: {stats['encoded_length']} emojis")
print(f"Compression ratio: {stats['actual_ratio']:.2f}")
print(f"Bits per emoji: {stats['bits_per_emoji']:.1f}")
```

## Best Practices

1. **Choosing Recipe Types**
   - Quick Bite: Best for very short messages
   - Light Meal: Good for medium-length messages
   - Classic: Best for ASCII text
   - Gourmet: Best for longer messages

2. **Error Handling**
   ```python
   try:
       encoded = codec.encode(message)
   except ValueError as e:
       print(f"Encoding error: {e}")
   ```

3. **Recipe Comparison**
   ```python
   message = "Test message"
   recipes = ["quick_bite", "light_meal", "classic", "gourmet"]
   
   for recipe in recipes:
       codec = EmojiCodec(recipe)
       encoded = codec.encode(message)
       stats = codec.get_stats(message, encoded)
       print(f"{recipe}: {stats['actual_ratio']:.2f}")
   ```

## Troubleshooting

### Common Issues

1. **Invalid Characters**
   - Error: "Kitchen accident while encoding: invalid encoding"
   - Solution: Ensure input text is valid UTF-8

2. **Incorrect Decoding**
   - Error: "Tasting error: invalid emoji sequence"
   - Solution: Use complete emoji sequences without modifications

3. **Recipe Not Found**
   - Error: "Unknown recipe type"
   - Solution: Use only supported recipe types

## Planned Features ([v2](https://github.com/FreddyRodgers/emojichef) progress)

- [X] File input/output support
- [ ] Custom emoji mapping definitions
- [ ] Support ecoji 2.0 (base 1024) encoding scheme
- [X] Data compression integration
- [X] Error correction codes
- [ ] Streaming support for large files
- [ ] Configuration file support
- [X] Additional encoding bases

## ⚠️ Important [Security Notice](docs/emojichef-security-notice.md): Encoding vs. Encryption

## Acknowledgments

- Inspired by [Wingdings](https://en.wikipedia.org/wiki/Wingdings), [CyberChef](https://github.com/gchq/CyberChef), and the prior experimental emoji encoding schemes 
   - emojicoding (Base1024): [https://github.com/shea256/emojicoding](https://github.com/shea256/emojicoding)
   - Ecoji 2.0 (Base1024): [https://github.com/keith-turner/ecoji](https://github.com/keith-turner/ecoji)
- Motivated by [Mr. Jeff the Man](https://x.com/MrJeffMan), [shmoocon](https://shmoocon.org) lobbycon, and [nyxgeek](https://x.com/nyxgeek) 
- Special thanks to the emoji standards committee and Claude 3.5 Sonnet

## Contact

- Project Link: [https://github.com/FreddyRodgers/emojichef-v1](https://github.com/FreddyRodgers/emojichef-v1)

## Version History

### v1.0 (2025-01-17)
- Initial release using concepts iterated overtime
- Four encoding bases (64, 128, 256, 1024)
- Interactive menu interface
- Basic statistics
- Colorful terminal output

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.MD) file for details.