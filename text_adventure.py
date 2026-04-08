def get_choice(valid_choices):
    """Prompt until the player enters one of the allowed choices."""
    while True:
        choice = input("> ").strip().lower()
        if choice in valid_choices:
            return choice
        print(f"Please choose one of: {', '.join(valid_choices)}")


def play_game():
    print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.")
    print("Which one do you want to pick up? (match/flashlight)")

    first_choice = get_choice(["match", "flashlight"])

    if first_choice == "match":
        print()
        print("You pick up the match and strike it, and for an instant, the forest around you is illuminated.")
        print("You see a large grizzly bear, and then the match burns out.")
        print("Do you want to RUN, or HIDE behind a tree? (run/hide)")

        second_choice = get_choice(["run", "hide"])

        if second_choice == "run":
            print()
            print("You run as fast as you can and escape the bear.")
            print("After a few minutes, you find a cabin and make it to safety.")
        else:
            print()
            print("You hide behind a tree, but the bear finds you.")
            print("Game over.")

    else:
        print()
        print("You pick up the flashlight and turn it on.")
        print("You see the pathway lit up in front of you, but you thought you also heard something off to the side.")
        print("Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? (follow/look)")

        second_choice = get_choice(["follow", "look"])

        if second_choice == "follow":
            print()
            print("You follow the path and safely find your way out of the forest.")
        else:
            print()
            print("You look into the trees and discover it was only a curious owl.")
            print("Relieved, you return to the path and leave the forest safely.")


if __name__ == "__main__":
    play_game()
