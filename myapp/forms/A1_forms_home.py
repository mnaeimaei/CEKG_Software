from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField


class MainDfgForm(forms.Form):
    mainDfgMode = forms.ChoiceField(
        choices=[('dfg1Mode', 'Independent Multi-Morbid Patient Care Pathways'),
                 ('dfg2Mode', 'Dependent Multi-Morbid Patient Care Pathways'),
                 ('dfg3Mode', 'Consolidated Multi-Morbid Patient Care Pathways with Overlapping Activities'),
                 ('dfg4Mode', 'Consolidated Multi-Morbid Patient Care Pathways with Individual Counts'),
                 ('dfg5Mode', 'Consolidated Patient Care Pathways with Aggregated Occurrences'),
                 ('dfg6Mode', 'Multi-Morbid Patient Care Pathways Based on Admission')
    ],
        widget=forms.RadioSelect,
        label=''
    )

class Dfg1Form(forms.Form):
    dfg1Mode = forms.ChoiceField(
        choices=[
        ('1', 'Activities only'),
        ('2', 'Activities + Their Domain'),
        ('3', 'Activities + Their Domain mapped to SNOMED CT'),
        ('4', 'Activities + Their Domain mapped to SNOMED CT within a specific distance'),
        ('5', 'Activities + Their Features/Values with consideration of separate nodes'),
        ('6', 'Activities + Their Features/Values with consideration of separate nodes + Their Domain'),
        ('7', 'Activities + Their Features/Values with consideration of separate nodes + Their Domain mapped to SNOMED CT'),
        ('8','Activities + Their Features/Values with consideration of separate nodes + Their Domain mapped to SNOMED CT within a specific distance')
    ],
        widget=forms.RadioSelect,
        label = '',
    required = False

    )


class Dfg2Form(forms.Form):
    dfg2Mode = forms.ChoiceField(
        choices=[
        ('9', 'Activities only'),
        ('10', 'Activities + Their Domain'),
        ('11', 'Activities + Their Domain mapped to SNOMED CT'),
        ('12', 'Activities + Their Domain mapped to SNOMED CT within a specific distance'),
        ('13', 'Activities + Their Features/Values with consideration of separate nodes'),
        ('14', 'Activities + Their Features/Values with consideration of separate nodes + Their Domain'),
        ('15', 'Activities + Their Features/Values with consideration of separate nodes + Their Domain mapped to SNOMED CT'),
        ('16','Activities + Their Features/Values with consideration of separate nodes + Their Domain mapped to SNOMED CT within a specific distance')
    ],
        widget=forms.RadioSelect,
        label='',
    required = False
    )

class Dfg3Form(forms.Form):
    dfg3Mode = forms.ChoiceField(
        choices=[
        ('17', 'Activities only'),
        ('18', 'Activities + Their Domain'),
        ('19', 'Activities + Their Domain mapped to SNOMED CT'),
        ('20', 'Activities + Their Domain mapped to SNOMED CT within a specific distance'),
        ('21', 'Activities + Their Features/Values without consideration of separate nodes'),
        ('22', 'Activities + Their Features/Values without consideration of separate nodes + Their Domain'),
        ('23', 'Activities + Their Features/Values without consideration of separate nodes + Their Domain mapped to SNOMED CT'),
        ('24','Activities + Their Features/Values without consideration of separate nodes + Their Domain mapped to SNOMED CT within a specific distance'),
        ('25', 'Activities + Their Features/Values with consideration of separate nodes'),
        ('26', 'Activities + Their Features/Values with consideration of separate nodes + Their Domain'),
        ('27', 'Activities + Their Features/Values with consideration of separate nodes + Their Domain mapped to SNOMED CT'),
        ('28','Activities + Their Features/Values with consideration of separate nodes + Their Domain mapped to SNOMED CT within a specific distance')
    ],
        widget=forms.RadioSelect,
        label='',
    required = False
    )

