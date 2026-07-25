"use strict";

document.getElementById("btn-print")?.addEventListener("click", () => {
  window.print();
});

const photoInput = document.getElementById("photo-input");
const photo = document.getElementById("photo");

photoInput?.addEventListener("change", (e) => {
  const file = e.target.files?.[0];
  if (!file || !photo) return;
  const url = URL.createObjectURL(file);
  photo.src = url;
});

document.querySelectorAll('[contenteditable="true"]').forEach((el) => {
  el.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey && el.tagName !== "UL" && !el.classList.contains("prose")) {
      e.preventDefault();
      el.blur();
    }
  });
});

/* Režim exportu: index.html?pdf=1 — jen A4 CV, bez toolbaru */
if (new URLSearchParams(location.search).has("pdf")) {
  document.documentElement.classList.add("pdf-export");
  document.body.style.background = "#fff";
  document.querySelector(".toolbar")?.remove();
  const cv = document.getElementById("cv");
  if (cv) {
    cv.style.margin = "0";
    cv.style.boxShadow = "none";
  }
}
