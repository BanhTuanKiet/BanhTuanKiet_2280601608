from flask import Flask, request, jsonify
from Cipher.Caesar import CaesarCipher
from Cipher.Vigenere import VigenereCipher
from Cipher.Transposition import TranspositionCipher
from Cipher.RailFence import RailFenceCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()
vigener_cipher = VigenereCipher()
transposition_cipher = TranspositionCipher()
railfence_cipher = RailFenceCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.get_json()  
    encrypted_text = data['plain_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(encrypted_text, key)
    return jsonify({"decrypted_text": decrypted_text})

@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigener_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.get_json()
    encrypted_text = data['plain_text']
    key = data['key']
    decrypted_text = vigener_cipher.decrypt(encrypted_text, key)
    return jsonify({"decrypted_text": decrypted_text})

@app.route("/api/transpositio/encrypt", methods=["POST"])
def transpositio_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/transpositio/decrypt", methods=["POST"])
def transpositio_decrypt():
    data = request.get_json()
    encrypted_text = data.get('plain_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(encrypted_text, key)
    return jsonify({"decrypted_text": decrypted_text})

@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.get_json()
    encrypted_text = data.get('plain_text')
    key = int(data.get('key'))
    decrypted_text = railfence_cipher.rail_fence_decrypt(encrypted_text, key)
    return jsonify({"decrypted_text": decrypted_text})

if __name__ == "__main__":
    app.run(debug=True)
