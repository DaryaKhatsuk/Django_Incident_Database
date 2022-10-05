from django.db import models


class Employees(models.Model):
    id_base = models.AutoField(primary_key=True)
    certificate = models.DecimalField(unique=True, decimal_places=0, max_digits=7, max_length=7,
                                      verbose_name='Номер удостоверения', help_text='Не более 7 цифр')
    full_name = models.CharField(max_length=35, verbose_name='Ф.И.О.')
    title = models.CharField(max_length=20, verbose_name='Звание')
    address = models.CharField(max_length=30, verbose_name='Адрес')
    family_composition = models.CharField(max_length=20, verbose_name='Состав семьи')

    def __str__(self):
        return f'{self.certificate}'

    class Meta:
        verbose_name = 'Сотрудникa'
        verbose_name_plural = 'Сотрудники'
        ordering = ('certificate',)


class IncidentDB(models.Model):
    id_base = models.AutoField(primary_key=True)
    registration_number = models.DecimalField(unique=True, decimal_places=0, max_digits=7, max_length=7,
                                              verbose_name='Номер происшествия', help_text='Не более 7 цифр')
    date_of_registration = models.DateField(verbose_name='Дата происшествия')
    type_event = models.CharField(max_length=20, verbose_name='Тип происшествия')
    source_messages = models.CharField(max_length=20, verbose_name='Источник сообщения')
    registration_criminal_case = models.TextField(verbose_name='Состояние уголовного дела')
    number_criminal_case = models.DecimalField(unique=True, decimal_places=0, max_digits=7, max_length=7, null=True,
                                               blank=True, verbose_name='Номер уголовного дела',
                                               help_text='Не более 7 цифр')
    number_of_the_operation = models.DecimalField(unique=True, decimal_places=0, max_digits=7, max_length=7,
                                                  verbose_name='Регистрационный номер сообщения',
                                                  help_text='Не более 7 цифр')
    registration_number_of_the_employee = models.ForeignKey(Employees, on_delete=models.DO_NOTHING,
                                                            verbose_name='Регистрационный номер сотрудника')
    the_scene_of_the_incident = models.CharField(max_length=20, verbose_name='Место происшествия')
    a_brief_description_of_the_incident = models.TextField(verbose_name='Краткое описание происшествия')

    def __str__(self):
        return f'{self.number_criminal_case}'

    class Meta:
        verbose_name = 'Происшествие'
        verbose_name_plural = 'Происшествия'
        ordering = ('registration_number',)


class Faces(models.Model):
    id_base = models.AutoField(primary_key=True)
    number_criminal_case = models.ForeignKey(IncidentDB, models.DO_NOTHING, verbose_name='Номер уголовного дела',
                                             null=True, blank=True)
    person = models.CharField(max_length=35, verbose_name='Ф.И.О.')
    registration_number_of_person = models.DecimalField(unique=True, decimal_places=0, max_digits=10, max_length=10,
                                                        verbose_name='Регистрационный номер лица',
                                                        help_text='Не более 10 цифр')
    address = models.CharField(max_length=30, verbose_name='Адрес')
    num_convictions = models.DecimalField(unique=True, decimal_places=0, max_digits=10, max_length=10,
                                          verbose_name='Количество судимостей', help_text='Не более 10 цифр')
    fingerprint_cipher = models.CharField(max_length=15, verbose_name='Шифр отпечатков пальцев',
                                          help_text='Не более 15 знаков')
    status_of_a_person = models.CharField(max_length=30, verbose_name='Статус гражданина в происшествии')

    def __str__(self):
        return f'{self.person}'

    class Meta:
        verbose_name = 'Лицо'
        verbose_name_plural = 'Лица'
        ordering = ('person',)
