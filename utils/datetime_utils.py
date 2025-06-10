class DataTimeUtils:
    default_iso_format = 'YYYY-MM-DD'

    @classmethod
    def convert_to_iso(cls, date_str):
        datetime.date.fromisoformat(cls.default_iso_format, date_str)

    @staticmethod
    def convert_to_custom_format(date_str, custom_format):
        datetime.datetime.combine(date_str, custom_format)
