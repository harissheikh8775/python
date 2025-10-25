# ================================
# 🏛 Caesar Cipher Project
# ================================

# Import the logo art from a separate file
from caesar_cipher_art import logo

# Display the logo
print(logo)

# Define the list of alphabets (can also use string.ascii_lowercase)
alphabets = [chr(i) for i in range(97, 123)]  # 'a' to 'z'


def caesar(original_text, shift_amount, encode_or_decode):

    # Normalize shift to always stay within the alphabet range (0–25)
    shift_amount %= 26

    # Reverse the shift for decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    output_text = ""

    # Process each character in the text
    for letter in original_text:
        if letter.isalpha():  # Only shift alphabets
            # Find new position after shifting
            new_position = (alphabets.index(letter) + shift_amount) % 26
            output_text += alphabets[new_position]
        else:
            # Keep spaces, numbers, and symbols unchanged
            output_text += letter

    # Display the result
    print(f"\nHere is the {encode_or_decode}d result: {output_text}\n")


# Main loop to allow multiple encryptions/decryptions
while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user whether they want to continue
    restart = input("Type 'yes' to go again, or 'no' to exit:\n").lower()
    if restart == "no":
        print("Goodbye! 👋")
        break
