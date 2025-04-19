import * as c25Module from "./C29_neo4j_Domain_Module.js";


document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C25 is ready!");



        c25Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c25Module.formDiv.submit(); // Submit the form
        });


    }
);