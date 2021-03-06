from pathlib import Path
from PIL import ImageFont

COMPONENT_DIR = Path(__file__).parent
ROOT_DIR = COMPONENT_DIR.parent
ASSETS_DIR = COMPONENT_DIR.parent / 'assets' / 'card_generator'
SHRINE_CARD_DIR = COMPONENT_DIR.parent / 'assets' / 'cards' / 'shrine_cards'
TOKEN_DIR = COMPONENT_DIR.parent / 'assets' / 'tokens' / 'world_tokens'
OUTPUT_DIR = COMPONENT_DIR / 'output'
MOVES_OUTPUT_DIR = OUTPUT_DIR / 'moves'
SHRINE_OUTPUT_DIR = OUTPUT_DIR / 'shrine_cards'
CARD_FRONTS_OUTPUT_DIR = OUTPUT_DIR / 'card_fronts'
CARD_BACKS_OUTPUT_DIR = OUTPUT_DIR / 'card_backs'
DECKS_OUTPUT_DIR = OUTPUT_DIR / 'decks'
CARD_FRONTS_DECK_IMG = '{j}_card_fronts_deck.png'
CARD_BACKS_DECK_IMG = '{j}_card_backs_deck.png'
DECKS_OBJECTS_OUTPUT_DIR = OUTPUT_DIR / 'deck_objects'
CARD_OBJECT_TEMPLATE = ASSETS_DIR / 'card_object_template.json'
DECK_OBJECT_TEMPLATE = ASSETS_DIR / 'deck_object_template.json'

ART_FORM_URL = 'https://www.serebii.net/pokemon/art'

# Fonts
FONT_DIR = ASSETS_DIR / 'fonts'
FONT_ORIENTAL = str(FONT_DIR / 'la_oriental.otf')
ORIENTAL_80 = ImageFont.truetype(FONT_ORIENTAL, size=80)
ORIENTAL_96 = ImageFont.truetype(FONT_ORIENTAL, size=96)
ORIENTAL_102 = ImageFont.truetype(FONT_ORIENTAL, size=102)
BARLOW_36 = ImageFont.truetype(str(ASSETS_DIR / 'fonts' / 'barlow.ttf'), size=36)
BARLOW_48 = ImageFont.truetype(str(ASSETS_DIR / 'fonts' / 'barlow.ttf'), size=48)
BARLOW_60 = ImageFont.truetype(str(ASSETS_DIR / 'fonts' / 'barlow.ttf'), size=60)
BARLOW_64 = ImageFont.truetype(str(ASSETS_DIR / 'fonts' / 'barlow.ttf'), size=64)
BARLOW_80 = ImageFont.truetype(str(ASSETS_DIR / 'fonts' / 'barlow.ttf'), size=80)
BARLOW_96 = ImageFont.truetype(str(ASSETS_DIR / 'fonts' / 'barlow.ttf'), size=96)

# Colours
DARK_COLOUR = (37, 37, 50)
WHITE_COLOUR = (255, 255, 255)

CARD_FRONTS_DECK_CLOUD_URLS = [
    'http://cloud-3.steamusercontent.com/ugc/1792989789157145036/3941A9D7703CBABAB8488362D217AE390AE9D045/',
    'http://cloud-3.steamusercontent.com/ugc/1792989789157145598/153FD8EF51D566920228DCF165C3C610F1BBD044/',
    'http://cloud-3.steamusercontent.com/ugc/1792989789157145848/4091FB1BC9770716091D6AED48E5F6C7FFFE62E2/',
    'http://cloud-3.steamusercontent.com/ugc/1792989789157146144/09B04EBBDB39DA9CB49CE5BFE549B720AB112E77/'
]
CARD_BACKS_DECK_CLOUD_URLS = [
    'http://cloud-3.steamusercontent.com/ugc/1792989789157144934/1B38D25DDE41DC99D43E0713C03BB13CF08147A8/',
    'http://cloud-3.steamusercontent.com/ugc/1792989789157145142/24DF23D0DBD71BC1DBF27BEF2632F51AF6CAB208/',
    'http://cloud-3.steamusercontent.com/ugc/1792989789157145753/A2DD2DE48EDD99C2FB3CD0346CD300A48CA71C16/',
    'http://cloud-3.steamusercontent.com/ugc/1792989789157145989/049E2278A7BE62C712BCBA877B24BDF831F7DB78/'
]

MODERATE_ENCOUNTER_THRESHOLD = 13
STRONG_ENCOUNTER_THRESHOLD = 17

# Type Chart

NORMAL = 'normal'
FIRE = 'fire'
WATER = 'water'
ELECTRIC = 'electric'
GRASS = 'grass'
ICE = 'ice'
FIGHTING = 'fighting'
POISON = 'poison'
GROUND = 'ground'
FLYING = 'flying'
PSYCHIC = 'psychic'
BUG = 'bug'
ROCK = 'rock'
GHOST = 'ghost'
DRAGON = 'dragon'
DARK = 'dark'
STEEL = 'steel'
FAIRY = 'fairy'

