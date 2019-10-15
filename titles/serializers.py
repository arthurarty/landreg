from rest_framework import serializers

from titles.models import Title


class TitleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.phone_number")

    class Meta:
        model = Title
        fields = ['id', 'proprietor', 'tenure', 'tenure_volume',
                  'tenure_folio_no', 'size_of_land', 'lease_period',
                  'lease_authority', 'district', 'parish', 'block', 'plot',
                  'user'
                  ]
