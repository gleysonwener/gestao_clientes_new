# Generated by Django 4.0.5 on 2022-06-16 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_remove_venda_pessoa_delete_itensdopedido_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'permissions': (('deletar_clientes', 'Deletar clientes'),)},
        ),
    ]
