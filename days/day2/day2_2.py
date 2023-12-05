def get_powers_sum(games_input):
    s = 0
    for game in games_input:
        s += find_game_power(game)
    return s


def find_game_power(game):
    parts = game.split(":")
    game_id = int(parts[0].split(" ")[1])
    sets = parts[1].split(";")

    maxes = {
        "r": 0,
        "g": 0,
        "b": 0,
    }

    for s in sets:
        colors = s.strip().split(",")

        for color in colors:
            color_info = color.strip().split(" ")
            count = int(color_info[0].strip())
            color_name = color_info[1].strip()

            if count > maxes[color_name[0]]:
                maxes[color_name[0]] = count

    return maxes["r"] * maxes["g"] * maxes["b"]


###

def test_valid_game():
    # assert (4, 2, 6) == find_maxes("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    # assert (1, 3, 4) == find_maxes("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    # assert (20, 13, 6) == find_maxes("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    # assert (14, 3, 15) == find_maxes("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    # assert (6, 3, 2) == find_maxes("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")

    assert 48 == find_game_power("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert 12 == find_game_power("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
    assert 1560 == find_game_power("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    assert 630 == find_game_power("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    assert 36 == find_game_power("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")


def test_powers_sum():
    assert 2286 == get_powers_sum(read_file_as_list("ex2_2.txt"))


###

def read_file_as_list(file_name):
    with open(file_name) as file:
        file_input = []

        for line in file:
            file_input.append(line)

        return file_input


if __name__ == "__main__":
    games_input = read_file_as_list("ex2_2.txt")
    result = get_powers_sum(games_input)
    print(result)

    games_input = read_file_as_list("in2_2.txt")
    result = get_powers_sum(games_input)
    print(result)
