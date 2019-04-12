from ..analytics.models import LedLightData


def write_led_light_data():
    queryset = LedLightData.objects.filter(active=True)
    for thing in queryset:
        print('\n')
        print('[*] writing data to csv for objects: ', thing)
        print('\n')
        thing.write_data_point()
