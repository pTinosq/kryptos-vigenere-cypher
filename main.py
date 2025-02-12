CIPHER_ALPHABET = []
CIPHER_ALPHABET_MATRIX = []
CIPHER_KEYWORD = ""


def main():
    lines = []
    # 1. Load in the cipher alphabet
    with open("kryptos_cipher_alphabet.csv", "r") as f:
        lines = f.readlines()

    # 2. Create the cipher alphabet matrix
    CIPHER_ALPHABET = lines[0].split(",")
    for i in range(len(CIPHER_ALPHABET)):
        CIPHER_ALPHABET_MATRIX.append(CIPHER_ALPHABET[i:] + CIPHER_ALPHABET[:i])

    # 3. Load in the cipher keyword
    with open("cipher_keyword.txt", "r") as f:
        lines = f.readlines()
        CIPHER_KEYWORD = lines[0].strip()

    # 4. Allow user to input plaintext
    plaintext = input("Enter the plaintext: ").upper()

    # 5. Update the keyword to match the length of the plaintext
    # Spaces are not encrypted so will be included in the keyword
    keystream = ""
    keystream_idx = 0
    for z, letter in enumerate(plaintext):
        if letter == " ":
            keystream += " "
        else:
            letter = CIPHER_KEYWORD[keystream_idx % len(CIPHER_KEYWORD)]
            keystream += letter
            keystream_idx += 1

    print(f"keystream: {keystream}")

    # 6. Generate the encrypted message
    encrypted_message = ""
    for z, plaintext_letter in enumerate(plaintext):
        if plaintext_letter == " ":
            encrypted_message += " "

        else:
            keystream_letter = keystream[z]
            # 6.1. Find the cipher alphabet to use using the letter of the plaintext
            cipher_alphabet_matrix_row = CIPHER_ALPHABET_MATRIX[
                CIPHER_ALPHABET.index(plaintext_letter)
            ]  # This will give us the row in the cipher alphabet matrix

            # 6.2. Find the letter using the row and the keystream letter
            letter = cipher_alphabet_matrix_row[CIPHER_ALPHABET.index(keystream_letter)]
            encrypted_message += letter

    print(encrypted_message)


if __name__ == "__main__":
    while True:
        main()
