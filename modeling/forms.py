from django import forms

class wemEP_form(forms.Form):
    central_eos = forms.IntegerField(label='Central EOS',
                                     initial=1)
    l2_eos = forms.IntegerField(label='Layer 2 EOS', 
                                 required=False)
    l2_massfrac = forms.FloatField(label='Layer 2 Mass Fraction',
                                   required=False)
    l3_eos = forms.IntegerField(label='Layer 3 EOS', 
                                required=False)
    l3_massfrac = forms.FloatField(label='Layer 3 Mass Fraction',
                                   required=False)
    interval = forms.IntegerField(label='Layer Output Interval',
                                  initial=100)
    mass = forms.FloatField(label='Planet Mass (Earth Masses)',
                            initial=1.0)
    step = forms.FloatField(label='Step Size (meters)',
                            initial=100.0)

class wemMR_form(forms.Form):
    central_eos = forms.IntegerField(label='Central EOS',
                                     initial=1)
    l2_eos = forms.IntegerField(label='Layer 2 EOS', 
                                 required=False)
    l2_massfrac = forms.FloatField(label='Layer 2 Mass Fraction',
                                   required=False)
    l3_eos = forms.IntegerField(label='Layer 3 EOS', 
                                required=False)
    l3_massfrac = forms.FloatField(label='Layer 3 Mass Fraction',
                                   required=False)
    interval = forms.FloatField(label='Plot Mass Interval (Earth Masses)',
                                  initial=1.0)
    start_mass = forms.FloatField(label='Start Mass (Earth Masses)',
                            initial=1.0)
    end_mass = forms.FloatField(label='End Mass (Earth Masses)',
                            initial=20.0)
    step = forms.FloatField(label='Step Size (meters)',
                            initial=1000.0)
