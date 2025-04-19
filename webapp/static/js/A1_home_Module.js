const AllFormContainer = document.getElementById('allForm');

export const MainDfgFormRadioButtons = document.querySelectorAll('#mainDfgDiv input[name="mainDfgMode"]');  //step1 for all

export const Dfg1FormRadioButtons = document.querySelectorAll('#dFG1Div input[name="dfg1Mode"]'); // step2 for 1
export const Dfg2FormRadioButtons = document.querySelectorAll('#dFG2Div input[name="dfg2Mode"]'); //step2 for 2
export const Dfg3FormRadioButtons = document.querySelectorAll('#dFG3Div input[name="dfg3Mode"]'); //step2 for 3
export const Dfg4FormRadioButtons = document.querySelectorAll('#dFG4Div input[name="dfg4Mode"]'); //step2 for 4
export const Dfg5FormRadioButtons = document.querySelectorAll('#dFG5Div input[name="dfg5Mode"]'); //step2 for 5
export const Dfg6FormRadioButtons = document.querySelectorAll('#dFG6Div input[name="dfg6Mode"]'); //step2 for 6

export const InputFormRadioButtons = document.querySelectorAll('#inputDiv input[name="inputMode"]'); //step3 for 1-5
export const InputFormDFG6RadioButtons = document.querySelectorAll('#inputDFG6Div input[name="inputModeDFG6"]'); //step3 for 6

export const ActivityFormRadioButtons = document.querySelectorAll('#activityDiv input[name="activityMode"]'); //step4 for 1_5
export const ActivityFormRadioButtonsDFG6 = document.querySelectorAll('#activityDFG6Div input[name="activityModeDFG6"]'); //step4 for 6

export const nextButton1FormSubmit = document.querySelectorAll('#nextButton1Div input[name="nextButton1Mode"]');


export const MainDfgDivContainer = document.getElementById('mainDfgDiv');
export const Dfg1DivContainer = document.getElementById('dFG1Div');
export const Dfg2DivContainer = document.getElementById('dFG2Div');
export const Dfg3DivContainer = document.getElementById('dFG3Div');
export const Dfg4DivContainer = document.getElementById('dFG4Div');
export const Dfg5DivContainer = document.getElementById('dFG5Div');
export const Dfg6ivContainer = document.getElementById('dFG6Div');
export const InputDivContainer = document.getElementById('inputDiv');
export const InputDivDfg6Container = document.getElementById('inputDFG6Div');
export const ActivityDivContainer = document.getElementById('activityDiv');

export const ActivityDivContainerDFG6 = document.getElementById('activityDFG6Div');

export const nextButton1DivContainer = document.getElementById('nextButton1Div');


export const ActivityFormSCT_DistanceDiv = document.getElementById('activityFormSCT_DistanceDiv');


function resetForm(divContainer) {
    const radioButtons = divContainer.querySelectorAll('input[type="radio"]');
    if (radioButtons) {
        radioButtons.forEach(function (element) {
            element.checked = false;
        });
    }
}

export {resetForm};


function resetTextBoxes(divContainer) {
    const textBoxes = divContainer.querySelectorAll('input[type="text"]');
    textBoxes.forEach(function (textBox) {
        textBox.value = '';
    });
}

export {resetTextBoxes};


function isAnyRadioButtonSelected(formContainer) {
    const radioButtons = formContainer.querySelectorAll('input[type="radio"]');
    return Array.from(radioButtons).some(radioButton => radioButton.checked);
}

export {isAnyRadioButtonSelected};

function toggleFieldVisibility(fieldName, isVisible) {
    var field = document.querySelector('[name="' + fieldName + '"]');
    if (field) {
        if (isVisible) {
            field.style.display = 'block';
            field.setAttribute('required', ''); // Make it required when visible
        } else {
            field.style.display = 'none';
            field.removeAttribute('required'); // Remove required when hidden
        }
    }
}

export {toggleFieldVisibility};


export const step1_01DivContainer = document.getElementById('Step1_01Div');
export const step1_02DivContainer = document.getElementById('Step1_02Div');
export const step1_03DivContainer = document.getElementById('Step1_03Div');
export const step1_04DivContainer = document.getElementById('Step1_04Div');
export const step1_05DivContainer = document.getElementById('Step1_05Div');
export const step1_06DivContainer = document.getElementById('Step1_06Div');

