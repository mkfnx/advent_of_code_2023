from helpers import read_file_as_list

maxes = {
    "r": 12,
    "g": 13,
    "b": 14
}


def get_valid_games_sum(games_input):
    s = 0
    for game in games_input:
        s += validate_game(game)
    return s


def validate_game(game):
    parts = game.split(":")
    game_id = int(parts[0].split(" ")[1])
    sets = parts[1].split(";")

    for s in sets:
        colors = s.strip().split(",")

        for color in colors:
            color_info = color.strip().split(" ")
            count = int(color_info[0].strip())
            color_name = color_info[1].strip()

            if count > maxes[color_name[0]]:
                return 0

    return game_id


###

def test_valid_game():
    assert 1 == validate_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert 2 == validate_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    assert 0 == validate_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    assert 0 == validate_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    assert 5 == validate_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")


def test_valid_games_sum():
    assert 8 == get_valid_games_sum(read_file_as_list("ex2.txt"))

###


if __name__ == "__main__":
    games_input = read_file_as_list("ex2_2.txt")
    result = get_valid_games_sum(games_input)
    print(result)

    games_input = read_file_as_list("in2_2.txt")
    result = get_valid_games_sum(games_input)
    print(result)
