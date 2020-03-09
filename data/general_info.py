from math import inf


class GeneralInfo():
    month_list = ['janeiro', 'fevereiro', 'marco', 'abril',
                  'maio', 'junho', 'julho', 'agosto',
                  'setembro', 'outubro', 'novembro', 'dezembro']
    filter_list = ['Alimentacao', 'Assinatura_e_servicos', 'Educacao',
                   'Beleza', 'Saude', 'Transporte', 'Outros', 'Saques']
    category_list = ['Classe','Regiao','Idade','Dependentes','Sexo','Estado_Civil']
    age_pins = [0, 25, 35, 50, inf]
    dependant_pins = [0, 1, 2, 3, 4, inf]