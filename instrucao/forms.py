from django import forms
from .models import Caminhao
from .models import Trator
from .models import Colhedora
from .models import Lider



class CaminhaoForm(forms.ModelForm):
    class Meta:
        model = Caminhao
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'mi': forms.NumberInput(),
            'ni': forms.TextInput(),
            'mc': forms.NumberInput(),
            'nc': forms.TextInput(),
            'equip': forms.NumberInput(),  
            'ls': forms.TextInput(),
            'hs': forms.TimeInput(attrs={'type': 'time'}),
            'kms': forms.NumberInput(),
            'lc': forms.TextInput(),
            'hc': forms.TimeInput(attrs={'type': 'time'}),
            'kmc': forms.NumberInput(),
            'vg': forms.TextInput(),
            'md': forms.NumberInput(),
            'avaliacao_om': forms.TextInput(),
            'avaliacao_dg': forms.TextInput(),
            'avaliacao_aa': forms.TextInput(),
            'avaliacao_or': forms.TextInput(),
            'avaliacao_caminhao': forms.NumberInput(), 
            'observacoes': forms.Textarea(),
        }


class ColhedoraForm(forms.ModelForm):
    class Meta:
        model = Colhedora
        fields = '__all__'
        widgets = {
            'data2': forms.DateInput(attrs={'type': 'date'}),
            'hora2': forms.TimeInput(attrs={'type': 'time'}),
            'mit': forms.NumberInput(),
            'nit': forms.TextInput(),
            'mct': forms.NumberInput(), 
            'nct': forms.TextInput(),   
            'equipt': forms.NumberInput(),
            'hsa': forms.TimeInput(attrs={'type': 'time'}),  
            'hca': forms.TimeInput(attrs={'type': 'time'}),
            'hori': forms.NumberInput(),
            'horif': forms.NumberInput(),  
            'cldfrente': forms.NumberInput(),  
            'avaliacao_om2': forms.NumberInput(),
            'avaliacao_bord2': forms.NumberInput(),
            'avaliacao_aut2': forms.NumberInput(),
            'avaliacao_op2': forms.NumberInput(),
            'avaliacao_pcb': forms.NumberInput(),
            'avaliacao_pp': forms.NumberInput(),
            'avaliacao_cb': forms.NumberInput(),
            'avaliacao_st': forms.NumberInput(),
            'avaliacao_vc2': forms.NumberInput(),
            'avaliacao_tec': forms.NumberInput(),
            'avaliacao_sdd2': forms.NumberInput(),
            'avaliacao_gi': forms.NumberInput(),
            'observacoes': forms.Textarea(), 
        }

class TratorForm(forms.ModelForm):
    class Meta:
        model = Trator
        fields = '__all__'
        widgets = {
            'data3': forms.DateInput(attrs={'type': 'date'}),
            'hora3': forms.TimeInput(attrs={'type': 'time'}), 
            'mit2': forms.NumberInput(),
            'nit2': forms.TextInput(),
            'mct2': forms.NumberInput(),
            'nct2': forms.TextInput(),
            'quipt2': forms.NumberInput(),
            'lsa2': forms.TextInput(),
            'hsa2': forms.TimeInput(attrs={'type': 'time'}),
            'lca2': forms.TextInput(),
            'hca2': forms.TimeInput(attrs={'type': 'time'}),
            'hori2': forms.NumberInput(),
            'horif2': forms.NumberInput(),
            'avaliacao_opm': forms.NumberInput(),
            'avaliacao_bordo': forms.NumberInput(),
            'avaliacao_autz': forms.NumberInput(),
            'avaliacao_opo': forms.NumberInput(),
            'avaliacao_inst': forms.NumberInput(),
            'avaliacao_rot': forms.NumberInput(),
            'avaliacao_sdono': forms.NumberInput(),
            'avaliacao_tm': forms.NumberInput(),
            'avaliacao_te': forms.NumberInput(),
            'avaliacao_vct': forms.NumberInput(),
            'avaliacao_sc': forms.NumberInput(),
            'avaliacao_pl': forms.NumberInput(),
            'observacoes': forms.Textarea(),
        }

class LiderForm(forms.ModelForm):
    class Meta:
        model = Lider
        fields = '__all__'
        widgets = {
            'data4': forms.DateInput(attrs={'type': 'date'}),
            'hora4': forms.TimeInput(attrs={'type': 'time'}),
            'mit3': forms.NumberInput(),
            'nit3': forms.TextInput(), 
            'mct3': forms.NumberInput(), 
            'nct3': forms.TextInput(),    
            'ldrfrente': forms.NumberInput(),
            'fazenda': forms.TextInput(), 
            'unidade': forms.TextInput(),
            'avaliacao_lider1': forms.NumberInput(),
            'avaliacao_lider2': forms.NumberInput(),
            'avaliacao_lider3': forms.NumberInput(),
            'avaliacao_lider4': forms.NumberInput(),
            'avaliacao_lider5': forms.NumberInput(),
            'avaliacao_lider6': forms.NumberInput(),
            'avaliacao_lider7': forms.NumberInput(),
            'observacoes': forms.Textarea(),  # corrigido de 'observacoes' para singular
        }