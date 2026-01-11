# Basic Caesar cipher that can encrypt or decrypt text
def caesar(text, shift, encrypt=True):

    # Make sure the shift value makes sense
    if not isinstance(shift, int):
        return "Shift must be an integer."

    if shift < 1 or shift > 25:
        return "Shift must be between 1 and 25."

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Flip the shift for decryption
    if not encrypt:
        shift = -shift

    # Build the shifted alphabet
    shifted = alphabet[shift:] + alphabet[:shift]

    # Create a translation map for both lowercase and uppercase
    table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted + shifted.upper()
    )

    # Apply the translation
    return text.translate(table)


# Simple wrappers for clarity
def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


# Test example (ROT13)
encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)

# Final Output
print(decrypted_text)
print(encrypted_text)
