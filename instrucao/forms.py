from django import forms
from .models import Caminhao
from .models import Trator
from .models import Colhedora
from .models import Lider
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        widgets = {
            'matricula_funcionario': forms.NumberInput(),
            'nome_funcionario': forms.TextInput(),
        }




class CaminhaoForm(forms.ModelForm):
    class Meta:
        model = Caminhao
        fields = '__all__'
        widgets = {
            'data_caminhao': forms.DateInput(attrs={'type': 'date'}),
            'hora_caminhao': forms.TimeInput(attrs={'type': 'time'}),
            'matricula_instrutor_caminhao': forms.NumberInput(),
            'nome_instrutor_caminhao': forms.TextInput(),
            'matricula_condutor_caminhao': forms.NumberInput(),
            'nome_condutor_caminhao': forms.TextInput(),
            'equipamento_caminhao': forms.NumberInput(),  
            'local_saida_caminhao': forms.TextInput(),
            'km_saida_caminhao': forms.NumberInput(),
            'local_chegada_caminhao': forms.TextInput(),
            'hora_chegada_caminhao': forms.TimeInput(attrs={'type': 'time'}),
            'km_chegada_caminhao': forms.NumberInput(),
            'viagem_caminhao': forms.TextInput(),
            'media_caminhao': forms.NumberInput(),
            'avaliacao_op_mantenedor_caminhao': forms.TextInput(),
            'avaliacao_digitacao_bordo_caminhao': forms.TextInput(),
            'acoes_autorizadas_caminhao': forms.TextInput(),
            'operacao_caminhao': forms.TextInput(),
            'avaliacao_caminhao': forms.NumberInput(), 
            'observacoes': forms.Textarea(),
        }


class ColhedoraForm(forms.ModelForm):
    class Meta:
        model = Colhedora
        fields = '__all__'
        widgets = {
            'data_colhedora': forms.DateInput(attrs={'type': 'date'}),
            'hora_colhedora': forms.TimeInput(attrs={'type': 'time'}),
            'matricula_instrutor_colhedora': forms.NumberInput(),
            'nome_instrutor_colhedora': forms.TextInput(),
            'matricula_condutor_colhedora': forms.NumberInput(),
            'nome_condutor_colhedora': forms.TextInput(),
            'equipamento_colhedora': forms.NumberInput(),
            'hora_saida_colhedora': forms.TimeInput(attrs={'type': 'time'}),  # corrigido aqui
            'hora_chegada_colhedora': forms.TimeInput(attrs={'type': 'time'}),
            'horimetro_inicial_colhedora': forms.NumberInput(),
            'horimetro_final_colhedora': forms.NumberInput(),
            'frente_colhedora': forms.NumberInput(),
            'avaliacao_operacao_mantendedor_colhedora': forms.NumberInput(),
            'avaliacao_digitacao_bordo_colhedora': forms.NumberInput(),
            'avaliacao_acoes_autorizadas_colhedora': forms.NumberInput(),
            'avaliacao_operacao_colhedora': forms.NumberInput(),
            'avaliacao_pressao_corte_base_colhedora': forms.NumberInput(),
            'avaliacao_pressao_picador_colhedora': forms.NumberInput(),
            'avaliacao_configuracao_cb_colhedora': forms.NumberInput(),
            'avaliacao_sincronismo_transbordo_colhedora': forms.NumberInput(),
            'avaliacao_velocidade_constante_colhedora': forms.NumberInput(),
            'avaliacao_utilizacao_tecnologia_colhedora': forms.NumberInput(),
            'avaliacao_senso_de_dono_colhedora': forms.NumberInput(),
            'avaliacao_geral_instrutor_colhedora': forms.NumberInput(),
            'observacoes': forms.Textarea(),
        }


class TratorForm(forms.ModelForm):
    class Meta:
        model = Trator
        fields = '__all__'
        widgets = {
            'data_trator': forms.DateInput(attrs={'type': 'date'}),
            'hora_trator': forms.TimeInput(attrs={'type': 'time'}), 
            'matricula_instrutor_trator': forms.NumberInput(),
            'nome_instrutor_trator': forms.TextInput(),
            'matricula_condutor_trator': forms.NumberInput(),
            'nome_condutor_trator': forms.TextInput(),
            'equipamento_trator': forms.NumberInput(),
            'local_saida_trator': forms.TextInput(),
            'hora_saida_trator': forms.TimeInput(attrs={'type': 'time'}),
            'local_chegada_trator': forms.TextInput(),
            'hora_chegada_trator': forms.TimeInput(attrs={'type': 'time'}),
            'horimetro_inicial_trator': forms.NumberInput(),
            'horimetro_final_trator': forms.NumberInput(),
            'avaliacao_operador_mantenedor_trator': forms.NumberInput(),
            'avaliacao_digitacao_bordo_trator': forms.NumberInput(),
            'avaliacao_acoes_autorizadas_trator': forms.NumberInput(),
            'avaliacao_operacao_trator': forms.NumberInput(),
            'avaliacao_instrutor_trator': forms.NumberInput(),
            'avaliacao_rotacoes_trator': forms.NumberInput(),
            'avaliacao_senso_dono_trator': forms.NumberInput(),
            'avaliacao_troca_marcha_trator': forms.NumberInput(),
            'avaliacao_troca_embreagem_trator': forms.NumberInput(),
            'avaliacao_velocidade_constante_trator': forms.NumberInput(),
            'avaliacao_sincronismo_colheora_trator': forms.NumberInput(),
            'avaliacao_paralelismo_trator': forms.NumberInput(),
            'observacoes': forms.Textarea(),
        }

class LiderForm(forms.ModelForm):
    class Meta:
        model = Lider
        fields = '__all__'
        widgets = {
            'data_lider': forms.DateInput(attrs={'type': 'date'}),
            'hora_lider': forms.TimeInput(attrs={'type': 'time'}),
            'matricula_instrutor_lider': forms.NumberInput(),
            'nome_instrutor_lider': forms.TextInput(), 
            'matricula_do_lider': forms.NumberInput(), 
            'nome_do_lider': forms.TextInput(),    
            'frente_lider': forms.NumberInput(),
            'fazenda_lider': forms.TextInput(), 
            'unidade_lider': forms.TextInput(),
            'avaliacao_organizacao_area_trasnbordamento_lider': forms.NumberInput(),
            'avaliacao_abertura_aceiros_lider': forms.NumberInput(),
            'avaliacao_tempo_carregamento_metros_lineares_lider': forms.NumberInput(),
            'avaliacao_qualidade_colheita_lider': forms.NumberInput(),
            'avaliacao_aproveitamento_tempo_colhedora': forms.NumberInput(),
            'avaliacao_lideranca_equipe': forms.NumberInput(),
            'avaliacao_final_instrutor': forms.NumberInput(),
            'observacoes': forms.Textarea(),  # corrigido de 'observacoes' para singular
        }