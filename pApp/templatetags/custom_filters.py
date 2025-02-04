from django import template

register = template.Library()

def bahttext(value):
    from num2words import num2words
    try:
        value = float(value)
        text = num2words(value, lang='th') + "บาทถ้วน"
        return text
    except:
        return value

register.filter('bahttext', bahttext)
