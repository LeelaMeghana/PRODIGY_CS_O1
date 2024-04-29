def caesar_cipher(text, shift, mode):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted = (ord(char) - 65 + shift if mode == 'encrypt' else ord(char) - 65 - shift) % 26 + 65
                encrypted_text += chr(shifted)
            elif char.islower():
                shifted = (ord(char) - 97 + shift if mode == 'encrypt' else ord(char) - 97 - shift) % 26 + 97
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Please choose a valid option.")
            continue

        text = input("Enter the message: ")
        shift = int(input("Enter the shift value (a number between 1 and 25): "))

        if not 1 <= shift <= 25:
            print("Shift value must be between 1 and 25.")
            continue

        if choice == 'encrypt':
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            print("Encrypted message:", encrypted_text)
        else:
            decrypted_text = caesar_cipher(text, shift, 'decrypt')
            print("Decrypted message:", decrypted_text)

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
