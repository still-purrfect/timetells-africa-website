from django.contrib import admin
from .models import (
    Service,
    Project,
    QuoteRequest,
    ContactMessage
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = ("title",)

    search_fields = ("title",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ("title",)

    search_fields = ("title",)


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "service",
        "phone",
        "submitted_at",
    )

    search_fields = (
        "full_name",
        "service",
    )

    list_filter = (
        "service",
        "submitted_at",
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "subject",
        "submitted_at",
    )

    search_fields = (
        "full_name",
        "subject",
    )

    list_filter = (
        "submitted_at",
    )    