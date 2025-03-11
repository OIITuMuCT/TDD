from django import forms
from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"

class ItemForm(forms.ModelForm):
    """ форма для элемента списка """
    class Meta:
        model = Item
        fields = ('text', )

        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }
    # метод save избавляет от ошибки 
    # TypeError: save() got an unexpected keyword argument 'for_list'
    def save(self, for_list):
        self.instance.list = for_list
        return super().save()
    