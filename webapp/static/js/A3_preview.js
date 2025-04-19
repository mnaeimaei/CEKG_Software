import * as a3Module from "./A3_preview_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";
import {divApplyButton} from "./A3_preview_Module.js";

document.addEventListener('DOMContentLoaded', function () {

    console.log("Document 3 is ready!");
    console.log(a3Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(a3Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    fetch('/api/excel/')
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            var sheetSelector = document.getElementById('sheetSelector');
            var tableContainer = document.getElementById('tableContainer');

            // Populate the sheet selector dropdown
            for (var sheetName in data) {
                if (data.hasOwnProperty(sheetName)) {
                    var option = document.createElement('option');
                    option.value = sheetName;
                    option.textContent = sheetName;
                    sheetSelector.appendChild(option);
                }
            }

            // Function to render table
            function renderTable(sheetData) {
                if (sheetData.length === 0) {
                    tableContainer.innerHTML = '<p>No data available in this sheet.</p>';
                    return;
                }

                var tableHtml = '<table><thead><tr>';

                // Create table headers
                var headers = Object.keys(sheetData[0]);
                headers.forEach(function(header) {
                    tableHtml += '<th>' + header + '</th>';
                });
                tableHtml += '</tr></thead><tbody>';

                // Create table rows
                sheetData.forEach(function(row) {
                    tableHtml += '<tr>';
                    headers.forEach(function(header) {
                        tableHtml += '<td>' + row[header] + '</td>';
                    });
                    tableHtml += '</tr>';
                });
                tableHtml += '</tbody></table>';

                // Inject the table into the container
                tableContainer.innerHTML = tableHtml;
            }

            // Render the first sheet by default
            renderTable(data[sheetSelector.value]);

            // Add event listener to sheet selector to switch sheets
            sheetSelector.addEventListener('change', function () {
                renderTable(data[this.value]);
            });
        })
        .catch(function(error) {
            console.error('Error fetching Excel data:', error);
        });

    a3Module.updateDropdownVisibility(a3Module.optionsToShow, a3Module.optionsToShowDefault);

    const socket = progressBarModule.setupWebSocketProgressBarChannel(a3Module.softwareProtocol, 'progressA3', a3Module.progressBar, a3Module.divApplyButton, a3Module.divNextButton);



    progressBarModule.handleFormSubmissionChannel(socket, a3Module.divApplyButton);

    a3Module.nextButton.addEventListener('click', function (event) {
        event.preventDefault();  // Prevent the default form submission
        a3Module.formDiv.submit(); // Submit the form
    });


});
