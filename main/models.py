from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Enrollee(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='pages/', verbose_name="Излбражение")
    description = RichTextUploadingField(verbose_name="Текст")

    class Meta:
        verbose_name = 'данные об абитуриентах'
        verbose_name_plural = 'Абитуриенты'


    def __str__(self):
        return self.title

class Questions(models.Model):
    questions = models.ForeignKey(Enrollee, on_delete=models.CASCADE, verbose_name="абитуриет")
    question = models.CharField(max_length=500, verbose_name="Вопрос")
    answer = RichTextUploadingField(verbose_name="Ответ")

    class Meta:
        verbose_name = 'часто задаваемый вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'


class Quotas(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    table = RichTextUploadingField(verbose_name="Таблица")

    class Meta:
        verbose_name = 'данные о квотах'
        verbose_name_plural = 'Квоты'


class Finans(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    table = RichTextUploadingField(verbose_name="Таблица")

    class Meta:
        verbose_name = 'данные о финансовой деятельности'
        verbose_name_plural = 'Финансовая деятельность'


class Programs(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to = 'pages/')
    content = RichTextUploadingField(verbose_name="Текст")
    scheme = RichTextUploadingField(verbose_name="Схемы")
    table = RichTextUploadingField(verbose_name="Таблица")

    class Meta:
        verbose_name = 'данные о программах'
        verbose_name_plural = 'Программы'


class AdsCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.CharField(max_length=255, verbose_name="Описание")

    class Meta:
        verbose_name = 'категории объявлений'
        verbose_name_plural = 'Категории объявлений'

    def __str__(self):
        return self.name


class Ad(models.Model):
    ad = models.ForeignKey(AdsCategory, on_delete=models.CASCADE, verbose_name="Категория объявлений")
    image = models.ImageField(upload_to = 'pages/', null=True, blank=True, verbose_name="Излбражение")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.CharField(max_length=255, verbose_name="Описание")
    content = RichTextUploadingField(verbose_name="Текст")

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'Объявления'


class NewsCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.CharField(max_length=255, verbose_name="Описание")

    class Meta:
        verbose_name = 'категории новостей'
        verbose_name_plural = 'Категории новостей'

    def __str__(self):
        return self.name


class New(models.Model):
    new = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name="Категория новости")
    image = models.ImageField(upload_to = 'pages/', null=True, blank=True, verbose_name="Излбражение")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.CharField(max_length=255, verbose_name="Описание")
    content = RichTextUploadingField(verbose_name="Текст")

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'


class CentralDepartments(models.Model):
    icon = models.ImageField(upload_to='pages/')
    name = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to='pages/', verbose_name="Излбражение")
    boss = models.CharField(max_length=255, verbose_name="Глава отдела")
    time = models.CharField(max_length=255, null=True, blank=True, verbose_name="Время приема")
    phone = models.CharField(max_length=255, verbose_name="Номер телефона")
    email = models.CharField(max_length=255, verbose_name="адрес электронной почты")
    web = models.CharField(max_length=255, verbose_name="Сайт")
    location = models.CharField(max_length=255, verbose_name="место")
    content = RichTextUploadingField(verbose_name="Текст")

    class Meta:
        verbose_name = 'данные о центральных отделах'
        verbose_name_plural = 'Центральные отделы'


class InternationalRelationships(models.Model):
    icon = models.ImageField(upload_to='pages/', verbose_name="иконка")
    name = models.CharField(max_length=255, verbose_name="Название")
    content = RichTextUploadingField(verbose_name="Текст")

    class Meta:
        verbose_name = 'данные о международных отножений'
        verbose_name_plural = 'Международные отношения'


class Departments(models.Model):
    icon = models.ImageField(upload_to='pages/', verbose_name="иконка")
    name = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to='pages/', verbose_name="Излбражение")
    boss = models.CharField(max_length=255, verbose_name="Глава кафедры")
    time = models.CharField(max_length=255, verbose_name="Время приема")
    phone = models.CharField(max_length=255, verbose_name="Номер телефона")
    email = models.CharField(max_length=255, verbose_name="адрес электронной почты")
    location = models.CharField(max_length=255, verbose_name="место")
    content = RichTextUploadingField(verbose_name="История")
    more = RichTextUploadingField(null=True, blank=True, verbose_name="Больше информации")

    class Meta:
        verbose_name = 'Кафедра ДТПИ'
        verbose_name_plural = 'Кафедры ДТПИ'


