from django.forms import ModelForm
from appregionalidade.models import Contatos

# Create the form class.
class ContatoForm(ModelForm):
    class Meta:
        model = Contatos
        fields = ['nome', 'telefone', 'email']