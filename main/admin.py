from django.contrib import admin
from .models import *
from modeltranslation.admin import TabbedTranslationAdmin


class EnrolleeAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


class QuestionsAdmin(TabbedTranslationAdmin):
    list_display = ('question',)


class QuotasAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


class ProgramsAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


class AdsCategoryAdmin(TabbedTranslationAdmin):
    list_display = ('name',)


class AdAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


class NewsCategoryAdmin(TabbedTranslationAdmin):
    list_display = ('name',)


class NewAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'new')


class CentralDepartmentsAdmin(TabbedTranslationAdmin):
    list_display = ('name',)


class DepartmentsAdmin(TabbedTranslationAdmin):
    list_display = ('name',)


class ManagementAdmin(TabbedTranslationAdmin):
    list_display = ('position',)


class ExternalDepartmentAdmin(TabbedTranslationAdmin):
    list_display = ('position',)


class SpirtualEducationAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


class FinansAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


class InternationalRelationshipsAdmin(TabbedTranslationAdmin):
    list_display = ('name',)


class FotoAdmin(TabbedTranslationAdmin):
    list_display = ('id',)


class FotoCategoryAdmin(TabbedTranslationAdmin):
    list_display = ('title',)



class FacultetAdminsAdmin(TabbedTranslationAdmin):
    list_display = ('position',)


class FacultetsAdmin(TabbedTranslationAdmin):
    list_display = ('name',)


class ScienceAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


class DecreeAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


class RegulationsAdmin(TabbedTranslationAdmin):
    list_display = ('title',)


class MagistrAdmin(TabbedTranslationAdmin):
    list_display = ('title',)



admin.site.register(Enrollee, EnrolleeAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Quotas, QuotasAdmin)
admin.site.register(Programs, ProgramsAdmin)
admin.site.register(AdsCategory, AdsCategoryAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(CentralDepartments, CentralDepartmentsAdmin)
admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(ExternalDepartment, ExternalDepartmentAdmin)
admin.site.register(SpirtualEducation, SpirtualEducationAdmin)
admin.site.register(Finans, FinansAdmin)
admin.site.register(InternationalRelationships, InternationalRelationshipsAdmin)
admin.site.register(Foto, FotoAdmin)
admin.site.register(FotoCategory, FotoCategoryAdmin)
admin.site.register(Facultets, FacultetsAdmin)
admin.site.register(FacultetAdmins, FacultetAdminsAdmin)
admin.site.register(Science, ScienceAdmin)
admin.site.register(Decree, DecreeAdmin)
admin.site.register(Regulations, RegulationsAdmin)
admin.site.register(Magistr, MagistrAdmin)


