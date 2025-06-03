class DateTimeUtils:

    format_iso_default = 'YYYY-MM-DDTHH-mm-SS'

    @classmethod
    def convert_to_default_iso(cls, date_: str):
        return datetime.fromstr(date_, cls.format_iso_default)





response = {'id': 1, 'db': '25-05-1992'}

date_iso = DateTimeUtils.convert_to_default_iso(response['db'])