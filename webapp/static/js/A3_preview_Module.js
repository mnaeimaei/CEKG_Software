
export const applyButton = document.querySelector('#applyButtonDiv input[name="ApplyButtonMode"]');


export const nextButton = document.querySelector('#nextButton3Div input[name="NxButtonMode"]');
export const divApplyButton = document.getElementById('applyButtonDiv');

export const divNextButton = document.getElementById('nextButton3Div');





 export  const optionsContainer = document.getElementById('optionsContainer');
 export    const optionsToShow = JSON.parse(optionsContainer.getAttribute('data-options'));


 export     const optionsContainerDefault = document.getElementById('optionsContainerDefault');
 export    const optionsToShowDefault = JSON.parse(optionsContainerDefault.getAttribute('data-options-default'));


function updateDropdownVisibility(optionsToShow,optionsToShowDefault) {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach((dropdown) => {
        dropdown.style.display = 'none'; // Hide all dropdowns initially
        dropdown.querySelector('select').disabled = true; // Disable them
    });

    optionsToShow.forEach((option, index) => {
        const dropdownElement = document.getElementById(option);
        if (dropdownElement) {
            dropdownElement.style.display = 'block'; // Show the dropdown
            const selectElement = dropdownElement.querySelector('select');
            if (selectElement) {
                selectElement.disabled = false; // Enable the select element for submission
                // Set the value based on optionsToShowDefault
                const defaultValue = optionsToShowDefault[index];
                // Assuming you have the text values as options in your select
                for (let option of selectElement.options) {
                    if (option.text === defaultValue) {
                        option.selected = true;
                        break;
                    }
                }
            }
        }
    });
}

export { updateDropdownVisibility };

export const progressBar = document.getElementById('progressBar');
export const formDiv = document.getElementById('allForm3');

 export const softwareProtocolElement = document.getElementById('softProtocol');

export const softwareProtocol = softwareProtocolElement.getAttribute('data-g-prot');
