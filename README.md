## AI Image Generator

🖼️ AI Image Generator is a web application that generates images from text prompts using HuggingFace image generation models.

## 🚀 Features


Generate images from a text prompt.

Simple and colorful web interface using Flask and Tailwind CSS.

Can be tested locally or with Docker.

Compatible with Stability AI / Stable Diffusion models.

## 🛠️ Installation & Usage

1️⃣ Clone the project
```bash

git clone https://github.com/Islem-1/ia_image.git
cd AI-Image-Generator

2️⃣ Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

3️⃣ Configure your HuggingFace token

Create a .env file or modify app.py:

HF_TOKEN = "your_huggingface_token"

4️⃣ Run the Flask app
python app.py


Open your browser: http://localhost:5000

## 🐳 Docker
1️⃣ Build the Docker image
docker build -t islem55/ai-image-generator:latest .

2️⃣ Run the container locally
docker run -p 5000:5000 islem55/ai-image-generator:latest

3️⃣ Push to Docker Hub
docker push islem55/ai-image-generator:latest


Pull and run on any machine:

docker pull islem55/ai-image-generator:latest
docker run -p 5000:5000 islem55/ai-image-generator:latest
