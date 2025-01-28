def reverse_letter_cipher(message):
    # Define the normal and reversed alphabets
    normal_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reversed_alphabet = normal_alphabet[::-1]

    # Create a translation table using maketrans
    translation_table = str.maketrans(normal_alphabet, reversed_alphabet)

    # Translate the message using the translation table
    translated_message = message.translate(translation_table)

    return translated_message


# Example usage:
message = input('Enter message: ')
words = message.split(' ')

encrypted_message_word = []
for word in words:
    if len(word.strip()) > 0:
        encrypted_message_word.append(reverse_letter_cipher(word.upper()))
print("Original Message:", message)
print("Encrypted Message:", encrypted_message_word)

