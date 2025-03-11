from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailfenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Caesar Cipher
caesar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = data.get('key')
    if not plain_text or not key:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    if not cipher_text or not key:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Vigenere Cipher
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = data.get('key')
    if not plain_text or not key:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    if not cipher_text or not key:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Railfence Cipher
railfence_cipher = RailfenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = data.get('key')
    if not plain_text or not key:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    if not cipher_text or not key:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Playfair Cipher
playfair_cipher = PlayfairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.get_json()
    key = data.get('key')
    if not key:
        return jsonify({'error': 'Missing key'}), 400
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = data.get('key')
    if not plain_text or not key:
        return jsonify({'error': 'Missing plain_text or key'}), 400
    encrypted_text = playfair_cipher.encrypt(plain_text, key)  # Sử dụng encrypt trực tiếp
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    if not cipher_text or not key:
        return jsonify({'error': 'Missing cipher_text or key'}), 400
    decrypted_text = playfair_cipher.decrypt(cipher_text, key)  # Sử dụng decrypt trực tiếp
    return jsonify({'decrypted_text': decrypted_text})

transposition_cipher = TranspositionCipher()
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
if __name__ == '__main__':
    # Lưu ý: Không sử dụng debug=True trong môi trường sản xuất
    app.run(host="0.0.0.0", port=5000, debug=True)