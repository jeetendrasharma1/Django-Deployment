from django import template
register=template.Library()

def cut(value,args):
    """
     This cut out all the values of "args" from the string "value"
    """
    return value.replace(args,'')

register.filter('cut',cut) 
