## Python medivia API.

Easy to use [Medivia](http://www.medivia.org) API.

### Get started

`pip install medivia-api`

### How to use it.

```
from medivia-api import Medivia

medivia = Medivia('Legacy'); // World name you are using

medivia.get_online_players() // prints the whole list
```
### Methods.

`get_online_players()` - Method to get all the online players.

**Example response**
```
 {
   { name: 'Ethaanpump', level: '20', vocation: 'Elder Druid' },
   ...more,
 }
```
`get_player_information(character_name)` - Method to get the whole character information

**Example response**
```
{ 'name:': 'Ethaanpump ',
  'position:': 'player',
  ...
}
```

`get_player_death_information(character_name)` - Method to get the whole character death information by a giving name

**Example response**
```
[
  { date: 'Feb 12 2017', killed_by_message: 'Killed  at Level 258 by Fenlord.' },
  ...deaths
]
```

`get_player_tasks_information()` - Method to get the tasks from this player

**Example response**
```
[
  'Amazons',
  'Hydras',
  ..tasks
]
```

`get_guild_information(guild_url_Or_Name //guild_url or guild_id)` - Method to get the guild information by a giving guild URL or guild name.

**Example response**
```
[
  title: 'guild title'
]
```

TODO
1.- Get Guild Complete Information