import * as p2Module from "./C19_csv_Link_Module.js";



document.addEventListener('DOMContentLoaded', function () {
    console.log("Document 2.1 is ready!");


    p2Module.logForm.value = p2Module.defaultLog;
    p2Module.entityRelForm.value = p2Module.defaultEntityRel;
    p2Module.otherEntitiesForm.value = p2Module.defaultOtherEntities;
    p2Module.activityPropertiesForm.value = p2Module.defaultActivityProperties;
    p2Module.domainForm.value = p2Module.defaultDomain;
    p2Module.icdForm.value = p2Module.defaultIcd;
    p2Module.octNodeForm.value = p2Module.defaultOctNode;
    p2Module.octRelForm.value = p2Module.defaultOctRel;
    p2Module.dk3Form.value = p2Module.defaultDk3;
    p2Module.dk4Form.value = p2Module.defaultDk4;
    p2Module.dk5Form.value = p2Module.defaultDk5;
    p2Module.dk61Form.value = p2Module.defaultDk61;
    p2Module.dk62Form.value = p2Module.defaultDk62;
    p2Module.dk7Form.value = p2Module.defaultDk7;

    p2Module.logForm.required = true;
    p2Module.entityRelForm.required = true;
    p2Module.otherEntitiesForm.required = true;
    p2Module.activityPropertiesForm.required = true;
    p2Module.domainForm.required = true;
    p2Module.icdForm.required = true;
    p2Module.octNodeForm.required = true;
    p2Module.octRelForm.required = true;
    p2Module.dk3Form.required = true;
    p2Module.dk4Form.required = true;
    p2Module.dk5Form.required = true;
    p2Module.dk61Form.required = true;
    p2Module.dk61Form.required = true;
    p2Module.dk7Form.required = true;


    p2Module.formUpload.addEventListener('submit', function (event) {
        if (!p2Module.userForm.checkValidity() || !p2Module.passForm.checkValidity()) {
            event.preventDefault();  // This stops the form from submitting if it's not valid
            console.log("Form validation failed");
        } else {
            console.log("Form is valid, submitting");
        }
    });


});




