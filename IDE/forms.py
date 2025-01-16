from django import forms
# 'style': "width:500px; height:800px; margin-top: 0; font-family: monospace;"  # Corrected style with margin-top: 0
 
class PYTHON_IDE(forms.Form):
    code = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Type something here...',
            'rows': 50,  # Set rows to 50 for a larger textarea
            'cols': 500,  # You can keep the width as 500 or adjust as needed
            'style': "margin-top: 0; font-family: monospace; height:400px; background-color: #2d2d2d; color: #f8f8f2;"  # Dark background and light text color
        }),
        label='',
        required=True
    )


#     from django import forms
