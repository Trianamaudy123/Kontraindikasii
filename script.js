// script.js
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const input = document.querySelector("input[name='obat']");
    const button = document.querySelector(".btn-primary");
    const commentBox = document.querySelector(".comment-box");

    // Animasi tombol saat diklik
    button.addEventListener("mousedown", function() {
        this.style.transform = "scale(0.95)";
    });
    button.addEventListener("mouseup", function() {
        this.style.transform = "scale(1)";
    });

    // Validasi input sebelum submit
    form.addEventListener("submit", function(event) {
        if (input.value.trim() === "") {
            event.preventDefault();
            alert("Nama obat tidak boleh kosong!");
        }
    });

    // Efek saat menulis komentar
    commentBox.addEventListener("focus", function() {
        this.style.borderColor = "#0D47A1";
    });
    commentBox.addEventListener("blur", function() {
        this.style.borderColor = "#1565C0";
    });
});
