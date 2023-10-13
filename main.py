import requests
import json

# Pregunta 1: ¿Cuantos personajes existen?
base_url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(base_url)
count_data = response.json()
total_pokemon = count_data["count"]
print(f"1. ¿Cuantos personajes existen? {total_pokemon}\n")

# Pregunta 2: Imprimir en pantalla "{name}-{status}-{species}" para todos los personajes.
pokemon_data = []
numero_pokemon = 50
for i in range(1, numero_pokemon + 1):
    url = f"{base_url}{i}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        nombre = data["name"]
        estado = data["species"]["name"]
        tipos = "-".join(tipo["type"]["name"] for tipo in data["types"])
        print(f"{nombre}-{estado}-{tipos}")
print("\n")

# Pregunta 3: Agruparlos por género (Male o Female) y calcular su respectiva cantidad teniendo en cuenta que cada especie hay 8 pokemones
gender_counts = {"Both": 0, "Male": 0, "Female": 0, "Genderless": 0}
for i in range(1, numero_pokemon + 1):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{i}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        gender_rate = data["gender_rate"]
        if gender_rate == -1:
            gender_counts["Genderless"] += 1
        elif gender_rate == 0:
            gender_counts["Male"] += 1
        elif gender_rate == 8:
            gender_counts["Female"] += 1
        else:
            gender_counts["Both"] += 1

print("3. Agrupar por género y calcular su cantidad:")
#gender_rate: Este campo indica la tasa de género del Pokémon, 
#que puede ser -1 (sin género definido), 0 (100% masculino), 
#8 (100% femenino) o entre 0 y 8 (género masculino y femenino). 

for gender, count in gender_counts.items():
    print(f"{gender}: {count} Pokémon")

# Pregunta 4: Agruparlos por Especies y calcular su respectiva cantidad
species_counts = {}
for i in range(1, numero_pokemon + 1):
    url = f"{base_url}{i}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        species = data["species"]["name"]
        if species in species_counts:
            species_counts[species] += 1
        else:
            species_counts[species] = 1
print("\n4. Agrupar por Especies y calcular su cantidad:")
for species, count in species_counts.items():
    print(f"{species}: {count} Pokémon")

# Pregunta 5: Indicar los 5 personajes con mayores apariciones (campo 'episode') se usa el campo game_indices ya que no se encontró el campo episode. 
top_characters = []
for i in range(1, numero_pokemon + 1):
    url = f"{base_url}{i}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        episode_count = len(data["game_indices"])
        top_characters.append((name, episode_count))
top_characters.sort(key=lambda x: x[1], reverse=True)
print("\n5. Los 5 personajes con mayores apariciones:")
for i, (name, episode_count) in enumerate(top_characters[:5]):
    print(f"{i+1}. {name} - Apariciones: {episode_count}")