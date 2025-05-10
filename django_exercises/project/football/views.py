from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from football.models import Team, Game

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
                            <td>
                                <a href="/games_played/{team.id}" target="_blank">
                                    {team.name}
                                </a>
                                </td>
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

# href="/games_played?team_id={team.id}"
def league_table(request):
    all_teams = Team.objects.all().order_by('-points')
    for place, team in enumerate(all_teams, start=1):
        team.place = place
    return HttpResponse(display_data_in_html_table(all_teams))



def display_games_played_in_html_table(label, data):
    html = f"""
    <br>
    <h1>{label}</h1>
    <br>
    <table border="1" cellpadding="5">
        <thead>
            <tr>
                <th>Game ID</th>
                <th>Team Home Goals</th>
                <th>Team Away Goals</th>
                <th>Team Away ID</th>
                <th>Team Home ID</th>
            </tr>
        </thead>
        <tbody>
            {
                "".join([
                    f'''
                        <tr>
                            <td>{game.id}</td>
                            <td>{game.team_home_goals}</td>
                            <td>{game.team_away_goals}</td>
                            <td>{game.team_away_id}</td>
                            <td>{game.team_home_id}</td>
                        </tr>
                    '''
                    for game in data
                ])
            }
        </tbody>
    </table>
    """
    return html

def show_games_played(request, team_id):
    team_name = Team.objects.get(id=team_id).name
    as_home_team = Game.objects.filter(team_home_id=team_id)
    as_away_team = Game.objects.filter(team_away_id=team_id)
    return HttpResponse(
        display_games_played_in_html_table(
            label=str(team_name),
            data=as_home_team | as_away_team
        )
    )

@csrf_exempt
def add_game(request):
    if request.method == "GET":
        # Zobraz formular na pridani zaznamu o zapase
        html_form = f"""
        <form method="POST">
            <label style="display: block; margin-top: 20px;">
                Home Team:
                <select name="team_home_id">
                    {
                        "".join([
                            f'<option value="{team.id}">{team.name}</option>'
                            for team in Team.objects.all()
                        ])
                    }
                </select>
            </label>
            <br>

            <label style="display: block; margin-top: 20px;">
                Away Team:
                <select name="team_away_id">
                    {
                        "".join([
                            f'<option value="{team.id}">{team.name}</option>'
                            for team in Team.objects.all()
                        ])
                    }
                </select>
            </label>
            <br>

            <label style="display: block; margin-top: 20px;">
                Team Home Goals:
                <input type="number" name="team_home_goals">
            </label>
            <br>

            <label style="display: block; margin-top: 20px;">
                Team Away Goals:
                <input type="number" name="team_away_goals">
            </label>
            <br>
            <input type="submit">
        </form>
        """
        return HttpResponse(html_form)
    elif request.method == "POST":
        team_home_id = request.POST.get("team_home_id")
        team_away_id = request.POST.get("team_away_id")
        team_home_goals = request.POST.get("team_home_goals")
        team_away_goals = request.POST.get("team_away_goals")

        try:
            team_home_id = int(team_home_id)
            team_away_id = int(team_away_id)
        except ValueError:
            err_msg = "ERRROR: Team IDs must be integers."
            return HttpResponse(err_msg)
        
        try:
            team_home_goals = int(team_home_goals)
            team_away_goals = int(team_away_goals)
        except ValueError:
            err_msg = "ERRROR: Goals must be integers."
            return HttpResponse(err_msg)
    
        if team_home_id == team_away_id:
            err_msg = "ERROR: Home and away teams cannot be the same."
            return HttpResponse(err_msg)
    
        if team_home_goals < 0 or team_away_goals < 0:
            err_msg = "ERROR: Goals cannot be negative."
            return HttpResponse(err_msg)
    
        game = Game.objects.create(
            team_home_id=team_home_id,
            team_home_goals=team_home_goals,
            team_away_id=team_away_id,
            team_away_goals=team_away_goals,
        )
        
        # Pridat body tymum - oskar
        if team_home_goals > team_away_goals:
            winner = team_home_id
        elif team_home_goals < team_away_goals:
            winner = team_away_id
        else:
            winner = None # Remiza/Draw

        # Pri vyhre - vyherni tym dostava 3 body, druhy tym nic
        if winner:
            winning_team = Team.objects.filter(id=winner)[0]
            print(f"Winning team: {winning_team}")
            winning_team.points += 3
            winning_team.save()
        # Pri remize - oba tymy dostavaji 1 bod
        else:
            home_team = Team.objects.filter(id=team_home_id)[0]
            home_team.points += 1
            home_team.save()
            away_team = Team.objects.filter(id=team_away_id)[0]
            away_team.points += 1
            away_team.save()

        # pridat body tymum - Jakub:
        # if goals_home > goals_away:
        #     team_home.points = (team_home.points or 0) + 3
        # elif goals_home < goals_away:
        #     team_away.points = (team_away.points or 0) + 3
        # else:
        #     team_home.points = (team_home.points or 0) + 1
        #     team_away.points = (team_away.points or 0) + 1
        # team_home.save()
        # team_away.save()

        return redirect(f"/games_played/{team_home_id}")

@csrf_exempt
def modify_team(request, team_id):
    team = Team.objects.get(id=team_id)
    if request.method == "GET":
        html_form = f"""
        <form method="POST">
            <label style="display: block; margin-top: 20px;">
                Team Name:
                <input type="text" name="team_name" value="{team.name}">
            </label>
            <br>
            <label style="display: block; margin-top: 20px;">
                Team Points:
                <input type="number" name="team_points" value="{team.points}">
            </label>
            <br>
            <input type="submit">
        """
        return HttpResponse(html_form)

    elif request.method == "POST":
        team_name = request.POST.get("team_name")
        if not team_name:
            raise ValueError("Team name cannot be empty.")
        
        team_points = request.POST.get("team_points")
        if not team_points:
            raise ValueError("Team points cannot be empty.")
        
        try:
            team_points = int(team_points)
        except ValueError:
            raise ValueError("Team points must be an integer.")

        team.name = team_name
        team.points = team_points
        team.save()

        return HttpResponse(f'Team {team_name} has been modified successfully.')
