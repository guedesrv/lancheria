from django.db import models

# Create your models here.

class Client(models.Model):
    """
    Classe Modelo de Dados -  Cadastro de Clientes do Lancheria
    """
    """
        Dados Básicos
    """

    CHOICES_PLAN = (
        (1,'Mensal'),
        (2,'Trimestral'),
        (3,'Semestral'),
        (4,'Mensal (3 x na semana)'),
        (5,'Trimestral (3 x na semana)'),
        (6,'Semestral (3 x na semana)'),
    )

    CHOICES_NEIGHBORHOOD = (
        (1,'Ahu'),
        (2,'Alto da Glória'),
        (3,'Alto da XV'),
        (4,'Bacacheri'),
        (5,'Batel'),
        (6,'Bigorrilho'),
        (7,'Boa Vista'),
        (8,'Bom Retiro'),
        (9,'Cabral'),
        (10,'Centro'),
        (11,'Centro Cívico'),
        (12,'Hugo Lange'),
        (13,'Jardim Social'),
        (14,'Juvevê'),
        (15,'Mercês'),
    )

    CHOICES_REGION = (
        (1,'Curitiba'),
        (2,'Região Metropolitana'),
    )

    CHOICES_PAYMENT = (
        (1,'Cartão de Crédito'),
        (2,'Transferência Bancária'),
        (3,'Dinheiro'),
    )

    name = models.CharField('Nome do Responsável', max_length=100)
    phone = models.CharField('Telefone', max_length=50, blank=True, null=True)
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=255,
        unique=True,
        db_index=True
    )

    """
        Endereço 
    """
    street = models.CharField('Rua', max_length=100, blank=True, null=True)
    region = models.IntegerField('Cidade', choices=CHOICES_REGION, default=1)
    district = models.IntegerField('Bairro', choices=CHOICES_NEIGHBORHOOD, default=1)
    number = models.CharField('Número', max_length=100, blank=True, null=True)
    complement = models.CharField('Complemento', max_length=100, blank=True, null=True)

    plan = models.IntegerField('Plano', choices=CHOICES_PLAN, default=1, blank=True, null=True)
    dainty = models.BooleanField('Incluir Guloseimas', default=False)

    payment = models.IntegerField('Plano', choices=CHOICES_PAYMENT, default=1, blank=True, null=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']


class Children(object):
    """
    Classe Modelo de Dados -  Cadastro de Filhos do Cliente Responsável

    """
    name = models.CharField('Nome do Filho', max_length=50)
    school = models.CharField('Nome da Escola', max_length=50)
    client = models.ForeignKey(Client)