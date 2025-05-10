from exercises_app.models import (
    Band,
    Album,
    Song,
    Article,
    Category,
    Person,
    Position
)

#  album_title | release_year | rating | band_id
def rel1():
    alb1 = Album()
    alb1.album_title = "Alb1"
    alb1.release_year = 2000
    alb1.rating = 4
    alb1.band_id = 1
    alb1.save()

    alb2 = Album()
    alb2.album_title = "Alb2"
    alb2.release_year = 2010
    alb2.rating = 5
    alb2.band_id = 10
    alb2.save()

    alb3 = Album()
    alb3.album_title = "Alb3"
    alb3.release_year = 2005
    alb3.rating = 1
    alb3.band_id = 15
    alb3.save()

    # Raises IntegrityError
    # alb4 = Album()
    # alb4.album_title = "Alb4"
    # alb4.release_year = 2015
    # alb4.rating = 3
    # alb4.save()


# V konzoli provest:
    # >>> from exercises_app.models import *
    # >>> b = Band.objects.get(pk=10)
    # >>> b
    # <Band: Band object (10)>
    # >>> b.name
    # 'Oasis'
    # >>> b.album_set.all()
    # <QuerySet [<Album: Album object (2)>]>
    # >>> albums = b.album_set.all()
    # >>> for i in albums: print(i.album_title)
    # ... 
    # Alb2
    # >>> 


def rel2():
    song1 = Song()
    song1.title = "Song1"
    song1.duration = "00:03:00"
    song1.album_id = 1
    song1.save()

    song2 = Song()
    song2.title = "Song2"
    song2.duration = "00:04:00"
    song2.album_id = 2
    song2.save()

    song3 = Song()
    song3.title = "Song3"
    song3.duration = "00:03:30"
    song3.album_id = 3
    song3.save()


# V konzoli provest:
    # >>> from exercises_app.relationships import rel2
    # >>> rel2()


def rel3():
    # All the albums by any band (we pick Oasis)
    oasis = Band.objects.get(pk=10)
    oasis_albums = oasis.album_set.all()
    for i in oasis_albums:
        print(i.album_title)

    # All the songs from every album
    all_albums = Album.objects.all()
    
    for album in all_albums:
        print(f"album title: {album.album_title}")
    
        all_songs = album.song_set.all()
        for song in all_songs:
            print(song.title)

# V konzoli provest:
    # >>> from exercises_app.relationships import rel3
    # >>> rel3()

def rel4():
    # Add multiple categories to each article.
    article = Article.objects.get(pk=1)

    cat1 = Category.objects.get(pk=1)
    cat2 = Category.objects.get(pk=2)

    article.category_set.set([cat1, cat2])
    article.save()

    new_cat = Category()
    new_cat.name = "Other"
    new_cat.description = "Other category"
    new_cat.my_id = 3
    new_cat.save()

    article = Article.objects.get(pk=1)
    article.category_set.add(new_cat)
    article.save()

# V konzoli provest:
    # >>> from exercises_app.relationships import rel4
    # >>> rel4()

def rel5():
    cat1 = Category.objects.get(pk=1)
    
    print("Articles in category:", cat1.name)
    cat1_articles = cat1.articles.all()
    for i in cat1_articles:
        print()
        print(i.title)
        print(i.author)
        print(i.date_added)

    cat1_articles_ids = [i.id for i in cat1_articles]

    cat2 = Category.objects.get(pk=2)
    cat2_articles = cat2.articles.all()
    for i in cat2_articles:
        if i.id in cat1_articles_ids:
            print()
            print(i.title)
            print(i.author)
            print(i.date_added)

# V konzoli provest:
    # >>> from exercises_app.relationships import rel5
    # >>> rel5()

def rel6():
    p1 = Person()
    p1.name = "Honza Novotny"
    p1.save()

    p2 = Person()
    p2.name = "Martin Novak"
    p2.save()

    p3 = Person()
    p3.name = "Jan Deak"
    p3.save()
    
    pos1 = Position()
    pos1.position_name = "CEO"
    pos1.salary = 1000.20
    pos1.person = p1
    pos1.save()

    pos2 = Position()
    pos2.position_name = "CTO"
    pos2.salary = 5000.5
    pos2.person = p2
    pos2.save()

    pos3 = Position()
    pos3.position_name = "PM"
    pos3.salary = 2000.5
    pos3.person_id = p3.id
    pos3.save()

# V konzoli provest:
    # >>> from exercises_app.relationships import rel6
    # >>> rel6()

def rel6_delete_test():
    p1 = Position.objects.get(pk=2)
    p1.delete()