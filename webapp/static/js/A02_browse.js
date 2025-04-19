
document.addEventListener('DOMContentLoaded', function () {

     const runButton = document.getElementById('runButton');


 const nextButton = document.getElementById('nextButton');

 const divRunButton = document.getElementById('downloadButtonDiv');


 const divNextButton = document.getElementById('nextButtonDiv');


 const progressBar = document.getElementById('progressBar');

 const progressBarDiv = document.getElementById('progressBarDiv');

 const formDiv = document.getElementById('allFormA02');

 const softwareProtocolElement = document.getElementById('softProtocol');

 const softwareProtocol = softwareProtocolElement.getAttribute('data-g-prot');

 const fileInput = document.getElementById('fileInput');

 const fileInputE = document.getElementById('fileInputError');


//////////////////////////////////////////////////////////////




function setupWebSocketProgressBarChannelProgressBar(wsProtocol, regex, targetProgressBar, runDiv, nextDiv, progressBarDiv) {
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
            console.log("Progress greater than 0.01%");
            runDiv.style.display = 'none'; // Hide the "Run Scripts" button
            progressBarDiv.style.display = 'block';
        }

        if (progress === 100) {
            console.log("Progress equal to 100%");
            nextDiv.style.display = 'block'; // Show the "Next Page" button
            progressBarDiv.style.display = 'none';
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



function handleFormSubmissionChannelDownload(socket, button, fileInputE) {
    button.addEventListener('click', async function (event) {
        event.preventDefault();

        const file = fileInput.files[0];

        fileInputE.style.display = 'none';
        fileInputE.innerText = '';

        if (!file) {
            // Show error message if no file is selected
            fileInputE.style.display = 'block';
            fileInputE.innerText = 'Please choose a file before uploading.';
            return;
        }

        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                const fileContent = e.target.result.split(',')[1];  // Get Base64 part
                const fileName = file.name;
                socket.send(JSON.stringify({
                    action: 'upload_file',
                    file_name: fileName,
                    file_content: fileContent
                }));
            };
            reader.readAsDataURL(file);  // Read file as Data URL (Base64 encoded)
        }
    });
}






    const socket = setupWebSocketProgressBarChannelProgressBar(softwareProtocol, 'progressA02', progressBar, divRunButton, divNextButton, progressBarDiv);

    handleFormSubmissionChannelDownload(socket, runButton, fileInputE);

    nextButton.addEventListener('click', function (event) {
        event.preventDefault();  // Prevent the default form submission
        formDiv.submit(); // Submit the form
    });


});