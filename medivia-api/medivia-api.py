import readers
from utilities import is_url
from scrapper import get_page_content

class Medivia:
    online_url = 'https://medivia.online/community/online/'
    characters_url = 'https://medivia.online/community/character/'
    base_guild_url = 'https://medivia.online/community/guilds/show/'

    def __init__(self, world_name):
        self.world_name = world_name

    def get_online_players(self):
        url = self.online_url + self.world_name
        return get_page_content(url, readers.read_online_players)

    def get_player_information(self, player_name):
        if player_name is None:
            print('Player name is required')
        else:
            url = self.characters_url + player_name
            return get_page_content(url, readers.read_player_information)

    def get_player_death_information(self, player_name):
        if player_name is None:
            print('Player name is required')
        else:
            url = self.characters_url + player_name
            return get_page_content(url, readers.read_player_deaths)

    def get_player_tasks_information(self, player_name):
        if player_name is None:
            print('Player name is required')
        else:
            url = self.characters_url + player_name
            return get_page_content(url, readers.read_player_tasks)

    def get_guild_information(self, guild_id_or_url):
        url = ''
        url_or_id = guild_id_or_url
        is_by_url = is_url(url_or_id)
        if not is_by_url:
            url = self.base_guild_url + url_or_id
        return get_page_content(url, readers.read_guild_information)
