from flask import Flask, request, jsonify, redirect, render_template
import random
import string

app = Flask(__name__)

# Dicionário para armazenar os links encurtados temporariamente
url_mapping = {}

def generate_short_url():
    """Gera um código curto aleatório de 6 caracteres"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/')
def home():
    """Serve a página inicial"""
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    original_url = data.get("url")
    
    if not original_url:
        return jsonify({"error": "URL inválida"}), 400
    
    short_code = generate_short_url()
    url_mapping[short_code] = original_url
    
    return jsonify({"short_url": f"http://127.0.0.1:5000/{short_code}"})

@app.route('/<short_code>')
def redirect_to_url(short_code):
    """Redireciona para a URL original"""
    original_url = url_mapping.get(short_code)
    if original_url:
        return redirect(original_url)
    return jsonify({"error": "URL não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
