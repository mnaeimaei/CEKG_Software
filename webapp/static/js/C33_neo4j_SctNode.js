import * as c27Module from "./C33_neo4j_SctNode_Module.js";


document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C27 is ready!");



        c27Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c27Module.formDiv.submit(); // Submit the form
        });


    }
);