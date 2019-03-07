from django import forms
from .models import SuperHeroModel


# if they are rich or have powers
Rich_Or_Power=\
    (
        ('rich','Rich'),
        ('power','Power')
    )
# (Flight, Speed, Invisibility, Telekenetic, Healing, Other)

# (Good, kinda good, neutral, a little evil, evil)
#choices for alignment
Alignment_Choies = \
    (
        ('G','Good'),
        ('NG','Neutral Good'),
        ('N','Neutral'),
        ('NE','Neutral Evil'),
        ('E','Evil'),
    )

class SuperHeroForm(forms.ModelForm):
    class Meta:
        model = SuperHeroModel
        fields = '__all__'
        widgets=\
            {
                'RichOrPower':forms.RadioSelect(choices=Rich_Or_Power),
                'Alignment':forms.Select(choices=Alignment_Choies),
            }