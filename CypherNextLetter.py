def next_letter_cipher(message):
    # Define the normal and next letter set alphabets
    normal_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reversed_alphabet = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'

    # Create a translation table using maketrans
    translation_table = str.maketrans(normal_alphabet, reversed_alphabet)

    # Translate the message using the translation table
    translated_message = message.translate(translation_table)

    return translated_message


# Example usage:
message = input('Enter message: ')
words = message.split(' ')
print(words)
encrypted_message_word = []
for word in words:
    if len(word.strip()) > 0:
        encrypted_message_word.append(next_letter_cipher(word.upper()))
print("Original Message:", message)
print("Encrypted Message:", encrypted_message_word)

