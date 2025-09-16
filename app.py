from flask import Flask, render_template, request, jsonify
import requests
import base64

app = Flask(__name__)

HF_TOKEN = "your HuggingFace token"  # <-- ton token HuggingFace

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {"inputs": prompt}

    try:
        # URL mise à jour pour le nouveau modèle Stable Diffusion XL
        response = requests.post(
            "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
            headers=headers,
            json=payload,
            timeout=120  # XL peut prendre un peu plus de temps
        )
        response.raise_for_status()

        # HuggingFace retourne l'image en blob
        image_bytes = response.content
        # Convertir en base64 pour envoyer au frontend
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")
        return jsonify({"image": f"data:image/png;base64,{image_base64}"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
