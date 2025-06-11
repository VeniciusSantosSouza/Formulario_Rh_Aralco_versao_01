from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta



class Funcionario(models.Model):
    cod_funcionario = models.CharField(max_length=20, primary_key=True, db_column='cod_funcionario')
    data_admissao = models.DateField(db_column='data_admissao')
    nome = models.CharField(max_length=100, db_column='nome')
    cargo = models.CharField(max_length=100, db_column='cargo')

    class Meta:
        managed = False
        db_table = '"rh_instrucao"."func_ativos"'


class Equipamento(models.Model):
    codigo_equip = models.IntegerField(primary_key=True)
    descricao_equip = models.TextField()
    marca = models.IntegerField()
    descricao_marca = models.TextField()
    modelo = models.IntegerField()
    descricao_modelo = models.TextField()
    cor = models.IntegerField()
    descricao_cor = models.TextField()
    codigo_resp = models.IntegerField()
    responsavel = models.TextField()
    chassis = models.TextField()
    renavam = models.TextField()
    motor = models.TextField()
    serie = models.TextField()
    km_atual = models.DecimalField(max_digits=10, decimal_places=2)
    placa = models.TextField()
    tipo_equipamento = models.IntegerField()
    descricao_tipo_equipamento = models.TextField()
    ano_modelo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = '"rh_instrucao"."equipamentos_ativos"'

class Caminhao(models.Model):
    id_caminhao = models.AutoField(primary_key=True)
    data_caminhao = models.DateField()
    hora_caminhao = models.TimeField()
    matricula_instrutor_caminhao = models.IntegerField() 
    nome_instrutor_caminhao = models.CharField(max_length=255)  
    matricula_condutor_caminhao = models.IntegerField() 
    nome_condutor_caminhao = models.CharField(max_length=255) 
    equipamento_caminhao = models.IntegerField() 
    local_saida_caminhao = models.CharField(max_length=255) 
    hora_saida_caminhao = models.TimeField()  
    km_saida_caminhao = models.FloatField() 
    local_chegada_caminhao = models.CharField(max_length=255)  
    hora_chegada_caminhao = models.TimeField()  
    km_chegada_caminhao = models.FloatField()  
    viagem_caminhao = models.CharField(max_length=60) 
    media_caminhao = models.FloatField()  
    avaliacao_op_mantenedor_caminhao = models.CharField(max_length=7)
    avaliacao_digitacao_bordo_caminhao = models.CharField(max_length=7)
    acoes_autorizadas_caminhao = models.CharField(max_length=7)
    operacao_caminhao = models.CharField(max_length=7)
    avaliacao_caminhao = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    observacoes = models.TextField(default='', blank=True)

    def clean(self):
        erros = {}

        # Validação de KM
        if self.km_chegada_caminhao is not None and self.km_saida_caminhao is not None:
            if self.km_chegada_caminhao < self.km_saida_caminhao:
                erros['km_chegada_caminhao'] = ("KM de chegada não pode ser menor que KM de saída.")

        if self.km_chegada_caminhao is not None:
            if self.km_chegada_caminhao < 0:
                erros['km_chegada_caminhao'] = ("KM de chegada não pode ser negativo")

        if self.km_saida_caminhao is not None:
            if self.km_saida_caminhao < 0:
                erros['km_saida_caminhao'] = ("KM de saída não pode ser negativo.")

        if self.hora_chegada_caminhao is not None and self.hora_saida_caminhao is not None and self.data_caminhao is not None:
            saida = datetime.combine(self.data_caminhao, self.hora_saida_caminhao)
            chegada = datetime.combine(self.data_caminhao, self.hora_chegada_caminhao)

            if chegada < saida:
                chegada += timedelta(days=1)

            if chegada < saida:
                erros['hora_chegada_caminhao'] = ("Horário de chegada não pode ser menor que horário de saída.")

        # Validação de matricula
        if self.matricula_condutor_caminhao is not None and self.matricula_instrutor_caminhao is not None:
            if self.matricula_condutor_caminhao == self.matricula_instrutor_caminhao:
                erros['matricula_condutor_caminhao'] = ("Matricula do condutor não pode ser igual ao do Instrutor.")

        if self.equipamento_caminhao is not None:
            if not Equipamento.objects.filter(codigo_equip=self.equipamento_caminhao).exists():
                erros['equipamento_caminhao'] = "Equipamento informado não existe na base de dados."

        if erros:
            raise ValidationError(erros)


