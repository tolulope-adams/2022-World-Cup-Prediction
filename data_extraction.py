import re
import requests
from bs4 import BeautifulSoup
from player import Player
from country import Country

WC_SQUAD_LIST_URL = "https://www.skysports.com/football/news/12098/12741629/world-cup-2022-squad-lists-england-brazil-argentina-france-germany-spain-and-more"


def find_players(squad_list):
    players_list = []
    player_postions = ["GK", "DF", "MF", "FW"]
    response = requests.get(squad_list)
    soup = BeautifulSoup(response.content, "html.parser")
    groups = soup.find_all('h2', string = re.compile('Group'))
    for group in groups:
        for i in range(4):
            team = group.find_next_siblings("h3")[i]
            for j in range(4):
                position = team.find_next_siblings("p")[j]
                players = position.get_text().split(":")[1]
                for player in players.split(", "):
                    player_name = player.split("(")[0]
                    # player_name = player_name.replace(',', '')
                    player_name = player_name.strip()

                    if(len(player.split("(")) > 1):
                        club_name = player.split("(")[1]
                    
                    club_name = club_name.replace(')', '')
                    club_name = club_name.replace('.', '')
                    club_name = club_name.strip()

                    player_obj = Player(player_name)
                    player_obj.set_country(team.get_text())
                    player_obj.set_position(player_postions[j])
                    player_obj.set_club_name(club_name)
                    players_list.append(player_obj)

    return players_list

def find_league(club_name):
    res = requests.get("https://en.wikipedia.org/wiki/" + club_name)
    soup = BeautifulSoup(res.content, "html.parser")
    league = soup.find('th', string = re.compile('League'))
    return league.find_next_siblings("td")[0].get_text()

def find_league_website(league):
    res = requests.get("https://en.wikipedia.org/wiki/" + league)
    soup = BeautifulSoup(res.content, "html.parser")
    website = soup.find('th', string = re.compile('Website'))
    website_link = website.find_next_siblings("td")[0].get_text()
    return website_link

def create_players_file(players_list):
    file = open("players.txt", "w")
    file.write("Name" + "," + "Country" + "," + "Position" + "," + "Goals" + "," 
        + "Assists" + "," + "Tackles" + "," + "Saves" + "," + "Club" + "," 
        + "League" + "," + "League_Website"
    )
    file.write("\n")
    count = 0
    for player in players_list:
        file.write(player.get_name() + "," + player.get_country() + "," 
            + player.get_position() + "," + player.get_goals_scored() + "," 
            + player.get_goals_assisted() + "," + player.get_tackles_won() + "," 
            + player.get_saves() + "," + player.get_club_name() + "," 
            + player.get_club_league() + "," + player.get_league_website()
        )
        file.write("\n")     
    file.close()
    print(True)

players = find_players(WC_SQUAD_LIST_URL)
create_players_file(players)

# def start_extraction():
#     for player in players:
#         player.set_league(find_league(player.get_club_name()))
#         player.set_league_website(find_league_website(player.get_league()))
# start_extraction()


# def confirm_extraction(countries):
#     if len(countries) < 32:
#         return False
        
# def extract_win_rate():
#     win_rate = 0
#     return win_rate

# def extract_passes_completed():
#     passes_completed = 0
#     return passes_completed

# def extract_total_goals_scored():
#     total_goals_scored = 0
#     return total_goals_scored

# def extract_total_goals_conceeded():
#     total_goals_scored = 0
#     return total_goals_scored

# #---------- Individual variables ----------
# def extract_players():
#     players = []
#     return players

# def extract_goals():
#     goals = 0
#     return goals

# def extract_assists():
#     assists = 0
#     return assists

# def extract_tackles_won():
#     tackles_won = 0
#     return tackles_won

# def extract_saves():
#     saves = 0
#     return saves










