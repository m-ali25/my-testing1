import streamlit as st
import pandas as pd
import requests
import numpy as np


st.title(':red[Pokemon Explorer!]')

number = st.number_input('Enter your favorite number to explore your Pokemon :sunglasses:', 1, 1000, step=1)

if st.button("Show my Pokemon's information"):
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{number}"
    response = requests.get(pokemon_url).json()

    pokemon_name = response['name']
    pokemon_height = response['height']
    pokemon_weight = response['weight']
    pokemon_image = response['sprites']
    moves = response['moves']
    species_url = response['species']['url']
    pokemon_sound = requests.get(species_url).json()

    st.title(pokemon_name.title())
    st.write(f"Your Pokemon's height is {pokemon_height}")
    st.write(f"Your Pokemon's weight is {pokemon_weight}")
    st.image(pokemon_image['front_default'])

    with st.expander("List of Moves", expanded=True):
            for move in moves:
                move_name = move['move']['name'].title()
                move_url = move['move']['url']
                
            
                move_response = requests.get(move_url).json()
                move_type = move_response['type']['name']
                move_accuracy = move_response['accuracy'] if 'accuracy' in move_response else 'N/A'
                move_power = move_response['power'] if 'power' in move_response else 'N/A'
                move_pp = move_response['pp'] if 'pp' in move_response else 'N/A'
                
                
                st.write(f"Move Name: {move_name}")
                st.write(f"* Type: {move_type}")
                st.write(f"* Accuracy: {move_accuracy}")
                st.write(f"* Power: {move_power}")

    random_pokemon_numbers = [str(i) for i in np.random.randint(1, 1000, 1)]  
    random_pokemon_data = []
    for num in random_pokemon_numbers:
        random_pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{num}"
        random_response = requests.get(random_pokemon_url).json()
        random_pokemon_data.append({
            'name': random_response['name'].title(),
            'height': random_response['height'],
            'weight': random_response['weight']
        })
    
    comparison_heights = [pokemon_height] + [data['height'] for data in random_pokemon_data]
    comparison_weights = [pokemon_weight] + [data['weight'] for data in random_pokemon_data]
    pokemon_names = [pokemon_name.title()] + [data['name'] for data in random_pokemon_data]

    st.subheader('Comparison with Other Pokemon:')
    st.bar_chart(comparison_heights)
    st.bar_chart(comparison_weights)

    
    