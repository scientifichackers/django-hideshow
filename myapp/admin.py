from django import forms
from django.contrib import admin
from django.forms import ModelForm

from myapp.models import MyModel


class MyModelForm(ModelForm):
    class Meta:
        widgets = {
            "some_integer_choice_field": forms.Select(
                attrs={
                    # all hidden by default
                    "--hide-fields": "a1, a2, a3, a4",
                    # a2, a4 visible when "0" is selected
                    "--show-on-0": "a2, a4",
                    # a1, a2 visible when the "1" is selected
                    "--show-on-1": "a1, a2",
                }
            ),
            "some_boolean_field": forms.CheckboxInput(
                attrs={
                    "--hide-fields": "b1, b2, b3",
                    # b1, b2 visible if checkbox checked
                    # b3 visible if checkbox un-checked
                    "--show-on-checked": "b1, b2",
                }
            ),
        }

    class Media:
        js = ("hideshow.js",)


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    form = MyModelForm
