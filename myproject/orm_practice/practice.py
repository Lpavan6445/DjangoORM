from .models import Author, Books, Publisher, User
from .serializers import BookSerializers, AuthorSerializers, PublisherSerializers, UserSerializers
import datetime
from django.db.models import Count, Avg, Sum, Max, Min, Q, F

""" 1) Write a Query using Django ORM to fetch all the books objects from your database. """
def solution1():
    books = Books.objects.all()
    res = BookSerializers(books, many=True)
    return res.data

"""
    2) Write a Query using Django ORM to fetch title and published_date of all books from the database. 
"""
def solution2():
    books = Books.objects.values('title', 'published_date')
    return books


"""
    3) Fetch first name and last name of all the new authors ( Authors with popularity_score = 0 are new authors ).
"""
def solution3():
    authors = Author.objects.filter(popularity_score=0).values('firstname', 'lastname')
    return authors

"""
    4) Fetch first name and popularity score of all authors whose first name starts with A and popularity score is greater than or equal to 8.
"""
def solution4():
    authors = Author.objects.filter(firstname__startswith = 'A', popularity_score__gte = 8).values('firstname', 'popularity_score')
    return authors

"""
    5) Fetch first name of all the authors with aa case insensitive in their first name.
"""
def solution5():
    authors = Author.objects.filter(firstname__icontains =  'aa').values()
    return authors

""" 
    6) Fetch list of all the authors whose ids are in the list = [1, 3, 23, 43, 134, 25].
"""
def solution6():
    authors = Author.objects.filter(pk__in = [1, 3, 23, 43, 134, 25]).values()
    return authors

""" 
    7) Fetch list of all the publishers who joined after or in September 2012, output list should only contain first name and join date of publisher. Order by join date.
"""
def solution7():
    publishers = Publisher.objects.filter(joindate__gte = datetime.date(year=20, month=9, day=1)).order_by('joindate').values('firstname', 'joindate')
    return publishers


"""
    8) Fetch ordered list of first 10 last names of Publishers, list must not contain duplicates.
    Sample Output: [
        "Gilbert",
        "Johnson",
        "Knight",
        "Paul",
        "Soto"
    ]
"""
def solution8():
    publishers = Publisher.objects.values_list('lastname', flat=True).order_by('lastname').distinct()[:10]
    return publishers


"""
    9) Get the signup date for the last joined Author and Publisher.
"""
def solution9():
    last_joined_author = Author.objects.order_by('-joindate').first()
    last_joined_publisher = Publisher.objects.order_by('-joindate').first()

    if last_joined_author and last_joined_publisher:
        return {
            'last_joined_author_date': last_joined_author.joindate,
            'last_joined_publisher_date': last_joined_publisher.joindate
        }
    else:
        return None

"""
    10) Get the first name, last name and join date of the last author who joined.
"""
def solution10():
    author = Author.objects.order_by('-joindate').values('firstname', 'lastname', 'joindate').first()
    return author

"""
    11) Fetch list of all authors who joined after or in year 2013
"""
def solution11():
    # sol1 (easy way):
    author = Author.objects.filter(joindate__year__gte = 2013).values()

    # sol 2: 
    # author = Author.objects.filter(joindate__gte = datetime.date(2013, 1, 1)).values()
    return author

"""
    12) Fetch total price of all the books written by authors with popularity score 7 or higher.
"""
def solution12():
    books = Books.objects.filter(author__popularity_score__gte = 7).aggregate(total_price_off_all_books = Sum('price'))
    return books

"""
    13) Fetch list of titles of all books written by authors whose first name starts with ‘A’. The result should contain a list of the titles of every book. Not a list of tuples.
"""
def solution13():
    # note => flat=True will give list result
    books = Books.objects.filter(author__firstname__icontains = 'A').values_list('title', flat=True)
    return books

"""
    14) Get total price of all the books written by author with pk in list [1, 3, 4]
"""
def solution14():
    books = Books.objects.filter(author__pk__in = [1, 3, 4]).aggregate(total_price = Sum('price'))
    return books

"""
    15) Produce a list of all the authors along with their recommender.
"""
def solution15():
    authors = Author.objects.values('firstname', 'recommendedby__firstname')
    return authors

"""
    16) Produce list of all authors who published their book by publisher pk = 1, output list should be ordered by first name.
"""
def solution16():
    authors = Author.objects.filter(books__publisher__pk=1).values_list('firstname', flat=True)
    return authors


"""
    17) Create three new users and add in the followers of the author with pk = 1.
"""
def solution17():
    user1 = User.objects.create(username="pavan", email="pavan@gmail.com")
    user2 = User.objects.create(username="naresh", email="naresh@gmail.com")
    user3 = User.objects.create(username="ganesh", email="ganesh@gmail.com")
    
    authors = Author.objects.get(pk=1)
    #  Adds one or more objects to the many-to-many relationship.
    authors.followers.add(user1, user2, user3)
    res = AuthorSerializers(authors, many=False)
    return res.data

"""
    18) Set the followers list of the author with pk = 2, with only one user.
"""
def solution18():
    user1 = User.objects.create(username="pavan", email="pavan@gmail.com")
    authors = Author.objects.get(pk=2)
    # Sets the many-to-many relationship to the specified set of objects, replacing the existing ones.
    authors.followers.set(user1)
    res = AuthorSerializers(authors, many=False)
    return res.data

