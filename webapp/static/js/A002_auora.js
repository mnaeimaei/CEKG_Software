import * as p2Module from "./A002_auora_Module.js";



document.addEventListener('DOMContentLoaded', function () {
    console.log("Document 2.1 is ready!");


     p2Module.uriForm.value = p2Module.deafaultUri;
        p2Module.userForm.value = p2Module.deafaultUser;
    p2Module.passForm.value = p2Module.defaultPass;

            p2Module.uriForm.required = true;
        p2Module.userForm.required = true;
    p2Module.passForm.required = true;


p2Module.formUpload.addEventListener('submit', function(event) {
    if (!p2Module.userForm.checkValidity() || !p2Module.passForm.checkValidity()) {
        event.preventDefault();  // This stops the form from submitting if it's not valid
        console.log("Form validation failed");
    } else {
        console.log("Form is valid, submitting");
    }
});


});




