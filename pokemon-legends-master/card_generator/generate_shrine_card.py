from config import *
from utils import xy, read_cube_shirne, get_img, wrap_text
from io import BytesIO
import pandas as pd
import requests
from PIL import Image, ImageDraw
from tqdm import tqdm

print('Generating Shrine Cards.....')


def run(overwrite=False):
    try:
        SHRINE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    except OSError:
        if overwrite:
            print('Error to generate Dir patch')
        else:
            print(' already exists, skipping...')
    else:
        if overwrite:
            SHRINE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def get_base():
    return get_img(SHRINE_CARD_DIR / 'ShireModel2.PNG', xy(14.5, 7.5))


def get_pokemon_art(carddf):
    pokemon_art_size = get_size()

    try:
        pokemon_art_img = get_img(ASSETS_DIR / 'pokemon' / f'{carddf.pokedex_number}.png',
                                  xy(pokemon_art_size, pokemon_art_size))
    except (FileNotFoundError, AttributeError):
        response = requests.get(f'{ART_FORM_URL}/{carddf.pokedex_number}.png')
        pokemon_art_img = get_img(BytesIO(response.content), xy(pokemon_art_size, pokemon_art_size))
        pokemon_art_img.save(ASSETS_DIR / 'pokemon' / f'{carddf.pokedex_number}.png')
    return pokemon_art_img


def get_size():
    min_size = 7
    max_size = 11
    return max(min(11 // 2 + 3, max_size), min_size)


def add_pokemon_art(img, shrinerow):
    pokemon_art_img = get_pokemon_art(shrinerow)
    img.paste(pokemon_art_img, xy((16 - pokemon_art_img.width / 64) / 2, (20 - pokemon_art_img.height / 64) / 2),
              pokemon_art_img)


def add_shireplace(img, shrinerow):

    Shrineimage = Image.open(TOKEN_DIR / f'{shrinerow.Shrine}.png').convert('RGBA').resize(xy(3.5, 3.5))
    img.paste(Shrineimage, xy(-0.35, 16.35), Shrineimage)

    if pd.isnull(shrinerow.description):
        return
    d = ImageDraw.Draw(img)
    description = wrap_text(shrinerow.Shrine_place, d, BARLOW_64, max_width=17.5)
    d.multiline_text(xy(7.25, 18), description, fill=WHITE_COLOUR, font=BARLOW_64, anchor='mm', align='center')


def get_shrine_art(shrinerow):
    pokemon_art_size = get_size(shrinerow)
    try:
        pokemon_art_img = get_img(ASSETS_DIR / 'pokemon' / f'{shrinerow.pokedex_number:03}.png',
                                  xy(pokemon_art_size, pokemon_art_size))
    except (FileNotFoundError, AttributeError):
        response = requests.get(f'{ART_FORM_URL}/{shrinerow.pokedex_number:03}.png')
        pokemon_art_img = get_img(BytesIO(response.content), xy(pokemon_art_size, pokemon_art_size))
        pokemon_art_img.save(ASSETS_DIR / 'pokemon' / f'{shrinerow.pokedex_number:03}.png')
    return pokemon_art_img


def get_shrine_types(shrinerow):
    return [type_ for type_ in shrinerow.Shrine_place if not pd.isnull(type_)]


def add_description(img, shrinerow):
    d = ImageDraw.Draw(img)
    #    6.25, 18.75)
    # Legendary Encounter
    d.text(xy(2.25, 20.75), shrinerow.encounter_type, fill=WHITE_COLOUR, font=BARLOW_80, anchor='lm')
    # Legendary Encounter
    description = wrap_text(shrinerow.card_descriptions, d, BARLOW_60, max_width=14.45)
    d.multiline_text(xy(7.99, 23.75), description, fill=WHITE_COLOUR, font=BARLOW_60, anchor='mm', align='center')


def add_text(img, shrinerow):
    d = ImageDraw.Draw(img)
    types = get_shrine_types(shrinerow)

    # Pokémon Name
    if not pd.isnull(shrinerow.pokedex_name):
        d.text(xy(1.5, 2.5), shrinerow.pokedex_name, fill=WHITE_COLOUR, font=BARLOW_48, anchor='lm')

    # Pokémon Description
    d.text(xy(1.5, 1.5), shrinerow.Shrine_title,
           fill=WHITE_COLOUR, font=BARLOW_96 if pd.isnull(shrinerow.Shrine_title) else BARLOW_80, anchor='lm')


# Functions

def compose_base():
    card_base = 'ShireModel2'
    shire_base = Image.open(SHRINE_CARD_DIR / f'{card_base}.png').convert('RGBA').resize(xy(16, 28))
    return shire_base


def run(overwrite=False):
    print('Generating Shrine cards:')

    SHRINE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    carddf = read_cube_shirne(sheet_name='Shrine')

    for i, shrinerow in tqdm(carddf.iterrows(), total=carddf.shape[0]):
        output_path = SHRINE_OUTPUT_DIR / f'{i}_{shrinerow.pokedex_name.lower()}.png'
        if output_path.is_file() and not overwrite:
            continue

        base_img = compose_base()
        img = Image.new('RGBA', xy(16, 28))
        add_pokemon_art(img, shrinerow)
        add_shireplace(img, shrinerow)
        add_text(img, shrinerow)
        add_description(img, shrinerow)
        base_img.paste(img, xy(0, 0), img)
        base_img.save(output_path)

        imgback = get_img(SHRINE_CARD_DIR / f'{shrinerow.back_card}.png', xy(16, 28))
        imgback.save(SHRINE_OUTPUT_DIR/  f'{shrinerow.back_card}.png')


if __name__ == '__main__':
    run(overwrite=True)
