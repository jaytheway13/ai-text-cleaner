async function submitText() {
  const text = document.getElementById("text-input").value;
  const res = await fetch("http://localhost:5000/filter", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  const data = await res.json();
  document.getElementById("output").innerText = data.filtered_text;
}

async function uploadFile() {
  const fileInput = document.getElementById("file-input");
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const res = await fetch("http://localhost:5000/upload", {
    method: "POST",
    body: formData,
  });
  const data = await res.json();
  document.getElementById("text-input").value = data.text;
}
