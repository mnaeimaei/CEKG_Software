import * as p1Module from "./A1_home_Module.js";

document.addEventListener('DOMContentLoaded', function () {
    console.log("Document 1 is ready!");


    p1Module.MainDfgFormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            // Reset other DFG forms when a new selection is made in formMainDFG
            console.log("main DFG button was changed!");
            p1Module.resetForm(p1Module.Dfg1DivContainer);
            p1Module.resetForm(p1Module.Dfg2DivContainer);
            p1Module.resetForm(p1Module.Dfg3DivContainer);
            p1Module.resetForm(p1Module.Dfg4DivContainer);
            p1Module.resetForm(p1Module.Dfg5DivContainer);
            p1Module.resetForm(p1Module.Dfg6ivContainer);
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.ActivityDivContainer);
            p1Module.resetForm(p1Module.ActivityDivContainerDFG6);


        });
    });


    p1Module.Dfg1FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);
            p1Module.resetForm(p1Module.ActivityDivContainer);
            p1Module.resetForm(p1Module.ActivityDivContainerDFG6);

        });
    });


    p1Module.Dfg2FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);
            p1Module.resetForm(p1Module.ActivityDivContainer);
            p1Module.resetForm(p1Module.ActivityDivContainerDFG6);

        });
    });


    p1Module.Dfg3FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);
            p1Module.resetForm(p1Module.ActivityDivContainer);
            p1Module.resetForm(p1Module.ActivityDivContainerDFG6);

        });
    });

    p1Module.Dfg4FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);
            p1Module.resetForm(p1Module.ActivityDivContainer);
            p1Module.resetForm(p1Module.ActivityDivContainerDFG6);

        });
    });

    p1Module.Dfg5FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);
            p1Module.resetForm(p1Module.ActivityDivContainer);
            p1Module.resetForm(p1Module.ActivityDivContainerDFG6);

        });
    });


    p1Module.Dfg6FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);
            p1Module.resetForm(p1Module.ActivityDivContainer);
            p1Module.resetForm(p1Module.ActivityDivContainerDFG6);

        });
    });


    p1Module.InputFormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.ActivityDivContainer);
            p1Module.resetForm(p1Module.ActivityDivContainerDFG6);

        });
    });


});




