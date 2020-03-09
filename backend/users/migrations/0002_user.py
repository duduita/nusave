from django.db import migrations
import json

def create_data(apps, schema_editor):
    User = apps.get_model('users', 'NuUser')
    db_alias = schema_editor.connection.alias
    
    file = open('../data/dataset.json')
    data = json.load(file)

    for i in range(len(data['Nome'])):
        nome = data['Nome'][str(i)]
        estado_civil = data['Estado_Civil'][str(i)]
        sexo = data['Sexo'][str(i)]
        classe = data['Classe'][str(i)]
        idade = data['Idade'][str(i)]
        dependentes = data['Dependentes'][str(i)]
        regiao = data['Regiao'][str(i)]
        data_mes = data['Data'][str(i)]
        alimentacao = data['Alimentacao'][str(i)]
        assinatura = data['Assinatura_e_servico'][str(i)]
        educacao = data['Educacao'][str(i)]
        restaurantes = data['Restaurantes_e_bares'][str(i)]
        casa = data['Casa'][str(i)]
        dividas = data['Dividas'][str(i)]
        investimentos = data['Investimentos'][str(i)]
        lazer = data['Lazer'][str(i)]
        saude = data['Saude'][str(i)]
        transporte = data['Transporte'][str(i)]
        beleza = data['Beleza'][str(i)]
        outros = data['Outros'][str(i)]

        user = User(account_number = str(i),
             email = nome+'@gmail.com',
             name = nome,
             marital_status = estado_civil,
             gender = sexo,
             social_class = classe,
             age = idade,
             dependents = dependentes,
             region = regiao,
             date = data_mes,
             food_expense = alimentacao,
             services_expense = assinatura,
             education_expense = educacao,
             restaurants_expense = restaurantes,
             house_expense = casa,
             debts_expense = dividas,
             investiments_expense = investimentos,
             recreation_expense = lazer,
             health_expense = saude,
             transport_expense = transporte,
             beauty_expense = beleza,
             others_expense = outros)

        user.save()
        
class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
