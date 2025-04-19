
from django import forms


class LogLink(forms.Form):
    logLinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )


class EntityRelLink(forms.Form):
    entityRelLinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )

class OtherEntitiesLink(forms.Form):
    otherEntitiesLinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )

class ActivityPropertiesLink(forms.Form):
    activityPropertiesLinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )


class DomainLink(forms.Form):
    domainLinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )

class IcdLink(forms.Form):
    icdLinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )


class OctNodeLink(forms.Form):
    octNodeLinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )


class OctRelLink(forms.Form):
    octRelLinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )

class Dk3Link(forms.Form):
    dk3LinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )


class Dk4Link(forms.Form):
    dk4LinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )


class Dk5Link(forms.Form):
    dk5LinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )

class Dk61Link(forms.Form):
    dk61LinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )


class Dk62Link(forms.Form):
    dk62LinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )


class Dk7Link(forms.Form):
    dk7LinkMode = forms.CharField(
        label='',
        max_length=800,
        required=True,
        widget=forms.TextInput(attrs={'size': '1000'})
    )


