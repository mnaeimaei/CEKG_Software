import * as c24Module from "./C27_neo4j_activityProperties_Module.js";


document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C24 is ready!");



        c24Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c24Module.formDiv.submit(); // Submit the form
        });


    }
);