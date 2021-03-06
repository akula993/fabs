from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='site-main-menu'):
    categories = Category.objects.all()
    return {"categories": categories, 'menu_class': menu_class}


@register.inclusion_tag('blog/menu_mobile.html')
def show_mobile(menu_class='site-mobile-menu'):
    categories = Category.objects.all()
    return {"categories": categories, 'menu_class': menu_class}
