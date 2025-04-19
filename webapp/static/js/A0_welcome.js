import * as a0Module from "./A0_welcome_Module.js";
import {startButton} from "./A0_welcome_Module.js";


document.addEventListener('DOMContentLoaded', function () {


        console.log("Document Welcome is ready!");





        a0Module.startButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            a0Module.formDiv.submit(); // Submit the form
        });


    }
);