import * as c22Module from "./C23_neo4j_otherEntities_Module.js";


document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C22 is ready!");

        c22Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c22Module.formDiv.submit(); // Submit the form
        });


    }
);