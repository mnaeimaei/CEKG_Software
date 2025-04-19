import * as c32Module from "./C43_neo4j_DK4_Module.js";




document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C32 is ready!");


        c32Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c32Module.formDiv.submit(); // Submit the form
        });


    }
);