import * as c31Module from "./C41_neo4j_DK3_Module.js";




document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C31 is ready!");


        c31Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c31Module.formDiv.submit(); // Submit the form
        });


    }
);