class Country:
    def __init__(self, name):
        self.name = name
        self.players = []

    def get_name(self):
        return self.name

    def get_players(self):
        return self.players

    def add_player(self, player):
        self.players.append(player)

    def add_players(self, players):
        self.players.extend(players)


    def remove_player(self, player):
        players.remove(player)

    def count_win_rate():
        return None

    def count_clean_sheets():
        return None

    def count_total_goals_scored():
        return None

    def count_total_goals_conceeded():
        return None

    def count_passes_completed():
        return None