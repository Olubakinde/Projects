document.addEventListener("DOMContentLoaded", function() {
    // Retrieve information from the form or any other source
    const name = "John Doe";
    const email = "john@example.com";
    const studentId = "1234567890";
    const uniqueId = `${name}-${email}-${studentId}`;

    // Display the unique ID
    const idInfoElement = document.getElementById("id-info");
    idInfoElement.innerHTML += `<p><strong>Unique ID:</strong> ${uniqueId}</p>`;

    // Generate QR code for the unique ID
    const qrCodeElement = document.getElementById("qrcode");
    new QRCode(qrCodeElement, {
        text: uniqueId,
        width: 128,
        height: 128,
        colorDark: "#000000",
        colorLight: "#ffffff",
        correctLevel: QRCode.CorrectLevel.H
    });
});
