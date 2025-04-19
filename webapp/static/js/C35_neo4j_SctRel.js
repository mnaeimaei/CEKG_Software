import * as c28Module from "./C35_neo4j_SctRel_Module.js";


document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C28 is ready!");


        c28Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c28Module.formDiv.submit(); // Submit the form
        });


    }
);