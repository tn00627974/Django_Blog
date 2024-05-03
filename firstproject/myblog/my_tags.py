from django import template
from django.utils.safestring import mark_safe # 防止XSS攻擊

register = template.Library()


@register.simple_tag
def mul(v1,v2,v3):
    return v1*v2*v3


@register.simple_tag
def my_input(v1,v2):
    temp_html = '''
    <div class="imput-group mb-3">
    <span class="input-group-text" id="%s">@</span>
    <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
    </div> 
    ''' .format(v1,v2)
    return mark_safe(temp_html)

@register.filter
def my_filter(v1,v2):
    return v1*v2