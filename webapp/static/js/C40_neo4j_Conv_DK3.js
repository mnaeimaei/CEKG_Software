import * as c20Module from "./C40_neo4j_Conv_DK3_Mdule.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";


document.addEventListener('DOMContentLoaded', function () {


        console.log("Document C20 is ready!");



        const socket = progressBarModule.setupWebSocketProgressBarChannel(c20Module.softwareProtocol, 'progressC40', c20Module.progressBar, c20Module.divRunButton, c20Module.divNextButton);

        progressBarModule.handleFormSubmissionChannel(socket, c20Module.runButton);

        c20Module.nextButton.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the default form submission
            c20Module.formDiv.submit(); // Submit the form
        });


    }
);