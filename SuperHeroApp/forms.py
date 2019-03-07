from django import forms
from .models import SuperHeroModel

Rich_Or_Power=\
    (
        ('rich','Rich'),
        ('power','Power')
    )
# (Flight, Speed, Invisibility, Telekenetic, Healing, Other)
Power_Choices =\
    (
        ('flight','Flight'),
        ('speed','Speed'),
        ('invisibility','Invisibility'),
        ('telekinesis','Telekinesis'),
        ('healing','Healing'),
        ('other','Other'),
    )
# (Good, kinda good, neutral, a little evil, evil)

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
                'Power':forms.CheckboxSelectMultiple(choices=Power_Choices),
                'Alignment':forms.Select(choices=Alignment_Choies),
            }