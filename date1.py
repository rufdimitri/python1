import datetime
import locale


def date1():
    from datetime import date #import within function scope
    today = date.today()
    custom_date = date.fromisoformat("1568-02-27")
    custom_formatted = custom_date.strftime("%d. %B %Y")
    local_format = custom_date.strftime("%x %X")
    local_format2 = custom_date.strftime("%c")

    print(f"today: {today}")
    print(f"custom_date: {custom_date}")
    print(f"custom_formatted: {custom_formatted}")
    print(f"local_format: {local_format}")
    print(f"local_format2: {local_format2}")
    print("-------")


def date2():
    #date.today() #error, because import scope is limited to date1() function
    today = datetime.date.today()
    print(today)
    print(f"day: {today.day}")
    print(f"month: {today.month}")
    print(f"year: {today.year}")
    print("-------")

def date3_locale():
    from datetime import date
    from babel.dates import format_date, format_datetime, format_time #have to use 3rd party library to get
    # clean date time formatting for different locales without changing current locale of the app
    d = date(2007, 4, 1)
    formatted_en = format_date(d, locale='en')
    formatted_de = format_date(d, locale='de_DE')
    formatted_ru = format_date(d, locale='ru_RU')
    print(f"formatted_en: {formatted_en}")
    print(f"formatted_de: {formatted_de}")
    print(f"formatted_ru: {formatted_ru}")
    print("-------")


date1()
date2()
date3_locale()