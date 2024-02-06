/* Project specific Javascript goes here. */

function toggleContactFrom() {
    var modal = document.getElementById("modalContactFrom");
    modal.classList.toggle("show");
}

// Call the toggleModal function when a button is clicked
var button = document.getElementById("toggleButton");
button.addEventListener("click", toggleContactFrom);