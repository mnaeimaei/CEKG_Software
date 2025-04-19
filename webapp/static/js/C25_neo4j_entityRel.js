import * as c23Module from "./C25_neo4j_entityRel_Module.js";


document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C23 is ready!");


        c23Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c23Module.formDiv.submit(); // Submit the form
        });


    }
);