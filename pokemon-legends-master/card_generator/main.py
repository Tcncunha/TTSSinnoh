import generate_moves
import generate_pokemon
import generate_decks
import generate_deck_objects
import generate_shrine_card

def run_all(overwrite=False):

    generate_moves.run(overwrite)
    generate_pokemon.run(overwrite)
    generate_decks.run()
    generate_deck_objects.run()
    generate_shrine_card.run(overwrite)




if __name__ == '__main__':
    run_all(overwrite=False)
