const inputBox = document.getElementById("inputBox");
const suggestionsDiv = document.getElementById("suggestions");

let debounceTimer = null;

inputBox.addEventListener("keyup", function (event) {

    // 🔥 Only trigger correction when SPACE is pressed
    if (event.key !== " ") {
        return;
    }

    clearTimeout(debounceTimer);

    debounceTimer = setTimeout(async () => {

        const text = inputBox.value;

        if (text.trim() === "") {
            suggestionsDiv.innerHTML = "";
            return;
        }

        try {

            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ text: text })
            });

            const data = await response.json();

            // 🔥 Replace ONLY if correction exists
            if (data.corrected && data.corrected !== text) {
                inputBox.value = data.corrected + " ";
            }

            displaySuggestions(data.suggestions);

        } catch (error) {
            console.error("Prediction error:", error);
        }

    }, 150);

});


function displaySuggestions(words) {

    suggestionsDiv.innerHTML = "";

    if (!words || words.length === 0) return;

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

    inputBox.value = currentText + " " + word + " ";
    inputBox.focus();

    suggestionsDiv.innerHTML = "";
}