#from django.shortcuts import render
from django.http import HttpResponse

from football.models import Team

# Create your views here.
def display_data_in_html_table(data):
    html = f"""
    <table>
        <thead>
            <tr>
                <th>Team</th>
                <th>Points</th>
                <th>Place</th>
            </tr>
        </thead>
        <tbody>
            {
                "".join([
                    f'''
                        <tr>
                            <td>{team.name}</td>
                            <td>{team.points}</td>
                            <td>{team.place}</td>
                        </tr>
                    '''
                    for team in data
                ])
            }
        </tbody>
    </table>
    """
    return html

def league_table(request):
    all_teams = Team.objects.all().order_by('-points')
    for place, team in enumerate(all_teams, start=1):
        team.place = place
    return HttpResponse(display_data_in_html_table(all_teams))



