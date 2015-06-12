from django.contrib import admin

from .models import CommonName
from .models import Use       
from .models import Subspecies
from .models import Range     
from .models import Species
from .models import Reference
from .models import Image
from .models import UserProfile

class SpeciesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('binomial_nomenclature', 'created', 'modified')

admin.site.register(CommonName)
admin.site.register(Use)
admin.site.register(Subspecies)
admin.site.register(Range)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Reference)
admin.site.register(Image)
admin.site.register(UserProfile)

