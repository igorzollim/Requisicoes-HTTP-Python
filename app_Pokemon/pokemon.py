import requests
from exception import PokemonNotFound

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def exibe_pokemon(dados_pokemon):
    print('  Nome: {}'.format(dados_pokemon['name']))
    print('  Abilidades: ')
    for x in dados_pokemon['abilities']:
        print('     {}'.format(x['ability']['name']))

    print('  Imagem do pokemon:{}'.format(dados_pokemon['sprites']['front_shiny']))

def pokemon_disponivel(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/')
    lista_pokemons = response.json()

    for x in lista_pokemons['results']:
        if pokemon == x['name']:
            return True

    return False

if __name__ == '__main__':
    while True:
        try:
            nome_pokemon = input('Escolha um pokemon: ')

            if pokemon_disponivel(nome_pokemon):
                dados_pokemon = retorna_dados_pokemon(nome_pokemon)
                exibe_pokemon(dados_pokemon)
                break
            else:
                raise PokemonNotFound('Pokemon não encontrado!')

        except PokemonNotFound as ex:
            print(ex)