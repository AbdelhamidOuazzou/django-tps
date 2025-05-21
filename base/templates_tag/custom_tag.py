from django import template
registre=template.Library()
def get_value(dictionary,key):
    return dictionary.get(key)
def addclass(value,arg):
    return value.as_widget(attrs={'class':arg})
registre.filter('getval',get_value)
registre.filter('addclass',addclass)