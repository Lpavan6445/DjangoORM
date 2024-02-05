
from rest_framework import serializers
from .models import Author, Books, Publisher, User

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializers(serializers.ModelSerializer):
    author = AuthorSerializers()
    publisher = PublisherSerializers()
    class Meta:
        model = Books
        fields = '__all__'