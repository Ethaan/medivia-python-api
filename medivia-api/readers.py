from utilities import camelize, encode_string


def read_online_players(html):
    online_data = []
    online_user_data = {}
    ul = html.findAll('ul')[1]
    counter = 0
    for div in ul.findAll('div'):
        text = encode_string(div.get_text())
        if counter == 0:
            online_user_data['last_login'] = text
        elif counter == 1:
            online_user_data['name'] = encode_string(div.find('a').get_text())
        elif counter == 2:
            online_user_data['vocation'] = text
        elif counter == 3:
            online_user_data['level'] = text
        else:
            online_data.append(online_user_data)
            online_user_data = {}
            counter = 0
        counter += 1
    del online_data[0]
    return online_data

def read_player_information(html):
    player_information = {}
    div_container = html.find('div', { 'class': 'med-character' })
    div_information = div_container.find('div', { 'class': ['med-width-50', 'med-white-space-normal']})
    for div in div_information.findAll('div', { 'class': ['med-width-100', 'med-mt-10']}):
        text = ''
        for inner_div in div:
            text+= encode_string(inner_div.get_text())
        two_points_index = text.find(':')
        player_information[camelize(text[:two_points_index])] = text[two_points_index + 1:]
    return player_information

def read_player_deaths(html):
    player_death_information = []
    div_container = html.findAll('div', { 'class': 'med-show-more' })
    for div in div_container[0].findAll('div', { 'class': 'black-link' }):
        player_death_data = {}
        text = encode_string(div.get_text())
        index_of_ago = text.find('ago')
        player_death_data['date'] = text[:index_of_ago + 3]
        player_death_data['killed_by'] = text[index_of_ago + 3:]
        player_death_information.append(player_death_data)
    return player_death_information

def read_player_tasks(html):
    player_tasks_information = []
    div_container = html.findAll('div', { 'class': 'med-show-more' })
    for div in div_container[1].findAll('div', { 'class': 'black-link' }):
        text = encode_string(div.get_text())
        index_of_total = text.find('Total')
        player_tasks_information.append(text[:index_of_total])
    return player_tasks_information

def read_guild_information(html):
    guild_information = {}
    title = html.findAll('div', { 'class': 'med-guild' })[0].find('div', { 'class': 'title'})
    guild_information['title'] = encode_string(title.get_text())
    return guild_information