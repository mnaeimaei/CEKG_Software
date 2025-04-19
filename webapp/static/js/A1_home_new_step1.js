import * as p1Module from "./A1_home_Module.js";
import {
    ActivityFormRadioButtons,
    Dfg2FormRadioButtons,
    Dfg3FormRadioButtons,
    Dfg4FormRadioButtons,
    Dfg5FormRadioButtons, Dfg6FormRadioButtons, InputFormDFG6RadioButtons, InputFormRadioButtons
} from "./A1_home_Module.js";

document.addEventListener('DOMContentLoaded', function () {
    console.log("Document 1 is ready!");


    /////////////////////////////////////////////////////////////////////////////////////////

    p1Module.MainDfgFormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            console.log("Document 1 is ready!");
            if (this.value === 'dfg1Mode') {
                console.log("dfg1Mode");
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'block';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'none';

                p1Module.step1_01DivContainer.style.display = 'block';
                p1Module.step1_02DivContainer.style.display = 'none';
                p1Module.step1_03DivContainer.style.display = 'none';
                p1Module.step1_04DivContainer.style.display = 'none';
                p1Module.step1_05DivContainer.style.display = 'none';
                p1Module.step1_06DivContainer.style.display = 'none';
                nonFunction1();


            }
            if (this.value === 'dfg2Mode') {
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'block';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'none';

                p1Module.step1_01DivContainer.style.display = 'none';
                p1Module.step1_02DivContainer.style.display = 'block';
                p1Module.step1_03DivContainer.style.display = 'none';
                p1Module.step1_04DivContainer.style.display = 'none';
                p1Module.step1_05DivContainer.style.display = 'none';
                p1Module.step1_06DivContainer.style.display = 'none';
                nonFunction1();


            }
            if (this.value === 'dfg3Mode') {
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'block';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'none';

                p1Module.step1_01DivContainer.style.display = 'none';
                p1Module.step1_02DivContainer.style.display = 'none';
                p1Module.step1_03DivContainer.style.display = 'block';
                p1Module.step1_04DivContainer.style.display = 'none';
                p1Module.step1_05DivContainer.style.display = 'none';
                p1Module.step1_06DivContainer.style.display = 'none';
                nonFunction1();


            }
            if (this.value === 'dfg4Mode') {
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'block';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'none';

                p1Module.step1_01DivContainer.style.display = 'none';
                p1Module.step1_02DivContainer.style.display = 'none';
                p1Module.step1_03DivContainer.style.display = 'none';
                p1Module.step1_04DivContainer.style.display = 'block';
                p1Module.step1_05DivContainer.style.display = 'none';
                p1Module.step1_06DivContainer.style.display = 'none';
                nonFunction1();


            }
            if (this.value === 'dfg5Mode') {
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'block';
                p1Module.Dfg6ivContainer.style.display = 'none';

                p1Module.step1_01DivContainer.style.display = 'none';
                p1Module.step1_02DivContainer.style.display = 'none';
                p1Module.step1_03DivContainer.style.display = 'none';
                p1Module.step1_04DivContainer.style.display = 'none';
                p1Module.step1_05DivContainer.style.display = 'block';
                p1Module.step1_06DivContainer.style.display = 'none';
                nonFunction1();

            }
            if (this.value === 'dfg6Mode') {
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'block';

                p1Module.step1_01DivContainer.style.display = 'none';
                p1Module.step1_02DivContainer.style.display = 'none';
                p1Module.step1_03DivContainer.style.display = 'none';
                p1Module.step1_04DivContainer.style.display = 'none';
                p1Module.step1_05DivContainer.style.display = 'none';
                p1Module.step1_06DivContainer.style.display = 'block';
                nonFunction1();


            }
            if (this.value !== 'dfg1Mode' && this.value !== 'dfg2Mode' && this.value !== 'dfg3Mode' && this.value !== 'dfg4Mode' && this.value !== 'dfg5Mode' && this.value !== 'dfg6Mode') {
                console.log("Document ewewewe is ready!");
                p1Module.MainDfgDivContainer.style.display = 'block';
                p1Module.Dfg1DivContainer.style.display = 'none';
                p1Module.Dfg2DivContainer.style.display = 'none';
                p1Module.Dfg3DivContainer.style.display = 'none';
                p1Module.Dfg4DivContainer.style.display = 'none';
                p1Module.Dfg5DivContainer.style.display = 'none';
                p1Module.Dfg6ivContainer.style.display = 'none';

                p1Module.step1_01DivContainer.style.display = 'none';
                p1Module.step1_02DivContainer.style.display = 'none';
                p1Module.step1_03DivContainer.style.display = 'none';
                p1Module.step1_04DivContainer.style.display = 'none';
                p1Module.step1_05DivContainer.style.display = 'none';
                p1Module.step1_06DivContainer.style.display = 'none';
                nonFunction1();

            }
        });
    });

    /////////////////////////////////////////////////////////////////////////////////////////

    p1Module.Dfg1FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            console.log("Document 1 is ready!");
            if (this.value === 'dfg1Mode') {
                console.log("1");
                p1Module.step2_1DivContainer.style.display = 'block';
                p1Module.step2_2DivContainer.style.display = 'none';
                p1Module.step2_3DivContainer.style.display = 'none';
                p1Module.step2_4DivContainer.style.display = 'none';
                p1Module.step2_5DivContainer.style.display = 'none';
                p1Module.step2_6DivContainer.style.display = 'none';
                p1Module.step2_7DivContainer.style.display = 'none';
                p1Module.step2_8DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '2') {
                p1Module.step2_1DivContainer.style.display = 'none';
                p1Module.step2_2DivContainer.style.display = 'block';
                p1Module.step2_3DivContainer.style.display = 'none';
                p1Module.step2_4DivContainer.style.display = 'none';
                p1Module.step2_5DivContainer.style.display = 'none';
                p1Module.step2_6DivContainer.style.display = 'none';
                p1Module.step2_7DivContainer.style.display = 'none';
                p1Module.step2_8DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '3') {
                p1Module.step2_1DivContainer.style.display = 'none';
                p1Module.step2_2DivContainer.style.display = 'none';
                p1Module.step2_3DivContainer.style.display = 'block';
                p1Module.step2_4DivContainer.style.display = 'none';
                p1Module.step2_5DivContainer.style.display = 'none';
                p1Module.step2_6DivContainer.style.display = 'none';
                p1Module.step2_7DivContainer.style.display = 'none';
                p1Module.step2_8DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '4') {
                p1Module.step2_1DivContainer.style.display = 'none';
                p1Module.step2_2DivContainer.style.display = 'none';
                p1Module.step2_3DivContainer.style.display = 'none';
                p1Module.step2_4DivContainer.style.display = 'block';
                p1Module.step2_5DivContainer.style.display = 'none';
                p1Module.step2_6DivContainer.style.display = 'none';
                p1Module.step2_7DivContainer.style.display = 'none';
                p1Module.step2_8DivContainer.style.display = 'none';
                nonFunction2();


            }
            if (this.value === '5') {
                p1Module.step2_1DivContainer.style.display = 'none';
                p1Module.step2_2DivContainer.style.display = 'none';
                p1Module.step2_3DivContainer.style.display = 'none';
                p1Module.step2_4DivContainer.style.display = 'none';
                p1Module.step2_5DivContainer.style.display = 'block';
                p1Module.step2_6DivContainer.style.display = 'none';
                p1Module.step2_7DivContainer.style.display = 'none';
                p1Module.step2_8DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '6') {
                p1Module.step2_1DivContainer.style.display = 'none';
                p1Module.step2_2DivContainer.style.display = 'none';
                p1Module.step2_3DivContainer.style.display = 'none';
                p1Module.step2_4DivContainer.style.display = 'none';
                p1Module.step2_5DivContainer.style.display = 'none';
                p1Module.step2_6DivContainer.style.display = 'block';
                p1Module.step2_7DivContainer.style.display = 'none';
                p1Module.step2_8DivContainer.style.display = 'none';
                nonFunction2();


            }

            if (this.value === '7') {
                p1Module.step2_1DivContainer.style.display = 'none';
                p1Module.step2_2DivContainer.style.display = 'none';
                p1Module.step2_3DivContainer.style.display = 'none';
                p1Module.step2_4DivContainer.style.display = 'none';
                p1Module.step2_5DivContainer.style.display = 'none';
                p1Module.step2_6DivContainer.style.display = 'none';
                p1Module.step2_7DivContainer.style.display = 'block';
                p1Module.step2_8DivContainer.style.display = 'none';
                nonFunction2();


            }

            if (this.value === '8') {
                p1Module.step2_1DivContainer.style.display = 'none';
                p1Module.step2_2DivContainer.style.display = 'none';
                p1Module.step2_3DivContainer.style.display = 'none';
                p1Module.step2_4DivContainer.style.display = 'none';
                p1Module.step2_5DivContainer.style.display = 'none';
                p1Module.step2_6DivContainer.style.display = 'none';
                p1Module.step2_7DivContainer.style.display = 'none';
                p1Module.step2_8DivContainer.style.display = 'block';
                nonFunction2();


            }
            if (this.value !== '1' && this.value !== '2' && this.value !== '3' && this.value !== '4' && this.value !== '5' && this.value !== '6' && this.value !== '7' && this.value !== '8') {
                console.log("Document ewewewe is ready!");
                p1Module.step2_1DivContainer.style.display = 'none';
                p1Module.step2_2DivContainer.style.display = 'none';
                p1Module.step2_3DivContainer.style.display = 'none';
                p1Module.step2_4DivContainer.style.display = 'none';
                p1Module.step2_5DivContainer.style.display = 'none';
                p1Module.step2_6DivContainer.style.display = 'none';
                p1Module.step2_7DivContainer.style.display = 'none';
                p1Module.step2_8DivContainer.style.display = 'none';
                nonFunction2();

            }
        });
    });

    /////////////////////////////////////////////////////////////////////////////////////////

    p1Module.Dfg2FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            console.log("Document 1 is ready!");
            if (this.value === 'dfg1Mode') {
                console.log("9");
                p1Module.step2_09DivContainer.style.display = 'block';
                p1Module.step2_10DivContainer.style.display = 'none';
                p1Module.step2_11DivContainer.style.display = 'none';
                p1Module.step2_12DivContainer.style.display = 'none';
                p1Module.step2_13DivContainer.style.display = 'none';
                p1Module.step2_14DivContainer.style.display = 'none';
                p1Module.step2_15DivContainer.style.display = 'none';
                p1Module.step2_16DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '10') {
                p1Module.step2_09DivContainer.style.display = 'none';
                p1Module.step2_10DivContainer.style.display = 'block';
                p1Module.step2_11DivContainer.style.display = 'none';
                p1Module.step2_12DivContainer.style.display = 'none';
                p1Module.step2_13DivContainer.style.display = 'none';
                p1Module.step2_14DivContainer.style.display = 'none';
                p1Module.step2_15DivContainer.style.display = 'none';
                p1Module.step2_16DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '11') {
                p1Module.step2_09DivContainer.style.display = 'none';
                p1Module.step2_10DivContainer.style.display = 'none';
                p1Module.step2_11DivContainer.style.display = 'block';
                p1Module.step2_12DivContainer.style.display = 'none';
                p1Module.step2_13DivContainer.style.display = 'none';
                p1Module.step2_14DivContainer.style.display = 'none';
                p1Module.step2_15DivContainer.style.display = 'none';
                p1Module.step2_16DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '12') {
                p1Module.step2_09DivContainer.style.display = 'none';
                p1Module.step2_10DivContainer.style.display = 'none';
                p1Module.step2_11DivContainer.style.display = 'none';
                p1Module.step2_12DivContainer.style.display = 'block';
                p1Module.step2_13DivContainer.style.display = 'none';
                p1Module.step2_14DivContainer.style.display = 'none';
                p1Module.step2_15DivContainer.style.display = 'none';
                p1Module.step2_16DivContainer.style.display = 'none';
                nonFunction2();


            }
            if (this.value === '13') {
                p1Module.step2_09DivContainer.style.display = 'none';
                p1Module.step2_10DivContainer.style.display = 'none';
                p1Module.step2_11DivContainer.style.display = 'none';
                p1Module.step2_12DivContainer.style.display = 'none';
                p1Module.step2_13DivContainer.style.display = 'block';
                p1Module.step2_14DivContainer.style.display = 'none';
                p1Module.step2_15DivContainer.style.display = 'none';
                p1Module.step2_16DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '14') {
                p1Module.step2_09DivContainer.style.display = 'none';
                p1Module.step2_10DivContainer.style.display = 'none';
                p1Module.step2_11DivContainer.style.display = 'none';
                p1Module.step2_12DivContainer.style.display = 'none';
                p1Module.step2_13DivContainer.style.display = 'none';
                p1Module.step2_14DivContainer.style.display = 'block';
                p1Module.step2_15DivContainer.style.display = 'none';
                p1Module.step2_16DivContainer.style.display = 'none';
                nonFunction2();


            }

            if (this.value === '15') {
                p1Module.step2_09DivContainer.style.display = 'none';
                p1Module.step2_10DivContainer.style.display = 'none';
                p1Module.step2_11DivContainer.style.display = 'none';
                p1Module.step2_12DivContainer.style.display = 'none';
                p1Module.step2_13DivContainer.style.display = 'none';
                p1Module.step2_14DivContainer.style.display = 'none';
                p1Module.step2_15DivContainer.style.display = 'block';
                p1Module.step2_16DivContainer.style.display = 'none';
                nonFunction2();

            }

            if (this.value === '16') {
                p1Module.step2_09DivContainer.style.display = 'none';
                p1Module.step2_10DivContainer.style.display = 'none';
                p1Module.step2_11DivContainer.style.display = 'none';
                p1Module.step2_12DivContainer.style.display = 'none';
                p1Module.step2_13DivContainer.style.display = 'none';
                p1Module.step2_14DivContainer.style.display = 'none';
                p1Module.step2_15DivContainer.style.display = 'none';
                p1Module.step2_16DivContainer.style.display = 'block';
                nonFunction2();


            }
            if (this.value !== '9' && this.value !== '10' && this.value !== '11' && this.value !== '12' && this.value !== '13' && this.value !== '14' && this.value !== '15' && this.value !== '16') {
                console.log("Document ewewewe is ready!");
                p1Module.step2_09DivContainer.style.display = 'none';
                p1Module.step2_10DivContainer.style.display = 'none';
                p1Module.step2_11DivContainer.style.display = 'none';
                p1Module.step2_12DivContainer.style.display = 'none';
                p1Module.step2_13DivContainer.style.display = 'none';
                p1Module.step2_14DivContainer.style.display = 'none';
                p1Module.step2_15DivContainer.style.display = 'none';
                p1Module.step2_16DivContainer.style.display = 'none';
                nonFunction2();

            }
        });
    });

    /////////////////////////////////////////////////////////////////////////////////////////

    p1Module.Dfg3FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            console.log("Document 1 is ready!");
            if (this.value === 'dfg1Mode') {
                console.log("17");
                p1Module.step2_17DivContainer.style.display = 'block';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();
            }
            if (this.value === 'dfg1Mode') {
                console.log("18");
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'block';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === 'dfg1Mode') {
                console.log("19");
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'block';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === 'dfg1Mode') {
                console.log("20");
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'block';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '21') {
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'block';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '22') {
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'block';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '23') {
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'block';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();


            }
            if (this.value === '24') {
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'block';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '25') {
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'block';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();


            }

            if (this.value === '26') {
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'block';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();


            }

            if (this.value === '27') {
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'block';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '28') {
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'block';
                nonFunction2();


            }
            if (this.value !== '17' && this.value !== '18' && this.value !== '19' && this.value !== '20' && this.value !== '21' && this.value !== '22' && this.value !== '23' && this.value !== '24' && this.value !== '25' && this.value !== '26' && this.value !== '27' && this.value !== '28') {
                console.log("Document ewewewe is ready!");
                p1Module.step2_17DivContainer.style.display = 'none';
                p1Module.step2_18DivContainer.style.display = 'none';
                p1Module.step2_19DivContainer.style.display = 'none';
                p1Module.step2_20DivContainer.style.display = 'none';
                p1Module.step2_21DivContainer.style.display = 'none';
                p1Module.step2_22DivContainer.style.display = 'none';
                p1Module.step2_23DivContainer.style.display = 'none';
                p1Module.step2_24DivContainer.style.display = 'none';
                p1Module.step2_25DivContainer.style.display = 'none';
                p1Module.step2_26DivContainer.style.display = 'none';
                p1Module.step2_27DivContainer.style.display = 'none';
                p1Module.step2_28DivContainer.style.display = 'none';
                nonFunction2();

            }
        });
    });

    /////////////////////////////////////////////////////////////////////////////////////////

    p1Module.Dfg4FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            console.log("Document 1 is ready!");
            if (this.value === 'dfg1Mode') {
                console.log("29");
                p1Module.step2_29DivContainer.style.display = 'block';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === 'dfg1Mode') {
                console.log("30");
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'block';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === 'dfg1Mode') {
                console.log("31");
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'block';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === 'dfg1Mode') {
                console.log("32");
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'block';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '33') {
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'block';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '34') {
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'block';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '35') {
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'block';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '36') {
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'block';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '37') {
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'block';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();


            }

            if (this.value === '38') {
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'block';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();


            }

            if (this.value === '39') {
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'block';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();


            }
            if (this.value === '40') {
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'block';
                nonFunction2();


            }
            if (this.value !== '29' && this.value !== '30' && this.value !== '31' && this.value !== '32' && this.value !== '33' && this.value !== '34' && this.value !== '35' && this.value !== '36' && this.value !== '37' && this.value !== '38' && this.value !== '39' && this.value !== '40') {
                console.log("Document ewewewe is ready!");
                p1Module.step2_29DivContainer.style.display = 'none';
                p1Module.step2_30DivContainer.style.display = 'none';
                p1Module.step2_31DivContainer.style.display = 'none';
                p1Module.step2_32DivContainer.style.display = 'none';
                p1Module.step2_33DivContainer.style.display = 'none';
                p1Module.step2_34DivContainer.style.display = 'none';
                p1Module.step2_35DivContainer.style.display = 'none';
                p1Module.step2_36DivContainer.style.display = 'none';
                p1Module.step2_37DivContainer.style.display = 'none';
                p1Module.step2_38DivContainer.style.display = 'none';
                p1Module.step2_39DivContainer.style.display = 'none';
                p1Module.step2_40DivContainer.style.display = 'none';
                nonFunction2();

            }
        });
    });

    /////////////////////////////////////////////////////////////////////////////////////////

    p1Module.Dfg5FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            console.log("Document 1 is ready!");
            if (this.value === 'dfg1Mode') {
                console.log("41");
                p1Module.step2_41DivContainer.style.display = 'block';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === 'dfg1Mode') {
                console.log("42");
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'block';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === 'dfg1Mode') {
                console.log("43");
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'block';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === 'dfg1Mode') {
                console.log("44");
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'block';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '45') {
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'block';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '46') {
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'block';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '47') {
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'block';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();


            }
            if (this.value === '48') {
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'block';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();

            }
            if (this.value === '49') {
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'block';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();


            }

            if (this.value === '50') {
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'block';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();


            }

            if (this.value === '51') {
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'block';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();


            }
            if (this.value === '52') {
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'block';
                nonFunction2();


            }
            if (this.value !== '41' && this.value !== '42' && this.value !== '43' && this.value !== '44' && this.value !== '45' && this.value !== '46' && this.value !== '47' && this.value !== '48' && this.value !== '49' && this.value !== '50' && this.value !== '51' && this.value !== '52') {
                console.log("Document ewewewe is ready!");
                p1Module.step2_41DivContainer.style.display = 'none';
                p1Module.step2_42DivContainer.style.display = 'none';
                p1Module.step2_43DivContainer.style.display = 'none';
                p1Module.step2_44DivContainer.style.display = 'none';
                p1Module.step2_45DivContainer.style.display = 'none';
                p1Module.step2_46DivContainer.style.display = 'none';
                p1Module.step2_47DivContainer.style.display = 'none';
                p1Module.step2_48DivContainer.style.display = 'none';
                p1Module.step2_49DivContainer.style.display = 'none';
                p1Module.step2_50DivContainer.style.display = 'none';
                p1Module.step2_51DivContainer.style.display = 'none';
                p1Module.step2_52DivContainer.style.display = 'none';
                nonFunction2();

            }
        });
    });

    /////////////////////////////////////////////////////////////////////////////////////////

    p1Module.Dfg6FormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            console.log("Document 1 is ready!");
            if (this.value === 'dfg1Mode') {
                console.log("53");
                p1Module.step2_53DivContainer.style.display = 'block';
                p1Module.step2_54DivContainer.style.display = 'none';
                nonFunction2();


            }
            if (this.value === '54') {
                p1Module.step2_53DivContainer.style.display = 'none';
                p1Module.step2_54DivContainer.style.display = 'block';
                nonFunction2();
            }

            if (this.value !== '53' && this.value !== '54') {
                console.log("Document ewewewe is ready!");
                p1Module.step2_53DivContainer.style.display = 'none';
                p1Module.step2_54DivContainer.style.display = 'none';
                nonFunction2();

            }
        });
    });

    /////////////////////////////////////////////////////////////////////////////////////////

    p1Module.InputFormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            console.log("Document 1 is ready!");
            if (this.value === 'dfg1Mode') {
                console.log("1");
                p1Module.step3_01DivContainer.style.display = 'block';
                p1Module.step3_02DivContainer.style.display = 'none';
                p1Module.step3_03DivContainer.style.display = 'none';
                p1Module.step3_04DivContainer.style.display = 'none';
                p1Module.step3_05DivContainer.style.display = 'none';
                p1Module.step3_06DivContainer.style.display = 'none';
                p1Module.step3_07DivContainer.style.display = 'none';
                p1Module.step3_08DivContainer.style.display = 'none';
                p1Module.step3_09DivContainer.style.display = 'none';
                nonFunction3();

            }
            if (this.value === '2') {
                p1Module.step3_01DivContainer.style.display = 'none';
                p1Module.step3_02DivContainer.style.display = 'block';
                p1Module.step3_03DivContainer.style.display = 'none';
                p1Module.step3_04DivContainer.style.display = 'none';
                p1Module.step3_05DivContainer.style.display = 'none';
                p1Module.step3_06DivContainer.style.display = 'none';
                p1Module.step3_07DivContainer.style.display = 'none';
                p1Module.step3_08DivContainer.style.display = 'none';
                p1Module.step3_09DivContainer.style.display = 'none';
                nonFunction3();

            }
            if (this.value === '3') {
                p1Module.step3_01DivContainer.style.display = 'none';
                p1Module.step3_02DivContainer.style.display = 'none';
                p1Module.step3_03DivContainer.style.display = 'block';
                p1Module.step3_04DivContainer.style.display = 'none';
                p1Module.step3_05DivContainer.style.display = 'none';
                p1Module.step3_06DivContainer.style.display = 'none';
                p1Module.step3_07DivContainer.style.display = 'none';
                p1Module.step3_08DivContainer.style.display = 'none';
                p1Module.step3_09DivContainer.style.display = 'none';
                nonFunction3();

            }
            if (this.value === '4') {
                p1Module.step3_01DivContainer.style.display = 'none';
                p1Module.step3_02DivContainer.style.display = 'none';
                p1Module.step3_03DivContainer.style.display = 'none';
                p1Module.step3_04DivContainer.style.display = 'block';
                p1Module.step3_05DivContainer.style.display = 'none';
                p1Module.step3_06DivContainer.style.display = 'none';
                p1Module.step3_07DivContainer.style.display = 'none';
                p1Module.step3_08DivContainer.style.display = 'none';
                p1Module.step3_09DivContainer.style.display = 'none';
                nonFunction3();


            }
            if (this.value === '5') {
                p1Module.step3_01DivContainer.style.display = 'none';
                p1Module.step3_02DivContainer.style.display = 'none';
                p1Module.step3_03DivContainer.style.display = 'none';
                p1Module.step3_04DivContainer.style.display = 'none';
                p1Module.step3_05DivContainer.style.display = 'block';
                p1Module.step3_06DivContainer.style.display = 'none';
                p1Module.step3_07DivContainer.style.display = 'none';
                p1Module.step3_08DivContainer.style.display = 'none';
                p1Module.step3_09DivContainer.style.display = 'none';
                nonFunction3();

            }
            if (this.value === '6') {
                p1Module.step3_01DivContainer.style.display = 'none';
                p1Module.step3_02DivContainer.style.display = 'none';
                p1Module.step3_03DivContainer.style.display = 'none';
                p1Module.step3_04DivContainer.style.display = 'none';
                p1Module.step3_05DivContainer.style.display = 'none';
                p1Module.step3_06DivContainer.style.display = 'block';
                p1Module.step3_07DivContainer.style.display = 'none';
                p1Module.step3_08DivContainer.style.display = 'none';
                p1Module.step3_09DivContainer.style.display = 'none';
                nonFunction3();

            }

            if (this.value === '7') {
                p1Module.step3_01DivContainer.style.display = 'none';
                p1Module.step3_02DivContainer.style.display = 'none';
                p1Module.step3_03DivContainer.style.display = 'none';
                p1Module.step3_04DivContainer.style.display = 'none';
                p1Module.step3_05DivContainer.style.display = 'none';
                p1Module.step3_06DivContainer.style.display = 'none';
                p1Module.step3_07DivContainer.style.display = 'block';
                p1Module.step3_08DivContainer.style.display = 'none';
                p1Module.step3_09DivContainer.style.display = 'none';
                nonFunction3();


            }

            if (this.value === '8') {
                p1Module.step3_01DivContainer.style.display = 'none';
                p1Module.step3_02DivContainer.style.display = 'none';
                p1Module.step3_03DivContainer.style.display = 'none';
                p1Module.step3_04DivContainer.style.display = 'none';
                p1Module.step3_05DivContainer.style.display = 'none';
                p1Module.step3_06DivContainer.style.display = 'none';
                p1Module.step3_07DivContainer.style.display = 'none';
                p1Module.step3_08DivContainer.style.display = 'block';
                p1Module.step3_09DivContainer.style.display = 'none';
                nonFunction3();


            }

            if (this.value === '9') {
                p1Module.step3_01DivContainer.style.display = 'none';
                p1Module.step3_02DivContainer.style.display = 'none';
                p1Module.step3_03DivContainer.style.display = 'none';
                p1Module.step3_04DivContainer.style.display = 'none';
                p1Module.step3_05DivContainer.style.display = 'none';
                p1Module.step3_06DivContainer.style.display = 'none';
                p1Module.step3_07DivContainer.style.display = 'none';
                p1Module.step3_08DivContainer.style.display = 'none';
                p1Module.step3_09DivContainer.style.display = 'block';
                nonFunction3();


            }
            if (this.value !== '1' && this.value !== '2' && this.value !== '3' && this.value !== '4' && this.value !== '5' && this.value !== '6' && this.value !== '7' && this.value !== '8' && this.value !== '9') {
                console.log("Document ewewewe is ready!");
                p1Module.step3_01DivContainer.style.display = 'none';
                p1Module.step3_02DivContainer.style.display = 'none';
                p1Module.step3_03DivContainer.style.display = 'none';
                p1Module.step3_04DivContainer.style.display = 'none';
                p1Module.step3_05DivContainer.style.display = 'none';
                p1Module.step3_06DivContainer.style.display = 'none';
                p1Module.step3_07DivContainer.style.display = 'none';
                p1Module.step3_08DivContainer.style.display = 'none';
                p1Module.step3_09DivContainer.style.display = 'none';
                nonFunction3();

            }
        });
    });

    /////////////////////////////////////////////////////////////////////////////////////////

    p1Module.InputFormDFG6RadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            console.log("Document 1 is ready!");
            if (this.value === 'dfg1Mode') {
                console.log("option");
                p1Module.step3_optionDivContainer.style.display = 'block';
                nonFunction3();

            }

            if (this.value !== 'option') {
                console.log("Document ewewewe is ready!");
                p1Module.step3_optionDivContainer.style.display = 'none';
                nonFunction3();

            }
        });
    });

    /////////////////////////////////////////////////////////////////////////////////////////

    p1Module.ActivityFormRadioButtons.forEach(function (radioButton) {
        radioButton.addEventListener('change', function () {
            console.log("Document 1 is ready!");
            if (this.value === 'dfg1Mode') {
                console.log("1");
                p1Module.step4_01DivContainer.style.display = 'block';
                p1Module.step4_02DivContainer.style.display = 'none';
                p1Module.step4_03DivContainer.style.display = 'none';

            }
            if (this.value === '2') {
                p1Module.step4_01DivContainer.style.display = 'none';
                p1Module.step4_02DivContainer.style.display = 'block';
                p1Module.step4_03DivContainer.style.display = 'none';

            }
            if (this.value === '3') {
                p1Module.step4_01DivContainer.style.display = 'none';
                p1Module.step4_02DivContainer.style.display = 'none';
                p1Module.step4_03DivContainer.style.display = 'block';

            }

            if (this.value !== '1' && this.value !== '2' && this.value !== '3') {
                console.log("Document ewewewe is ready!");
                p1Module.step4_01DivContainer.style.display = 'none';
                p1Module.step4_02DivContainer.style.display = 'none';
                p1Module.step4_03DivContainer.style.display = 'none';

            }
        });
    });


    function nonFunction1() {


        p1Module.step2_1DivContainer.style.display = 'none';
        p1Module.step2_2DivContainer.style.display = 'none';
        p1Module.step2_3DivContainer.style.display = 'none';
        p1Module.step2_4DivContainer.style.display = 'none';
        p1Module.step2_5DivContainer.style.display = 'none';
        p1Module.step2_6DivContainer.style.display = 'none';
        p1Module.step2_7DivContainer.style.display = 'none';
        p1Module.step2_8DivContainer.style.display = 'none';


        p1Module.step2_09DivContainer.style.display = 'none';
        p1Module.step2_10DivContainer.style.display = 'none';
        p1Module.step2_11DivContainer.style.display = 'none';
        p1Module.step2_12DivContainer.style.display = 'none';
        p1Module.step2_13DivContainer.style.display = 'none';
        p1Module.step2_14DivContainer.style.display = 'none';
        p1Module.step2_15DivContainer.style.display = 'none';
        p1Module.step2_16DivContainer.style.display = 'none';


        p1Module.step2_17DivContainer.style.display = 'none';
        p1Module.step2_18DivContainer.style.display = 'none';
        p1Module.step2_19DivContainer.style.display = 'none';
        p1Module.step2_20DivContainer.style.display = 'none';
        p1Module.step2_21DivContainer.style.display = 'none';
        p1Module.step2_22DivContainer.style.display = 'none';
        p1Module.step2_23DivContainer.style.display = 'none';
        p1Module.step2_24DivContainer.style.display = 'none';
        p1Module.step2_25DivContainer.style.display = 'none';
        p1Module.step2_26DivContainer.style.display = 'none';
        p1Module.step2_27DivContainer.style.display = 'none';
        p1Module.step2_28DivContainer.style.display = 'none';

        p1Module.step2_29DivContainer.style.display = 'none';
        p1Module.step2_30DivContainer.style.display = 'none';
        p1Module.step2_31DivContainer.style.display = 'none';
        p1Module.step2_32DivContainer.style.display = 'none';
        p1Module.step2_33DivContainer.style.display = 'none';
        p1Module.step2_34DivContainer.style.display = 'none';
        p1Module.step2_35DivContainer.style.display = 'none';
        p1Module.step2_36DivContainer.style.display = 'none';
        p1Module.step2_37DivContainer.style.display = 'none';
        p1Module.step2_38DivContainer.style.display = 'none';
        p1Module.step2_39DivContainer.style.display = 'none';
        p1Module.step2_40DivContainer.style.display = 'none';


        p1Module.step2_41DivContainer.style.display = 'none';
        p1Module.step2_42DivContainer.style.display = 'none';
        p1Module.step2_43DivContainer.style.display = 'none';
        p1Module.step2_44DivContainer.style.display = 'none';
        p1Module.step2_45DivContainer.style.display = 'none';
        p1Module.step2_46DivContainer.style.display = 'none';
        p1Module.step2_47DivContainer.style.display = 'none';
        p1Module.step2_48DivContainer.style.display = 'none';
        p1Module.step2_49DivContainer.style.display = 'none';
        p1Module.step2_50DivContainer.style.display = 'none';
        p1Module.step2_51DivContainer.style.display = 'none';
        p1Module.step2_52DivContainer.style.display = 'none';

        p1Module.step2_53DivContainer.style.display = 'none';
        p1Module.step2_54DivContainer.style.display = 'none';


        p1Module.step3_01DivContainer.style.display = 'none';
        p1Module.step3_02DivContainer.style.display = 'none';
        p1Module.step3_03DivContainer.style.display = 'none';
        p1Module.step3_04DivContainer.style.display = 'none';
        p1Module.step3_05DivContainer.style.display = 'none';
        p1Module.step3_06DivContainer.style.display = 'none';
        p1Module.step3_07DivContainer.style.display = 'none';
        p1Module.step3_08DivContainer.style.display = 'none';
        p1Module.step3_09DivContainer.style.display = 'none';


        p1Module.step3_optionDivContainer.style.display = 'none';


        p1Module.step4_01DivContainer.style.display = 'none';
        p1Module.step4_02DivContainer.style.display = 'none';
        p1Module.step4_03DivContainer.style.display = 'none';

    }


    function nonFunction2() {
        p1Module.step3_01DivContainer.style.display = 'none';
        p1Module.step3_02DivContainer.style.display = 'none';
        p1Module.step3_03DivContainer.style.display = 'none';
        p1Module.step3_04DivContainer.style.display = 'none';
        p1Module.step3_05DivContainer.style.display = 'none';
        p1Module.step3_06DivContainer.style.display = 'none';
        p1Module.step3_07DivContainer.style.display = 'none';
        p1Module.step3_08DivContainer.style.display = 'none';
        p1Module.step3_09DivContainer.style.display = 'none';


        p1Module.step3_optionDivContainer.style.display = 'none';


        p1Module.step4_01DivContainer.style.display = 'none';
        p1Module.step4_02DivContainer.style.display = 'none';
        p1Module.step4_03DivContainer.style.display = 'none';

    }


    function nonFunction3() {
        p1Module.step4_01DivContainer.style.display = 'none';
        p1Module.step4_02DivContainer.style.display = 'none';
        p1Module.step4_03DivContainer.style.display = 'none';

    }


});




