document.getElementById("formLogin").addEventListener("submit", function(event) {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value.trim();

    if (email === "teste@gmail.com" && senha === "123456") {
        window.location.href = "produtos.html";
    } else {
        document.getElementById("mensagem").textContent =
            "E-mail ou senha incorretos!";
    }
});