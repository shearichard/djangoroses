from rest_framework import serializers
from .models import Species


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('binomial_nomenclature', 'subspecies', 'common_name', 'height_and_spread', 'range', 'use', 'further_reference', 'image', 'created', 'modified')

