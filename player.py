class Player:
    def __init__(self, name):
        self.name = name
        self.country = "Unknown"
        self.position = "Unknown"
        self.goals_scored = "Unknown"
        self.goals_assisted = "Unknown"
        self.tackles = "Unknown"
        self.saves = "Unknown"
        self.club_name = "Unknown"
        self.league = "Unknown"
        self.league_website = "Unknown"


    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_goals_scored(self):
        return self.goals_scored

    def set_goals_scored(self, goals):
        self.goals_scored = goals

    def get_goals_assisted(self):
        return self.goals_assisted

    def set_goals_assisted(self, assists):
        self.goals_assisted = assists

    def get_tackles_won(self):
        return self.tackles

    def set_tackles_won(self, tackles):
        self.tackles = tackles

    def get_saves(self):
        return self.saves

    def set_saves(self, saves):
        self.saves = saves

    def get_club_name(self):
        return self.club_name

    def set_club_name(self, club_name):
        self.club_name = club_name

    def get_club_league(self):
        return self.league

    def set_club_league(self, league):
        self.league = league

    def get_league_website(self):
        return self.league_website

    def set_league_website(self, league_website):
        self.league_website = league_website