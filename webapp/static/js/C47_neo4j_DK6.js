import * as c34Module from "./C47_neo4j_DK6_Module.js";



document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C34 is ready!");


        c34Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c34Module.formDiv.submit(); // Submit the form
        });


    }
);