export const step2_1DivContainer = document.getElementById('Step2_1Div');
export const step2_2DivContainer = document.getElementById('Step2_2Div');
export const step2_3DivContainer = document.getElementById('Step2_3Div');
export const step2_4DivContainer = document.getElementById('Step2_4Div');
export const step2_5DivContainer = document.getElementById('Step2_5Div');
export const step2_6DivContainer = document.getElementById('Step2_6Div');
export const step2_7DivContainer = document.getElementById('Step2_7Div');
export const step2_8DivContainer = document.getElementById('Step2_8Div');

export const step2_09DivContainer = document.getElementById('Step2_09Div');
export const step2_10DivContainer = document.getElementById('Step2_10Div');
export const step2_11DivContainer = document.getElementById('Step2_11Div');
export const step2_12DivContainer = document.getElementById('Step2_12Div');
export const step2_13DivContainer = document.getElementById('Step2_13Div');
export const step2_14DivContainer = document.getElementById('Step2_14Div');
export const step2_15DivContainer = document.getElementById('Step2_15Div');
export const step2_16DivContainer = document.getElementById('Step2_16Div');


export const step2_17DivContainer = document.getElementById('Step2_17Div');
export const step2_18DivContainer = document.getElementById('Step2_18Div');
export const step2_19DivContainer = document.getElementById('Step2_19Div');
export const step2_20DivContainer = document.getElementById('Step2_20Div');
export const step2_21DivContainer = document.getElementById('Step2_21Div');
export const step2_22DivContainer = document.getElementById('Step2_22Div');
export const step2_23DivContainer = document.getElementById('Step2_23Div');
export const step2_24DivContainer = document.getElementById('Step2_24Div');
export const step2_25DivContainer = document.getElementById('Step2_25Div');
export const step2_26DivContainer = document.getElementById('Step2_26Div');
export const step2_27DivContainer = document.getElementById('Step2_27Div');
export const step2_28DivContainer = document.getElementById('Step2_28Div');


export const step2_29DivContainer = document.getElementById('Step2_29Div');
export const step2_30DivContainer = document.getElementById('Step2_30Div');
export const step2_31DivContainer = document.getElementById('Step2_31Div');
export const step2_32DivContainer = document.getElementById('Step2_32Div');
export const step2_33DivContainer = document.getElementById('Step2_33Div');
export const step2_34DivContainer = document.getElementById('Step2_34Div');
export const step2_35DivContainer = document.getElementById('Step2_35Div');
export const step2_36DivContainer = document.getElementById('Step2_36Div');
export const step2_37DivContainer = document.getElementById('Step2_37Div');
export const step2_38DivContainer = document.getElementById('Step2_38Div');
export const step2_39DivContainer = document.getElementById('Step2_39Div');
export const step2_40DivContainer = document.getElementById('Step2_40Div');


export const step2_41DivContainer = document.getElementById('Step2_41Div');
export const step2_42DivContainer = document.getElementById('Step2_42Div');
export const step2_43DivContainer = document.getElementById('Step2_43Div');
export const step2_44DivContainer = document.getElementById('Step2_44Div');
export const step2_45DivContainer = document.getElementById('Step2_45Div');
export const step2_46DivContainer = document.getElementById('Step2_46Div');
export const step2_47DivContainer = document.getElementById('Step2_47Div');
export const step2_48DivContainer = document.getElementById('Step2_48Div');
export const step2_49DivContainer = document.getElementById('Step2_49Div');
export const step2_50DivContainer = document.getElementById('Step2_50Div');
export const step2_51DivContainer = document.getElementById('Step2_51Div');
export const step2_52DivContainer = document.getElementById('Step2_52Div');


export const step2_53DivContainer = document.getElementById('Step2_53Div');
export const step2_54DivContainer = document.getElementById('Step2_54Div');


export const step3_01DivContainer = document.getElementById('Step3_01Div');
export const step3_02DivContainer = document.getElementById('Step3_02Div');
export const step3_03DivContainer = document.getElementById('Step3_03Div');
export const step3_04DivContainer = document.getElementById('Step3_04Div');
export const step3_05DivContainer = document.getElementById('Step3_05Div');
export const step3_06DivContainer = document.getElementById('Step3_06Div');
export const step3_07DivContainer = document.getElementById('Step3_07Div');
export const step3_08DivContainer = document.getElementById('Step3_08Div');
export const step3_09DivContainer = document.getElementById('Step3_09Div');


export const step3_optionDivContainer = document.getElementById('Step3_optionDiv');


export const step4_01DivContainer = document.getElementById('Step4_01Div');
export const step4_02DivContainer = document.getElementById('Step4_02Div');
export const step4_03DivContainer = document.getElementById('Step4_03Div');