class Colhedora(models.Model):
    id_colhedora = models.AutoField(primary_key=True)
    data_colhedora = models.DateField()
    hora_colhedora = models.TimeField()
    matricula_instrutor_colhedora = models.IntegerField()
    nome_instrutor_colhedora = models.CharField(max_length=255)
    matricula_condutor_colhedora = models.IntegerField()
    nome_condutor_colhedora = models.CharField(max_length=255)
    equipamento_colhedora = models.IntegerField()
    hora_saida_colhedora = models.TimeField() 
    hora_chegada_colhedora = models.TimeField()
    horimetro_inicial_colhedora = models.FloatField()
    horimetro_final_colhedora = models.FloatField()
    frente_colhedora = models.IntegerField()
    avaliacao_operacao_mantendedor_colhedora = models.IntegerField()
    avaliacao_digitacao_bordo_colhedora = models.IntegerField()
    avaliacao_acoes_autorizadas_colhedora = models.IntegerField()
    avaliacao_operacao_colhedora = models.IntegerField()
    avaliacao_pressao_corte_base_colhedora = models.IntegerField()
    avaliacao_pressao_picador_colhedora = models.IntegerField()
    avaliacao_configuracao_cb_colhedora = models.IntegerField()
    avaliacao_sincronismo_transbordo_colhedora = models.IntegerField()
    avaliacao_velocidade_constante_colhedora = models.IntegerField()
    avaliacao_utilizacao_tecnologia_colhedora = models.IntegerField()
    avaliacao_senso_de_dono_colhedora = models.IntegerField()
    avaliacao_geral_instrutor_colhedora = models.IntegerField()
    observacoes = models.TextField(default='', blank=True)
    campo_temp_para_migracao = models.BooleanField(default=False, blank=True, null=True)

    def clean(self):
        erros = {}

        # Validação de Matricula
        if self.matricula_condutor_colhedora is not None and self. matricula_instrutor_colhedora is not None:
            if self.matricula_condutor_colhedora == self. matricula_instrutor_colhedora:
                erros['matricula_condutor_colhedora'] = ("Matricula do condutor não pode ser igual ao do Instrutor.")

        if self.hora_chegada_colhedora is not None and self.hora_saida_colhedora is not None and self.data_colhedora is not None:
            saida = datetime.combine(self.data_colhedora, self.hora_saida_colhedora)
            chegada = datetime.combine(self.data_colhedora, self.hora_chegada_colhedora)

            if chegada < saida:
                chegada += timedelta(days=1)

            if chegada < saida:
                erros['hora_chegada_colhedora'] = ("Horário de chegada não pode ser menor que horário de saída.")

        # Validado de Horímetro
        if self.horimetro_final_colhedora is not None and self.horimetro_inicial_colhedora is not None:
            if self.horimetro_final_colhedora <= self.horimetro_inicial_colhedora:
                erros['horimetro_final_colhedora'] = ("Horímetro final não pode ser menor ou igual ao horímetro inicial.")

        if self.horimetro_final_colhedora is not None:
            if self.horimetro_final_colhedora < 0:
                erros['horimetro_final_colhedora'] = ("Horímetro final não pode ser negativo")

        if self.horimetro_inicial_colhedora is not None:
            if self.horimetro_inicial_colhedora < 0:
                erros['horimetro_inicial_colhedora'] = ("Horímetro inicial não pode ser negativo")

        if self.equipamento_colhedora is not None:
            if not Equipamento.objects.filter(codigo_equip=self.equipamento_colhedora).exists():
                erros['equipamento_caminhao'] = ("Equipamento informado não existe na base de dados.")

        if erros:
            raise ValidationError(erros)


