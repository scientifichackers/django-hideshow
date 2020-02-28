# Django hideshow

Dynamically hide/show Django admin form fields using only HTML attributes. No javascript required. ™️

1. Add js file url to your model admin form's media class -

```python
class MyModelForm(ModelForm):
    class Media:
        js = (
            "https://cdn.jsdelivr.net/gh/scientifichackers/django-hideshow/hideshow.js",
        )          
```

2. Declare HTML attributes on any fields you want - 

```python
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
```

3. See it work -

<iframe width="560" height="315" src="https://www.youtube.com/embed/PeQ_uQuaTCI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>