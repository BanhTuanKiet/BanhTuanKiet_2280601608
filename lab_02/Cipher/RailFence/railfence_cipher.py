class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, key):
        rails = [[] for _ in range(key)]
        rail_index = 0
        direction = 1
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text
    
    def rail_fence_decrypt(self, plain_text, key):
        rail_lengths = [0] * key
        rail_index = 0
        direction = 1
        for _ in range(len(plain_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction
            
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(plain_text[start:start+length])
            start += length
            
        text = ""
        rail_index = 0
        direction = 1
        
        for _ in range(len(plain_text)):
            text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction
            
        return text