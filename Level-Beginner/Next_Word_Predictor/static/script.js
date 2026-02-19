const inputBox = document.getElementById("inputBox");
const suggestionsDiv = document.getElementById("suggestions");

let debounceTimer = null;

inputBox.addEventListener("input", function () {

    clearTimeout(debounceTimer);

    debounceTimer = setTimeout(async () => {

        const text = inputBox.value;

        if (text.trim() === "") {
            suggestionsDiv.innerHTML = "";
            return;
        }

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        displaySuggestions(data.suggestions);

    }, 200); // 200ms debounce

});

function displaySuggestions(words) {

    suggestionsDiv.innerHTML = "";

    words.forEach(word => {

        const span = document.createElement("span");
        span.className = "suggestion-item";
        span.textContent = word;

        span.onclick = () => {
            insertSuggestion(word);
        };

        suggestionsDiv.appendChild(span);

    });
}

function insertSuggestion(word) {

    let currentText = inputBox.value.trim();

    if (currentText === "") return;

    inputBox.value = currentText + " " + word;
    inputBox.focus();

    suggestionsDiv.innerHTML = "";
}