class Management(models.Model):
    position = models.CharField(max_length=255, verbose_name="Дослжность")
    image = models.ImageField(upload_to='pages/', verbose_name="Излбражение")
    full_name = models.CharField(max_length=255, verbose_name="Ф. И. О.")
    time = models.CharField(max_length=255, verbose_name="Время приема")
    phone = models.CharField(max_length=255, verbose_name="Номер телефона")
    email = models.CharField(max_length=255, verbose_name="Aдрес электронной почты")
    work_activities = RichTextUploadingField(verbose_name="Трудовая деятельность")

    class Meta:
        verbose_name = 'члена руководства'
        verbose_name_plural = 'Рукаводство'


class ExternalDepartment(models.Model):
    position = models.CharField(max_length=255, verbose_name="Дослжность")
    image = models.ImageField(upload_to='pages/', verbose_name="Излбражение")
    full_name = models.CharField(max_length=255, verbose_name="Ф. И. О.")
    time = models.CharField(max_length=255, verbose_name="Время приема")
    phone = models.CharField(max_length=255, verbose_name="Номер телефона")
    email = models.CharField(max_length=255, verbose_name="адрес электронной почты")
    location = models.CharField(max_length=255, verbose_name="место")

    class Meta:
        verbose_name = 'данные о заочном отделении'
        verbose_name_plural = 'Заочное отделение'


class SpirtualEducation(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='pages/', verbose_name="Излбражение")
    content = RichTextUploadingField(verbose_name="Текст")

    class Meta:
        verbose_name = 'данные о духовном образовании'
        verbose_name_plural = 'Духовное образование'


class FotoCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Событие")
    descr = models.TextField(null=True, blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'категорию фотогалереи'
        verbose_name_plural = 'Категории фотогалереи'

    def __str__(self):
        return self.title


class Foto(models.Model):
    foto = models.ForeignKey(FotoCategory, on_delete=models.CASCADE, verbose_name="Категории фото", null=True, blank=True)
    about = models.CharField(max_length=255, null=True, blank=True, verbose_name="(Описание) На фото ... ")
    image = models.ImageField(upload_to='foto/', verbose_name="Излбражение")

    class Meta:
        verbose_name = 'фотографию'
        verbose_name_plural = 'Фотографии'


class Facultets(models.Model):
    icon = models.ImageField(upload_to='pages/', verbose_name="Главная фотка")
    name = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to='pages/', verbose_name="Излбражение")
    boss = models.CharField(max_length=255, verbose_name="Глава Факультета")
    time = models.CharField(max_length=255, null=True, blank=True, verbose_name="Время приема")
    phone = models.CharField(max_length=255, verbose_name="Номер телефона")
    email = models.CharField(max_length=255, verbose_name="адрес электронной почты")
    location = models.CharField(max_length=255, verbose_name="место")
    content = RichTextUploadingField(verbose_name="Текст")
    more = RichTextUploadingField(null=True, blank=True, verbose_name="Больше информации")

    class Meta:
        verbose_name = 'факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return self.name


class FacultetAdmins(models.Model):
    facultetAdmins = models.ForeignKey(Facultets, on_delete=models.CASCADE, verbose_name="Факультет")
    position = models.CharField(max_length=255, verbose_name="Дослжность")
    image = models.ImageField(upload_to='facultet-admins/', verbose_name="Излбражение")
    fullname = models.CharField(max_length=255, verbose_name="Ф. И. О.")
    time = models.CharField(max_length=255, null=True, blank=True, verbose_name="Время приема")
    phone = models.CharField(max_length=255, verbose_name="Номер телефона")
    email = models.CharField(max_length=255, verbose_name="адрес электронной почты")
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name="место")

    class Meta:
        verbose_name = 'администрацию факультета'
        verbose_name_plural = 'Администрация Факультета'


class Science(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='pages/', verbose_name="Излбражение")
    title2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок 2")
    content = RichTextUploadingField(verbose_name="Текст")


    class Meta:
        verbose_name = 'данние о науке'
        verbose_name_plural = 'Наука'


class Magistr(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='pages/', verbose_name="Излбражение")
    title2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок 2")
    content = RichTextUploadingField(verbose_name="Текст")


    class Meta:
        verbose_name = 'данние о магистратуре'
        verbose_name_plural = 'Магистратура'


class Decree(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    icon = models.ImageField(upload_to='pages/', verbose_name="иконка")
    file = models.FileField(upload_to='files/', verbose_name="файл")


    class Meta:
        verbose_name = 'решениу'
        verbose_name_plural = 'Решения'


class Regulations(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    icon = models.ImageField(upload_to='pages/', verbose_name="иконка")
    file = models.FileField(upload_to='files/', verbose_name="файл")


    class Meta:
        verbose_name = 'устав'
        verbose_name_plural = 'Уставы'