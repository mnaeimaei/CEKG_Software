import * as c18Module from "./C18_csv_Downloading_Module.js";
import {nextButtonFormSubmit} from "./C18_csv_Downloading_Module.js";






document.addEventListener('DOMContentLoaded', function() {





c18Module.nextButtonFormSubmit.addEventListener('click', function(event) {
event.preventDefault();  // Prevent the default form submission
document.getElementById('allFormC18').submit(); // Submit the form
});


});
