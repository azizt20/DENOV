from modeltranslation.translator import translator, TranslationOptions
from .models import *


class EnrolleeTranslation(TranslationOptions):
    fields = ('title', 'description')


class QuestionsTranslation(TranslationOptions):
    fields = ('question', 'answer')


class QuotasTranslation(TranslationOptions):
    fields = ('title', 'table')


class FinansTranslation(TranslationOptions):
    fields = ('title', 'table')


class ProgramsTranslation(TranslationOptions):
    fields = ('title', 'content', 'scheme', 'table')


class AdsCategoryTranslation(TranslationOptions):
    fields = ('name', 'description')


class AdTranslation(TranslationOptions):
    fields = ('title', 'description', 'content')


class NewsCategoryTranslation(TranslationOptions):
    fields = ('name', 'description')


class NewTranslation(TranslationOptions):
    fields = ('title', 'description', 'content')


class CentralDepartmentsTranslation(TranslationOptions):
    fields = ('name', 'boss', 'time', 'location', 'content')


class InternationalRelationshipsTranslation(TranslationOptions):
    fields = ('name', 'content')


class DepartmentsTranslation(TranslationOptions):
    fields = ('name', 'boss', 'time', 'location', 'content', 'more')


class ManagementTranslation(TranslationOptions):
    fields = ('position', 'full_name', 'time', 'work_activities')


class ExternalDepartmentTranslation(TranslationOptions):
    fields = ('position', 'full_name', 'time', 'location')


class SpirtualEducationTranslation(TranslationOptions):
    fields = ('title', 'content')


class FotoCategoryTranslation(TranslationOptions):
    fields = ('title', 'descr')


class FotoTranslation(TranslationOptions):
    fields = ('about',)


class FacultetsTranslation(TranslationOptions):
    fields = ('name', 'boss', 'time', 'location', 'content', 'more')


class FacultetAdminsTranslation(TranslationOptions):
    fields = ('position', 'fullname', 'time', 'location')


class ScienceTranslation(TranslationOptions):
    fields = ('title', 'title2', 'content')


class MagistrTranslation(TranslationOptions):
    fields = ('title', 'title2', 'content')


class DecreeTranslation(TranslationOptions):
    fields = ('title',)


class RegulationsTranslation(TranslationOptions):
    fields = ('title',)


translator.register(Enrollee, EnrolleeTranslation)
translator.register(Questions, QuestionsTranslation)
translator.register(Quotas, QuotasTranslation)
translator.register(Finans, FinansTranslation)
translator.register(Programs, ProgramsTranslation)
translator.register(AdsCategory, AdsCategoryTranslation)
translator.register(Ad, AdTranslation)
translator.register(NewsCategory, NewsCategoryTranslation)
translator.register(New, NewTranslation)
translator.register(CentralDepartments, CentralDepartmentsTranslation)
translator.register(InternationalRelationships, InternationalRelationshipsTranslation)
translator.register(Departments, DepartmentsTranslation)
translator.register(Management, ManagementTranslation)
translator.register(ExternalDepartment, ExternalDepartmentTranslation)
translator.register(SpirtualEducation, SpirtualEducationTranslation)
translator.register(FotoCategory, FotoCategoryTranslation)
translator.register(Foto, FotoTranslation)
translator.register(FacultetAdmins, FacultetAdminsTranslation)
translator.register(Facultets, FacultetsTranslation)
translator.register(Science, ScienceTranslation)
translator.register(Decree, DecreeTranslation)
translator.register(Regulations, RegulationsTranslation)
translator.register(Magistr, MagistrTranslation)
