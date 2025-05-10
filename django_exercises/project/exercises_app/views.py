#from django.shortcuts import render
from django.http import HttpResponse
from exercises_app.models import Article, Band


# <head>
#     <style>
#         .article-label {
        
#         }
#     </style>
# </head>

# Create your views here.
def show_articles(request):
    #return render(request, 'articles.html')
    articles_data = Article.objects.filter(status=2)
    articles_html = f"""
    <html>
        <body>
            <h1>Articles</h1>
            <div>
                {
                    "".join([
                        f'''
                            <div> 
                                <label style="display: block; margin-top: 20px; font-weight: bold;">Title</label>
                                <br>
                                <span style="display: block; margin-bottom: 20px;">{article.title}</span>
                                <br>
                                <label style="display: block; margin-top: 20px; font-weight: bold;">Author</label>
                                <br>
                                <span style="display: block; margin-bottom: 20px;">{article.author}</span>
                                <br>
                                <label style="display: block; margin-top: 20px; font-weight: bold;">Date Added</label>
                                <br>
                                <span style="display: block; margin-bottom: 20px;">{article.date_added}</span>
                                <br>
                            </div>
                            <br>
                        '''
                        for article in articles_data
                    ])
                }
            </div>
        </body>
    </html>
    """
    return HttpResponse(articles_html)


def show_bands(request, band_id):
    band = Band.objects.get(pk=band_id)

    genre = band.genre
    genre_name = band.get_genre_display().capitalize()
    # genre_name = dict(band_choices)[band.genre].capitalize()
    
    band_albums = band.album_set.all()
    
    band_html = f"""
    <html>
        <body>
            <h1>Band</h1>
            <div>
                <label style="display: block; margin-top: 20px; font-weight: bold;">Name</label>
                <br>
                <span style="display: block; margin-bottom: 20px;">{band.name}</span>
                <br>
                <label style="display: block; margin-top: 20px; font-weight: bold;">Year of formation</label>
                <br>
                <span style="display: block; margin-bottom: 20px;">{band.year}</span>
                <br>
                <label style="display: block; margin-top: 20px; font-weight: bold;">Genre</label>
                <br>
                <span style="display: block; margin-bottom: 20px;">{genre_name}</span>
                <br>
                <label style="display: block; margin-top: 20px; font-weight: bold;">Is active?</label>
                <br>
                <span style="display: block; margin-bottom: 20px;">{band.still_active}</span>
            </div>

            <div style="margin-top: 50px;">
                <label style="display: block; margin-top: 20px; font-weight: bold;">Albums</label>
                <br>
                <span style="display: block; margin-bottom: 20px;">
                    {", ".join([album.album_title for album in band_albums])}
                </span>
            </div>
        </body>
    </html>
    """
    return HttpResponse(band_html)