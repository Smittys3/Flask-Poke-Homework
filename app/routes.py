from app import app
from app.models import Pokemon, db, User
from flask import render_template, request
from app.forms import PokemonSearchForm
import requests
from .models import User

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/search', methods = ["GET", "POST"])
def savePokemon():
    form = PokemonSearchForm()
    my_dict = {}
    if request.method == "POST":
        poke_name = form.name.data

        url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
        res = requests.get(url)
        if res.ok:
            data = res.json()
            user_pokemon = []
            my_dict = {
                'name' : data['forms'][0]['name'],
                'ability' : data['abilities'][0]['ability']['name'],
                'img_url' : data['sprites']['front_shiny'],
                'hp' : data['stats'][0]['base_stat'],
                'attack' : data['stats'][1]['base_stat'],
                'defense' : data['stats'][2]['base_stat']
                }
        # else:
        #     return "Sorry not a Pokeman. Please try again."


            name = data['name']
            ability = data['abilities'][0]['ability']['name']
            
            img_url = data['sprites']['front_shiny']
            hp = data['stats'][0]['base_stat']
            attack = data['stats'][1]['base_stat']
            defense = data['stats'][2]['base_stat']
            user_pokemon.append(my_dict)
            poke = Pokemon(name, ability, img_url, hp, attack, defense)
            db.session.add(poke)
            db.session.commit()


    return render_template('searchpokemon.html', form = form, pokemon = my_dict)