import * as c35Module from "./C49_neo4j_DK7_Module.js";




document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C35 is ready!");



        c35Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c35Module.formDiv.submit(); // Submit the form
        });


    }
);