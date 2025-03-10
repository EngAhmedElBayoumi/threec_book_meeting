document.addEventListener("DOMContentLoaded", function() {
    let extraField = document.querySelector("#id_extra_fields");

    if (extraField) {
        try {
            let data = JSON.parse(extraField.value || "{}");

            // Create a styled container
            let container = document.createElement("div");
            container.id = "extra-fields-container";
            container.classList.add("extra-fields-box");

            Object.keys(data).forEach((key) => {
                addField(container, key, data[key]);
            });

            extraField.style.display = "none";  // Hide raw JSON textarea
            extraField.parentNode.insertBefore(container, extraField);

            // Styled Add Field Button
            let addButton = document.createElement("button");
            addButton.innerText = "➕ Add Field";
            addButton.type = "button";
            addButton.classList.add("btn", "btn-success", "add-extra-field");
            addButton.onclick = function() {
                addField(container, "", "");
            };

            extraField.parentNode.insertBefore(addButton, extraField);
        } catch (e) {
            console.error("Invalid JSON in extra_fields");
        }

        // Update JSON before submitting the form
        extraField.form.addEventListener("submit", function() {
            let newData = {};
            document.querySelectorAll(".extra-field").forEach((input) => {
                let key = input.querySelector(".key").value.trim();
                let value = input.querySelector(".value").value.trim();
                if (key) newData[key] = value;
            });
            extraField.value = JSON.stringify(newData, null, 2);
        });
    }
});

// Function to Add Input Fields with Better Design
function addField(container, key, value) {
    let div = document.createElement("div");
    div.classList.add("extra-field");

    let keyInput = document.createElement("input");
    keyInput.type = "text";
    keyInput.classList.add("key", "form-control");
    keyInput.placeholder = "Field Name (Key)";
    keyInput.value = key;

    let valueInput = document.createElement("input");
    valueInput.type = "text";
    valueInput.classList.add("value", "form-control");
    valueInput.placeholder = "Field Value";
    valueInput.value = value;

    let removeButton = document.createElement("button");
    removeButton.innerHTML = "❌ Remove";
    removeButton.type = "button";
    removeButton.classList.add("btn", "btn-danger", "remove-extra-field");
    removeButton.onclick = function() {
        div.remove();
    };

    div.appendChild(keyInput);
    div.appendChild(valueInput);
    div.appendChild(removeButton);
    container.appendChild(div);
}
