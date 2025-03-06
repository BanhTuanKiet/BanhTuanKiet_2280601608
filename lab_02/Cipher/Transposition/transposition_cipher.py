class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext, key):
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(plaintext):
                encrypted_text += plaintext[pointer]
                pointer += key
        return encrypted_text
    
    def decrypt(self, plaintext, key):
        decrypted_text = [''] * key
        row, col = 0, 0
        for symbol in plaintext:
            decrypted_text[col] += symbol
            col += 1
            if col == key or (col == key - 1 and row >= len(plaintext) % key):
                col = 0
                row += 1
        return ''.join(decrypted_text)