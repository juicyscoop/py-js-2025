from exercises_app.models import Band, Category, Article
import random

def exercise_2a():
    no_year_bands = Band.objects.filter(year=None)
    for band in no_year_bands:
        print(f"name: {band.name}")
        print(f"identifier: {band.id}")

def exercise_2b():
    no_year_bands = Band.objects.filter(year=None)
    for band in no_year_bands:
        random_year = random.randint(1950, 2025)
        print(f"Chose random year: {random_year} for band: {band.name}")
        band.year = random_year
        band.save()

    
def exercise_3():
    all_bands = Band.objects.all()

    active_options = [True, False]
    genre_options = [0,1,2,3,4,5,6]

    for band in all_bands:
        band.still_active = random.choice(active_options)
        band.genre = random.choice(genre_options)
        band.save()

def print_band_names(bands, label=None):
    print(f"Label: {label}")
    for band in bands:
        print(band.name)

def exercise_4():
    bands1 = Band.objects.filter(name__contains="The")
    print_band_names(bands1, label="BANDS 1")

    bands2 = Band.objects \
        .filter(year__lt=1990) \
        .filter(year__gte=1980) \
        .filter(still_active=True)
    print_band_names(bands2, label="BANDS 2")
    
    bands3 = Band.objects \
        .filter(year__lt=1980) \
        .filter(year__gte=1970) \
        .filter(name__contains="The")
    print_band_names(bands3, label="BANDS 3")
    
    bands4 = Band.objects \
        .filter(year__lt=1990) \
        .filter(year__gte=1980) \
        .filter(still_active=False)
    print_band_names(bands4, label="BANDS 4")
    

def exercise_5():
    cat1 = Category()
    cat1.my_id = 1
    cat1.name = "Music"
    cat1.description = "Category for all audio media files"
    cat1.save()

    cat2 = Category()
    cat2.my_id = 2
    cat2.name = "Movies"
    cat2.description = "Category for all video media files"
    cat2.save()

    art1 = Article()
    art1.title = "My first article"
    art1.author = "John Doe"
    art1.content = """Is he staying arrival address earnest. To preference considered it themselves inquietude collecting estimating. View park for why gay knew face. Next than near to four so hand. Times so do he downs me would. Witty abode party her found quiet law. They door four bed fail now have. """
    art1.status = random.choice([1,2,3])
    art1.save()

    