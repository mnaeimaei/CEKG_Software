//export const progressBar = document.getElementById('progressBar');
//export const form2 = document.getElementById('allForm2');


//import * as p2Module from "./A2_Module_downloading";

//progressBarModule.handleFormSubmission(ws, p2Module.nextButton2FormSubmit, p2Module.form2);

function setupWebSocketProgressBarChannel(wsProtocol, regex, targetProgressBar, runDiv, nextDiv) {
    const socketURL = `${wsProtocol}://${window.location.host}/ws/${regex}/`;
    console.log("socketURL" + socketURL);

    const socket = new WebSocket(socketURL);
    //const socket = new WebSocket(wsProtocol + window.location.host + '/ws/progressC20/');
    socket.onopen = function (e) {
        console.log("WebSocket connection established.");
    };
    socket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        const progress = data.progress;
        console.log("Progress in JS: " + progress);
        targetProgressBar.style.width = progress + '%';
        targetProgressBar.innerText = progress + '% Complete';

        if (progress > 1) {
            console.log("Progress greater than 1%");
            runDiv.style.display = 'none'; // Hide the "Run Scripts" button
        }

        if (progress === 100) {
            console.log("Progress equal to 100%");
            nextDiv.style.display = 'block'; // Show the "Next Page" button
        }
    };
    socket.onclose = function (event) {
        if (event.wasClean) {
            console.log(`Closed cleanly, code=${event.code}, reason=${event.reason}`);  //Stopping all processes with SIGTERM in Heroku
        } else {
            console.log('Connection died'); //At the beginning of the loading the page
            window.location.reload();
        }
    };
    socket.onerror = function (error) {
        console.error("WebSocket error: ", error);
    };
    return socket;
}

export {setupWebSocketProgressBarChannel};

function handleFormSubmissionChannel(socket, button) {
    button.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default form submission
        // WebSocket connection must be established and listening before the form is submitted
        if (socket.readyState === WebSocket.OPEN) {
            console.log("WebSocket.OPEN");
            socket.send('run_scripts');
        } else {
            console.log("WebSocket.else");
            socket.onopen = function () {
                socket.send('run_scripts');
            };
        }
    });
}


export {handleFormSubmissionChannel};


function setupWebSocketProgressBarChannelLong(wsProtocol, regex, targetProgressBar, runDiv, nextDiv) {
    const socketURL = `${wsProtocol}://${window.location.host}/ws/${regex}/`;
    console.log("socketURL" + socketURL);

    const socket = new WebSocket(socketURL);
    //const socket = new WebSocket(wsProtocol + window.location.host + '/ws/progressC20/');
    socket.onopen = function (e) {
        console.log("WebSocket connection established.");
    };
    socket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        const progress = data.progress;
        console.log("Progress in JS: " + progress);
        targetProgressBar.style.width = progress + '%';
        targetProgressBar.innerText = progress + '% Complete';

        if (progress === 10 || progress === 20 || progress === 30 ||progress === 40 || progress === 50 || progress === 60 || progress === 70 || progress === 80 || progress === 90) {
            console.log("Reloading at " + progress + "% progress");
            window.location.reload();
        }


        if (progress > 1) {
            console.log("Progress greater than 1%");
            runDiv.style.display = 'none'; // Hide the "Run Scripts" button
        }

        if (progress === 100) {
            console.log("Progress equal to 100%");
            nextDiv.style.display = 'block'; // Show the "Next Page" button
        }
    };
    socket.onclose = function (event) {
        if (event.wasClean) {
            console.log(`Closed cleanly, code=${event.code}, reason=${event.reason}`);  //Stopping all processes with SIGTERM in Heroku
        } else {
            console.log('Connection died'); //At the beginning of the loading the page
            window.location.reload();
        }
    };
    socket.onerror = function (error) {
        console.error("WebSocket error: ", error);
    };
    return socket;
}

export {setupWebSocketProgressBarChannelLong};