IMMUNE = 'immune'
RESIST = 'resist'
REGULAR = 'regular'
WEAK = 'weak'

TYPE_CHART = {
    NORMAL: {IMMUNE: [GHOST], RESIST: [ROCK, STEEL], WEAK: []},
    FIRE: {IMMUNE: [], RESIST: [FIRE, WATER, ROCK, DRAGON], WEAK: [GRASS, ICE, BUG, STEEL]},
    WATER: {IMMUNE: [], RESIST: [WATER, GRASS, DRAGON], WEAK: [FIRE, GROUND, ROCK]},
    ELECTRIC: {IMMUNE: [GROUND], RESIST: [ELECTRIC, GRASS, DRAGON], WEAK: [WATER, FLYING]},
    GRASS: {IMMUNE: [], RESIST: [FIRE, GRASS, POISON, FLYING, BUG, DRAGON, STEEL], WEAK: [WATER, GROUND, ROCK]},
    ICE: {IMMUNE: [], RESIST: [FIRE, WATER, ICE, STEEL], WEAK: [GRASS, GROUND, FLYING, DRAGON]},
    FIGHTING: {IMMUNE: [GHOST], RESIST: [POISON, FLYING, PSYCHIC, BUG, FAIRY], WEAK: [NORMAL, ICE, ROCK, DARK, STEEL]},
    POISON: {IMMUNE: [STEEL], RESIST: [POISON, GROUND, ROCK, GHOST], WEAK: [GRASS, FAIRY]},
    GROUND: {IMMUNE: [FLYING], RESIST: [GRASS, BUG], WEAK: [FIRE, ELECTRIC, POISON, ROCK, STEEL]},
    FLYING: {IMMUNE: [], RESIST: [ELECTRIC, ROCK, STEEL], WEAK: [GRASS, FIGHTING, BUG]},
    PSYCHIC: {IMMUNE: [DARK], RESIST: [PSYCHIC, STEEL], WEAK: [FIGHTING, POISON]},
    BUG: {IMMUNE: [], RESIST: [FIRE, FIGHTING, POISON, FLYING, GHOST, STEEL, FAIRY], WEAK: [GRASS, PSYCHIC, DARK]},
    ROCK: {IMMUNE: [], RESIST: [FIGHTING, GROUND, STEEL], WEAK: [FIRE, ICE, FLYING, BUG]},
    GHOST: {IMMUNE: [NORMAL], RESIST: [DARK], WEAK: [PSYCHIC, GHOST]},
    DRAGON: {IMMUNE: [FAIRY], RESIST: [STEEL], WEAK: [DRAGON]},
    DARK: {IMMUNE: [], RESIST: [FIGHTING, DARK, FAIRY], WEAK: [PSYCHIC, GHOST]},
    STEEL: {IMMUNE: [], RESIST: [FIRE, WATER, ELECTRIC, STEEL], WEAK: [ICE, ROCK, FAIRY]},
    FAIRY: {IMMUNE: [], RESIST: [FIRE, POISON, STEEL], WEAK: [FIGHTING, DRAGON, DARK]}
}
# TYPE_COLOURS = {
#     NORMAL: {144 / 255, 153 / 255, 161 / 255},
#     FIRE: {255 / 255, 156 / 255, 84 / 255},
#     WATER: {77 / 255, 144 / 255, 213 / 255},
#     ELECTRIC: {243 / 255, 210 / 255, 59 / 255},
#     GRASS: {99 / 255, 187 / 255, 91 / 255},
#     ICE: {116 / 255, 206 / 255, 192 / 255},
#     FIGHTING: {206 / 255, 64 / 255, 105 / 255},
#     POISON: {171 / 255, 106 / 255, 200 / 255},
#     GROUND: {217 / 255, 119 / 255, 70 / 255},
#     FLYING: {143 / 255, 168 / 255, 221 / 255},
#     PSYCHIC: {249 / 255, 113 / 255, 118 / 255},
#     BUG: {144 / 255, 193 / 255, 44 / 255},
#     ROCK: {199 / 255, 183 / 255, 139 / 255},
#     GHOST: {82 / 255, 105 / 255, 172 / 255},
#     DRAGON: {10 / 255, 109 / 255, 196 / 255},
#     DARK: {90 / 255, 83 / 255, 102 / 255},
#     STEEL: {90 / 255, 142 / 255, 161 / 255},
#     FAIRY: {236 / 255, 143 / 255, 230 / 255}
# }

EFFECTIVENESS_COLOURS = {IMMUNE: (250, 150, 150), RESIST: (250, 200, 150), WEAK: (150, 200, 150)}
