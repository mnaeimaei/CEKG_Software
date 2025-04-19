import * as c33Module from "./C45_neo4j_DK5_Module.js";



document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C33 is ready!");


        c33Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c33Module.formDiv.submit(); // Submit the form
        });


    }
);