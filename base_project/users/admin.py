from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib import admin
from django import forms

from . import models


# Register your models here.
class UserCreationForm(forms.ModelForm):
    """
    Un formulario para crear nuevos usuarios. Incluye todos los campos
    requeridos, más una contraseña repetida.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    Un formulario para actualizar usuarios. Incluye todos los campos en el
    usuario, pero reemplaza el campo de contraseña con el campo de
    visualización de hash de contraseña del administrador..
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = models.User
        fields = ('email', 'password',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Personal info', {'fields': (
            'email',
            'password',
            'is_active'
        )}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        ('CUENTA', {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
            )}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(models.User, UserAdmin)
admin.site.unregister(Group)
