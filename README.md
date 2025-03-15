Encurtador de Links 🔗

Projeto de um encurtador de links simples usando Python (Flask), HTML, CSS e JavaScript. Permite encurtar URLs e redirecionar automaticamente quando um link encurtado é acessado.

📸 Imagem do Projeto
![Amigo Secreto!!!](https://github.com/coliveira1977/desafio_amigo_secreto/blob/mai/assets/amigo-secreto.png?raw=true)


🚀 Tecnologias Utilizadas

Flask (Python) - Backend para gerar e gerenciar links curtos.

HTML, CSS e JavaScript - Frontend simples e responsivo.

📂 Estrutura de Pastas

encurtador/
│── app.py               # Backend Flask
│── requirements.txt      # Dependências do projeto
│── static/               # Arquivos estáticos (CSS, JS, imagens)
│   │── styles.css        # Estilos
│   │── script.js         # Lógica do frontend
│── templates/            # HTML renderizado pelo Flask
│   │── index.html        # Página principal
│   │── print.png         # Screenshot do projeto
│── README.md             # Documentação

🛠️ Instalação e Execução

1️⃣ Clone o repositório

git clone https://github.com/coliveira1977/encurtador-de-links.git
cd encurtador-de-links

2️⃣ Crie um ambiente virtual (opcional, mas recomendado)

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

3️⃣ Instale as dependências

pip install -r requirements.txt

4️⃣ Execute o servidor

python app.py

5️⃣ Abra o navegador e acesse:

http://127.0.0.1:5000/

📜 Principais Trechos do Código

🔹 Backend (Flask - app.py)

from flask import Flask, request, jsonify, redirect, render_template
import random
import string

app = Flask(__name__)
url_mapping = {}

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    original_url = data.get("url")
    short_code = generate_short_url()
    url_mapping[short_code] = original_url
    return jsonify({"short_url": f"http://127.0.0.1:5000/{short_code}"})

@app.route('/<short_code>')
def redirect_to_url(short_code):
    return redirect(url_mapping.get(short_code, '/'))

🔹 Frontend (HTML - index.html)

<input type="text" id="urlInput" placeholder="Cole sua URL aqui...">
<button onclick="shortenUrl()">Encurtar</button>
<p id="shortenedUrl"></p>

🔹 Frontend (JavaScript - script.js)

async function shortenUrl() {
    const urlInput = document.getElementById("urlInput").value;
    const response = await fetch("/shorten", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: urlInput })
    });
    const result = await response.json();
    document.getElementById("shortenedUrl").innerHTML = `<a href="${result.short_url}" target="_blank">${result.short_url}</a>`;
}

📌 Melhorias Futuras

✅ Botão para copiar o link encurtado.✅ Banco de dados para persistência dos links.✅ Interface aprimorada com Bootstrap.

✍️ Autor

Christian Oliveira (coliveira1977)📧 Email: chr.oliveira@gmail.com🔗 GitHub: coliveira1977

📝 Licença: MIT 📜
