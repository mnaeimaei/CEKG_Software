import * as c21Module from "./C21_neo4j_EventLog_Module.js";

document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C21 is ready!");



        c21Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c21Module.formDiv.submit(); // Submit the form
        });


    }
);