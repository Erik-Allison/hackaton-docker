from django.contrib import admin

from hospitalApp.models import (Especialidades, Medicos, Pacientes, Horarios,
                                Citas)


@admin.register(Especialidades)
class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Nombre',
        'FechaRegistro',
    )


@admin.register(Medicos)
class Medicos(admin.ModelAdmin):
    list_display = (
        'id',
        'Nombres',
        'Apellidos',
        'Dni',
        'EspecialidadId'
    )


@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = (
        'Nombres',
        'Apellidos',
        'Telefono',
        'Activo',
    )


@admin.register(Horarios)
class HorariosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'FechaAtencion',
        'InicioAtencio',
        'FechaRegistro',
        'FechaModificacion',
    )


@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
    list_display = (
        'FechaAtencion',
        'InicioAtencion',
        'FinAtencion',
        'Activo',
        'FechaModificacion',
    )
