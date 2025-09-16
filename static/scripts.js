async function generateImage() {
  const prompt = document.getElementById("prompt").value;
  const loading = document.getElementById("loading");
  const resultImage = document.getElementById("resultImage");

  if (!prompt) {
    alert("⚠️ Please enter a prompt!");
    return;
  }

  loading.classList.remove("hidden");
  resultImage.classList.add("hidden");

  try {
    const response = await fetch("/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });

    const data = await response.json();

    if (data.error) throw new Error(data.error);

    resultImage.src = data.image;
    resultImage.classList.remove("hidden");
  } catch (err) {
    alert("Error: " + err.message);
  } finally {
    loading.classList.add("hidden");
  }
}
