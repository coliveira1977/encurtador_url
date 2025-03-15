async function shortenUrl() {
    const urlInput = document.getElementById("urlInput").value;
    
    if (!urlInput) {
        alert("Por favor, insira uma URL válida.");
        return;
    }

    const response = await fetch("http://127.0.0.1:5000/shorten", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: urlInput })
    });

    const result = await response.json();

    if (result.short_url) {
        document.getElementById("shortenedUrl").innerHTML = `
            Link encurtado: <a href="${result.short_url}" target="_blank">${result.short_url}</a>
        `;
    } else {
        alert("Erro ao encurtar a URL.");
    }
}
