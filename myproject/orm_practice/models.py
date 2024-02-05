from django.db import models
from faker import Faker
fake = Faker()

class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(null=True)
    telephone = models.CharField(max_length=100, null=True)
    recommendedby = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', null=True)
    joindate = models.DateField()
    popularity_score = models.IntegerField()
    followers = models.ManyToManyField('User', related_name='followed_authors', related_query_name='followed_authors')

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    @classmethod
    def create_dummy_data(cls):
        for _ in range(100):
            author = cls(
                firstname=fake.first_name(),
                lastname=fake.last_name(),
                address=fake.address(),
                zipcode=fake.random_int(min=10000, max=99999),
                telephone=fake.phone_number(),
                joindate=fake.date_between(start_date='-5y', end_date='today'),
                popularity_score=fake.random_int(min=1, max=100)
            )
            author.save()

class Books(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    published_date = models.DateField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', related_query_name='books')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', related_query_name='books')

    def __str__(self):
        return self.title

    @classmethod
    def create_dummy_data(cls):
        authors = Author.objects.all()
        publishers = Publisher.objects.all()

        for _ in range(20):
            book = cls(
                title=fake.catch_phrase(),
                genre=fake.word(),
                price=fake.random_int(min=10, max=100),
                published_date=fake.date_between(start_date='-1y', end_date='today'),
                author=fake.random_element(authors),
                publisher=fake.random_element(publishers)
            )
            book.save()

class Publisher(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    recommendedby = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
    joindate = models.DateField()
    popularity_score = models.IntegerField()

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    @classmethod
    def create_dummy_data(cls):
        for _ in range(5):
            publisher = cls(
                firstname=fake.first_name(),
                lastname=fake.last_name(),
                joindate=fake.date_between(start_date='-2y', end_date='today'),
                popularity_score=fake.random_int(min=1, max=100)
            )
            publisher.save()

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    @classmethod
    def create_dummy_data(cls):
        for _ in range(50):
            user = cls(
                username=fake.user_name(),
                email=fake.email()
            )
            user.save()
