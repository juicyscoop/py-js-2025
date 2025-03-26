from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for sessions

DICE_TYPES = {
    'D3': 3,
    'D4': 4,
    'D6': 6,
    'D8': 8,
    'D10': 10,
    'D12': 12,
    'D20': 20,
    'D100': 100
}

def roll_dice(dice_type):
    max_value = DICE_TYPES[dice_type]
    return random.randint(1, max_value)

def calculate_new_score(current_score, roll):
    if current_score > 0:  # Rules apply only after first turn
        if roll == 7:
            return current_score // 7
        elif roll == 11:
            return current_score * 11
    return current_score + roll

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize scores and chosen die in session if they don't exist
    if 'player_score' not in session:
        session['player_score'] = 0
    if 'computer_score' not in session:
        session['computer_score'] = 0
    # Initialize player_die in session with a default value
    if 'player_die' not in session:
        session['player_die'] = 'D6'  # Default die

    player_score = session['player_score']
    computer_score = session['computer_score']
    player_die = session['player_die']
    winner = None

    print(f"index: player_score (before POST) = {player_score}") # Debugging

    if player_score >= 2001:
        winner = 'Player'
    elif computer_score >= 2001:
        winner = 'Computer'

    if request.method == 'POST' and not winner:  # Only process rolls if there's no winner
        player_die = request.form.get('player_die')
        session['player_die'] = player_die  # Update session with chosen die
        player_roll = roll_dice(player_die)
        player_score = calculate_new_score(player_score, player_roll)
        session['player_score'] = player_score  # Update session

        computer_die = random.choice(list(DICE_TYPES.keys()))
        computer_roll = roll_dice(computer_die)
        computer_score = calculate_new_score(computer_score, computer_roll)
        session['computer_score'] = computer_score  # Update session

        if player_score >= 2001:
            winner = 'Player'
        elif computer_score >= 2001:
            winner = 'Computer'

    print(f"index: player_score (before render) = {player_score}") # Debugging

    return render_template('index.html', player_score=player_score, computer_score=computer_score, player_roll=player_roll if 'player_roll' in locals() else None, computer_roll=computer_roll if 'computer_roll' in locals() else None, player_die=player_die, winner=winner)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)