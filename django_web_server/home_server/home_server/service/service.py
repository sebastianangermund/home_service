from ..analytics.models import LedLightData


def schedule_ledlight_data_update():
    queryset = LedLightData.objects.all()
    logging_service(queryset)


def logging_service(queryset):
    for thing in queryset:
        thing.write_data_point
