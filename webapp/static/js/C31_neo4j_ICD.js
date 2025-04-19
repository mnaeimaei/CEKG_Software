import * as c26Module from "./C31_neo4j_ICD_Module.js";


document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C26 is ready!");


        c26Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c26Module.formDiv.submit(); // Submit the form
        });


    }
);