"""
    19) Add new users in followers of the author with pk = 1.
"""
def solution19():
    user1 = User.objects.create(username="pavan", email="pavan@gmail.com")
    authors = Author.objects.get(pk=1)
    authors.followers.add(user1)
    res = AuthorSerializers(authors, many=False)
    return res.data

"""
    20) Remove one user from the followers of the author with pk = 1.
"""
def solution20():
    user1 = User.objects.create(username="pavan", email="pavan@gmail.com")
    authors = Author.objects.get(pk=1)

    authors.followers.remove(user1)
    res = AuthorSerializers(authors, many=False)
    return res.data

"""
    21) Get first names of all the authors, whose user with pk = 1 is following. ( Without Accessing Author.objects manager )
"""
def solution21():
    authors = User.objects.get(pk=20).followed_authors.all().values_list('firstname', flat=True)

    return authors

"""
    22) Fetch list of all authors who wrote a book with “ar” as part of Book Title.
"""
def solution22():
    books = Author.objects.filter(books__title__icontains = 'ar').values_list('books__title', flat=True)
    return books


"""
    23) Fetch the list of authors whose names start with ‘A’ case insensitive, and either their popularity score is greater than 5 or they have joined after 2014. with Q objects.
"""
def solution23():
    books = Author.objects.filter(Q(firstname__startswith_icontains = 'A') and ( Q(popularity_score__gt = 5) or  Q(joindate__gt = datetime.date(2014,1,1)) )).values()
    return books


"""
    24) Retrieve a specific object with primary key= 1 from the Author table.
"""
def solution24():
    author = Author.objects.get(pk=1)
    return AuthorSerializers(author).data 

"""
    25) Retrieve the first N=10 records from an Author table.
"""
def solution25():
    authors = Author.objects.all()[:10]
    return AuthorSerializers(authors, many=True).data 

"""
    26) Retrieve Publisher records from a table that match this condition, popularity score = 7. And get the first and last record of that list.
"""
def solution26():
    authors = Author.objects.filter(popularity_score = 5).values()
    return [authors.first(), authors.last()]

"""
    27) Retrieve all authors who joined after or in the year 2012, popularity score greater than or equal to 4, join date after or with date 12, and first name starts with ‘a’ (case insensitive) without using Q objects.
"""
def solution27():
    authors = Author.objects.filter(
     joindate__year__gte=2012, popularity_score__gte=4, joindate__day__gte=12, firstname__istartswith='a'
    ).values()
    return authors

"""
    28) Retrieve all authors who did not join in 2022.
"""
def solution28():
    authors = Author.objects.exclude(
     joindate__year =2022
    ).values()
    return authors

"""
    29) Retrieve Oldest author, Newest author, Average popularity score of authors, sum of price of all books in database.
"""
def solution29():
    authors = Author.objects.order_by('joindate').values()
    oldestAuthor = authors.first()
    newestAuthor = authors.last()

    averagePopularityScore = authors.annotate(Avg('popularity_score'))
    sumOfAllBooksPrice = Books.objects.aggregate(Sum('price'))

    return { "oldestAuthor": oldestAuthor, "newestAuthor": newestAuthor, "sumOfAllBooksPrice": sumOfAllBooksPrice, "averagePopularityScore": averagePopularityScore}


"""
    30) Retrieve all authors who have no recommender, recommended by field is null.
"""
def solution30():
   authors = Author.objects.filter(recommendedby = None).values()
   return authors


"""
  31) Retrieve the books that do not have any authors, where the author is null. Also, retrieve the books whose authors are present, but do not have a recommender, where the author is not null and the author’s recommender is null. (Note that if the condition for the author not being null is not specified and only the condition for the recommender being null is mentioned, all books with both author null and author’s recommender null will be retrieved.)
"""
def solution31():
   authors = Author.objects.filter(recommendedby = None).values()
   return authors

"""
    32) Total price of books written by author with primary key = 1. ( Aggregation over related model ), oldest book written by author with pk = 1, latest book written by author with pk = 1.
"""
def solution32():
   authors = Author.objects.filter(pk = 1).aggregate(Sum('books__price'))

   oldestBook = Author.objects.filter(pk = 1).values('books__published_date')
   return oldestBook


"""
    33) Get the list of books with duplicate titles.
"""
def solution33():
    res = Books.objects.annotate(count_title=Count('title')).filter(count_title__gt=1).values()
    return res

"""
    34) Generate a list of books whose author has written more than 10 books.
"""
def solution34():
    res = Books.objects.annotate(booksCount=Count('author__books')).filter(booksCount__gt=1).values()
    return res


"""
    35) Get average popularity score of all the authors who joined after 20 September 2014.
"""
def solution35():
    res = Author.objects.filter(joindate__gt=datetime.date(year=2014, month=9, day=20)).aggregate(Avg('popularity_score')).values()
    return res


all_solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
    'solution11': solution11,
    'solution12': solution12,
    'solution13': solution13,
    'solution14': solution14,
    'solution15': solution15,
    'solution16': solution16,
    'solution17': solution17,
    'solution18': solution18,
    'solution19': solution19,
    'solution20': solution20,
    'solution21': solution21,
    'solution22': solution22,
    'solution23': solution23,
    'solution24': solution24,
    'solution25': solution25,
    'solution27': solution27,
    'solution28': solution28,
    'solution29': solution29,
    'solution30': solution30,
    'solution31': solution31,
    'solution32': solution32,
    'solution33': solution33,
    'solution34': solution34,
    'solution35': solution35,

}