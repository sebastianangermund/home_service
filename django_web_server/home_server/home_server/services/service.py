
def logging_service(queryset):
    for thing in queryset:
        thing.write_data_point