class Trator(models.Model):
    id_trator = models.AutoField(primary_key=True)
    data_trator = models.DateField()
    hora_trator = models.TimeField()
    matricula_instrutor_trator = models.IntegerField()
    nome_instrutor_trator = models.CharField(max_length=255)
    matricula_condutor_trator = models.IntegerField()
    nome_condutor_trator = models.CharField(max_length=255)
    equipamento_trator = models.IntegerField()
    local_saida_trator = models.CharField(max_length=255)
    hora_saida_trator = models.TimeField()
    local_chegada_trator = models.CharField(max_length=255)
    hora_chegada_trator = models.TimeField()
    horimetro_inicial_trator = models.FloatField()
    horimetro_final_trator = models.FloatField()
    frente_trator = models.TextField(default='', blank=False)
    avaliacao_operador_mantendedor_trator = models.IntegerField()
    avaliacao_digitacao_bordo_trator = models.IntegerField()
    avaliacao_acoes_autorizadas_trator = models.IntegerField()
    avaliacao_operacao_trator = models.IntegerField()
    avaliacao_instrutor_trator = models.IntegerField()
    avaliacao_rotacoes_trator = models.IntegerField()
    avaliacao_senso_dono_trator = models.IntegerField()
    avaliacao_troca_marcha_trator = models.IntegerField()
    avaliacao_troca_embreagem_trator = models.IntegerField()
    avaliacao_velocidade_constante_trator = models.IntegerField()
    avaliacao_sincronismo_colheora_trator = models.IntegerField()
    avaliacao_paralelismo_trator = models.IntegerField()
    observacoes = models.TextField(default='', blank=True)

    def clean(self):
        erros = {}

        if self.matricula_condutor_trator is not None and self.matricula_instrutor_trator is not None:
            if self.matricula_condutor_trator == self.matricula_instrutor_trator:
                erros['matricula_condutor_trator'] = ("Matrícula do condutor não pode ser igual à do Instrutor.")

        if self.hora_saida_trator is not None and self.hora_chegada_trator is not None and self.data_trator is not None:
            saida = datetime.combine(self.data_trator, self.hora_saida_trator)
            chegada = datetime.combine(self.data_trator, self.hora_chegada_trator)

            if chegada < saida:
                chegada += timedelta(days=1)

            if chegada < saida:
                erros['hora_chegada_trator'] = ("Horário de chegada não pode ser menor que horário de saída.")

        if self.horimetro_final_trator is not None and self.horimetro_inicial_trator is not None:
            if self.horimetro_final_trator <= self.horimetro_inicial_trator:
                erros['horimetro_final_trator'] = "Horímetro final não pode ser menor ou igual ao horímetro inicial."

        if self.horimetro_final_trator is not None:
            if self.horimetro_final_trator < 0:
                erros['horimetro_final_trator'] = ("Horímetro final não pode ser negativo")

        if self.horimetro_inicial_trator is not None:
            if self.horimetro_inicial_trator < 0:
                erros['horimetro_inicial_trator'] = ("Horímetro inicial não pode ser negativo")

        if self.equipamento_trator is not None:
            if not Equipamento.objects.filter(codigo_equip=self.equipamento_trator).exists():
                erros['equipamento_trator'] = ("Equipamento informado não existe na base de dados.")

        if erros:
            raise ValidationError(erros)




class Lider(models.Model):
    id_lider = models.AutoField(primary_key=True)
    data_lider = models.DateField()
    hora_lider = models.TimeField()
    matricula_instrutor_lider = models.IntegerField()
    nome_instrutor_lider = models.CharField(max_length=255)
    matricula_do_lider = models.IntegerField()
    nome_do_lider = models.CharField(max_length=255)
    frente_lider = models.IntegerField()
    fazenda_lider = models.CharField(max_length=255)
    unidade_lider = models.CharField(max_length=255) 
    avaliacao_organizacao_area_trasnbordamento_lider = models.IntegerField()
    avaliacao_abertura_aceiros_lider = models.IntegerField()
    avaliacao_tempo_carregamento_metros_lineares_lider = models.IntegerField()
    avaliacao_qualidade_colheita_lider = models.IntegerField()
    avaliacao_aproveitamento_tempo_colhedora = models.IntegerField()
    avaliacao_lideranca_equipe = models.IntegerField()
    avaliacao_final_instrutor = models.IntegerField()    
    observacoes = models.TextField(default='', blank=True)

    def clean(self):
        erros = {}

        if self.matricula_do_lider is not None and self.matricula_instrutor_lider is not None:
            if self.matricula_do_lider == self.matricula_instrutor_lider:
                erros['matricula_do_lider'] = ("Matricula do lider não pode ser igual ao do Instrutor.")

        if erros:
            raise ValidationError(erros)


class ProcessoSeletivo(models.Model):
    id_processo = models.AutoField(primary_key=True)
    data_teste = models.DateField()
    hora_teste = models.TimeField()
    matricula_instrutor_teste = models.IntegerField()
    nome_instrutor_teste = models.CharField(max_length=255)
    nome_pessoa_teste = models.CharField(max_length=255)
    tipo_veiculo_teste = models.CharField(max_length=255)
    hora_inicio_teste = models.TimeField()
    hora_final_teste = models.TimeField()
    resultado_teste = models.CharField(max_length=255)
    observacoes = models.TextField()
    

    def clean(self):
        erros = {}

        if self.hora_inicio_teste is not None and self.hora_final_teste is not None  and self.data_teste is not None:
            inicio = datetime.combine(self.data_teste, self.hora_inicio_teste)
            fim = datetime.combine(self.data_teste, self.hora_final_teste)

            if fim < inicio:
                fim += timedelta(days=1)

            if fim < inicio:
                erros['hora_final_teste'] = ("Horário de término não pode ser menor que o horário de início.")

        if erros:
            raise ValidationError(erros)