class Dfg4Form(forms.Form):
    dfg4Mode = forms.ChoiceField(
        choices=[
        ('29', 'Activities only'),
        ('30', 'Activities + Their Domain'),
        ('31', 'Activities + Their Domain mapped to SNOMED CT'),
        ('32', 'Activities + Their Domain mapped to SNOMED CT within a specific distance'),
        ('33', 'Activities + Their Features/Values without consideration of separate nodes'),
        ('34', 'Activities + Their Features/Values without consideration of separate nodes + Their Domain'),
        ('35', 'Activities + Their Features/Values without consideration of separate nodes + Their Domain mapped to SNOMED CT'),
        ('36','Activities + Their Features/Values without consideration of separate nodes + Their Domain mapped to SNOMED CT within a specific distance'),
        ('37', 'Activities + Their Features/Values with consideration of separate nodes'),
        ('38', 'Activities + Their Features/Values with consideration of separate nodes + Their Domain'),
        ('39', 'Activities + Their Features/Values with consideration of separate nodes + Their Domain mapped to SNOMED CT'),
        ('40','Activities + Their Features/Values with consideration of separate nodes + Their Domain mapped to SNOMED CT within a specific distance')
    ],

        widget=forms.RadioSelect,
        label='',
    required = False
    )

class Dfg5Form(forms.Form):
    dfg5Mode = forms.ChoiceField(
        choices=[
        ('41', 'Activities only'),
        ('42', 'Activities + Their Domain'),
        ('43', 'Activities + Their Domain mapped to SNOMED CT'),
        ('44', 'Activities + Their Domain mapped to SNOMED CT within a specific distance'),
        ('45', 'Activities + Their Features/Values without consideration of separate nodes'),
        ('46', 'Activities + Their Features/Values without consideration of separate nodes + Their Domain'),
        ('47', 'Activities + Their Features/Values without consideration of separate nodes + Their Domain mapped to SNOMED CT'),
        ('48','Activities + Their Features/Values without consideration of separate nodes + Their Domain mapped to SNOMED CT within a specific distance'),
        ('49', 'Activities + Their Features/Values with consideration of separate nodes'),
        ('50', 'Activities + Their Features/Values with consideration of separate nodes + Their Domain'),
        ('51', 'Activities + Their Features/Values with consideration of separate nodes + Their Domain mapped to SNOMED CT'),
        ('52','Activities + Their Features/Values with consideration of separate nodes + Their Domain mapped to SNOMED CT within a specific distance')
    ],


        widget=forms.RadioSelect,
        label='',
    required = False
    )

class Dfg6Form(forms.Form):
    dfg6Mode = forms.ChoiceField(
        choices=[
            ('53', 'Only one of them'),
            ('54', 'All of them together')
        ],
        widget=forms.RadioSelect,
        label='',
        required = False
    )


class InputForm(forms.Form):
    inputMode = forms.ChoiceField(
        choices=[
            ('1', 'Event Log Entities'),
            ('2', 'Event Log Entities + Disorder Entity'),
            ('3', 'Event Log Entities + Disorder Entity mapped to ICD Codes'),
            ('4', 'Event Log Entities + Disorder Entity mapped to ICD Codes of Ancestors with a distance of N'),
            ('5', 'Event Log Entities + Disorder Entity mapped to SNOMED CT ID'),
            ('6', 'Event Log Entities + Disorder Entity mapped to SNOMED CT ID of Ancestors with a distance of N'),
            ('7', 'Event Log Entities + Disorder Entity mapped to SNOMED CT ID of Ancestors with a distance of 1'),
            ('8', 'Event Log Entities + Disorder Entity (only one instance) mapped to ICD Codes'),
            ('9', 'Event Log Entities + Disorder Entity (only one instance) mapped to SNOMED CT Codes')
        ],

    widget=forms.RadioSelect,
        label='',
        required = False
    )


class InputFormDFG6(forms.Form):
    inputModeDFG6 = forms.ChoiceField(
        choices=[
            ('option', 'Event Log Entities + Disorder Entity')
        ],
        widget=forms.RadioSelect,
        label='',
        required = False
    )





class ActivitySelectionForm(forms.Form):
    activityMode = forms.ChoiceField(
        choices=[
            ('1', 'Using Event Log Activities\' labels'),
            ('2', 'Using SNOMED CT concepts mapped from Event log Activities\'s labels'),
            ('3', 'Using SNOMED CT concepts that are specific distant ancestors of other SNOMED CT concepts mapped from Event log Activities\'s labels')
        ],
        widget=forms.RadioSelect,
        label='',
        required = False
    )

class ActivityFormDFG6(forms.Form):
    activityModeDFG6 = forms.ChoiceField(
        choices=[
            ('option', 'Activities not used in care pathways.')
        ],
        widget=forms.RadioSelect,
        label='',
        required = False
    )




class NextButton1(forms.Form):
    nextButton1Mode = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'type': 'submit', 'value': 'Next'})
    )



