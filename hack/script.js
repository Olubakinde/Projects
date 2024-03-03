// JavaScript code for handling registration form submission goes here
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("registration-form");
    const loader = document.getElementById("loader");
    const message = document.getElementById("message");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const name = document.getElementById("name").value;
        const studentId = document.getElementById("student_id").value;
        const email = document.getElementById("email").value;
        const photo = document.getElementById("photo").files[0];

        if (name.trim() === "" || studentId.trim() === "" || email.trim() === "" || !photo) {
            showMessage("Please fill in all fields and upload a photo.", "error");
            return;
        }

        const formData = new FormData();
        formData.append("name", name);
        formData.append("student_id", studentId);
        formData.append("email", email);
        formData.append("photo", photo);

        loader.style.display = "block";
        message.style.display = "none";

        fetch("register.php", {
            method: "POST",
            body: formData
        })
        .then(response => {
            loader.style.display = "none";
            if (response.ok) {
                form.reset();
                showMessage("Registration successful!", "success");
            } else {
                throw new Error("Registration failed.");
            }
        })
        .catch(error => {
            loader.style.display = "none";
            console.error("Error:", error);
            showMessage("Registration failed. Please try again later.", "error");
        });
    });

    function showMessage(msg, type) {
        message.textContent = msg;
        message.className = type;
        message.style.display = "block";
    }
});
