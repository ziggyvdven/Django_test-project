from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
	"""Serializers a name field for testing our API view

	Args:
		serializers (_type_): _description_
	"""

	name = serializers.CharField(max_length=10)