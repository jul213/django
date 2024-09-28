puedes hacer formularios con django teniendo una forma similar a los modelos solo que se renderiza por una plantilla y por la url
tambien utilizando funciones 

from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre")
    url = forms.URLField(label="tu sitio web", required=False)
    correo = forms.EmailField(label="coloca tu correo electronico")
    
este seria un ejemplo de formularios de una mejor forma
