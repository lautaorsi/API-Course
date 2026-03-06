from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializers):
        class meta:
                    model = Itemfields = ['id','name','description']