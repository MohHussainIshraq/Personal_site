from django.contrib import admin
from . models import *

# from . models import(About, Services, Portfolio,
# Skill, Contact_us, Message,
# Blog, Footer, Category,
# Counters, Testimonial)

admin.site.register(Services)
admin.site.register(About)
admin.site.register(Portfolio)
admin.site.register(Skill)
admin.site.register(Contact_us)
admin.site.register(Message)
admin.site.register(Blog)
admin.site.register(Footer)
admin.site.register(Category)
admin.site.register(Counters)
admin.site.register(Testimonial)
admin.site.register(Sub_title)

