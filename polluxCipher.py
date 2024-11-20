import random

# Morse code mappings
morse_map = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", ", ": "--..--", ".": ".-.-.-",
    "?": "..--..", "/": "-..-.", "-": "-....-", "(": "-.--.", ")": "-.--.-"
}
morse_to_char_map = {v: k for k, v in morse_map.items()}

# Pollux cipher mappings
morse_to_num_map = {
    ".": ["0", "3", "7", "8", "A", "E", "F", "M", "O", "P", "Q", "X", "Y", "Z"],
    "-": ["1", "4", "5", "B", "C", "G", "J", "N", "R", "T", "W"],
    " ": ["2", "6", "9", "D", "H", "I", "K", "L", "S", "U", "V"]
}


# Create a reverse mapping from numbers/letters to Morse code symbols
# For each Morse symbol (. - space) and its corresponding numbers/letters in morse_to_num_map,
# create an entry mapping each number/letter back to its Morse symbol
num_to_morse_map = {}
for char, nums in morse_to_num_map.items():
    for num in nums:
        num_to_morse_map[num] = char

def text_to_morse(text):
    """
    Converts plain text to Morse code.

    Args:
    text (str): The plain text to convert.

    Returns:
    str: The converted Morse code string.
    """
    morse = ""
    for char in text.upper():
        if char in morse_map:
            morse_code = morse_map[char]
            morse += morse_code + ' '
    return morse.strip()

def morse_to_text(morse):
    """
    Converts Morse code to plain text.

    Args:
    morse (str): The Morse code string to convert.

    Returns:
    str: The converted plain text.
    """
    text = ""
    segments = morse.split(' ')
    for seg in segments:
        if seg in morse_to_char_map:
            character = morse_to_char_map[seg]
            text += character
    return text

def morse_to_num(morse):
    """
    Converts Morse code to a numeric code based on predefined mappings.

    Args:
    morse (str): The Morse code string to convert.

    Returns:
    str: A string of numbers representing the Morse code.
    """
    numbers = ""
    print(f"Starting conversion of Morse code '{morse}' to numeric code.")
    for char in morse:
        if char in morse_to_num_map:
            number = random.choice(morse_to_num_map[char])
            numbers += number
            print(f"Morse '{char}' converted to number '{number}'")
        else:
            print(f"Morse '{char}' not found in mapping, skipped.")
    return numbers

def num_to_morse(nums):
    """
    Converts a numeric code back to Morse code using a reverse mapping.

    Args:
    nums (str): The string of numbers to convert.

    Returns:
    str: The corresponding Morse code.
    """
    morse = ""
    print(f"Starting conversion of numeric code '{nums}' to Morse code.")
    for num in nums:
        if num in num_to_morse_map:
            morse_code = num_to_morse_map[num]
            morse += morse_code
            print(f"Numeric '{num}' converted to Morse '{morse_code}'")
        else:
            print(f"Numeric '{num}' not found in mapping, skipped.")
    return morse

def encode_pollux(text):
    """
    Encodes plain text to a numeric code using Morse code as an intermediary step.

    Args:
    text (str): The plain text to encode.

    Returns:
    str: The numeric code after encoding.
    """
    print(f"Text to encode: {text}")  # Print the input text
    morse = text_to_morse(text)
    print(f"Converted text to Morse: {morse}")  # Print the Morse code obtained from text
    numbers = morse_to_num(morse)
    print(f"Converted Morse to numbers: {numbers}")  # Print the numeric code obtained from Morse
    return numbers

def decode_pollux(nums):
    """
    Decodes a numeric code back to plain text using Morse code as an intermediary step.

    Args:
    nums (str): The numeric code to decode.

    Returns:
    str: The decoded plain text.
    """
    print(f"Numeric code to decode: {nums}")  # Print the input numeric code
    morse = num_to_morse(nums)
    print(f"Converted from numbers to Morse: {morse}")  # Print the Morse code obtained from numbers
    text = morse_to_text(morse)
    print(f"Converted from Morse to text: {text}")  # Print the final decoded text
    return text

def main():
    import sys
    # Open a text file to write the output
    with open("output.txt", "w") as file:
        # Redirect standard output to the file
        sys.stdout = file

        # Testing the functions
        test_string = "CMSC191"
        print("Starting encoding")  # Print the initial test string
        encoded = encode_pollux(test_string)
        print(f"Encoded output: {encoded}")  # Print the encoded result
        print("\n")
        print("Starting decryptio")
        decoded = decode_pollux(encoded)
        print(f"Decoded output: {decoded}")  # Print the decoded result

    # Reset standard output to default
    sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()
