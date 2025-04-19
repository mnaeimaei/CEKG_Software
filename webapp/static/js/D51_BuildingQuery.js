import * as d36Module from "./D51_BuildingQuery_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";


document.addEventListener('DOMContentLoaded', function () {


        console.log("Document D36 is ready!");




        d36Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            d36Module.formDiv.submit(); // Submit the form
        });


    }
);