# Discord Bots

## whitelister.py
> whitelister.py is a simple discord bot written using the python API. You can invite it to your servers to automate the access control of the minecraft server running in the local `screen` session named 'minecraft'. All commands are sent from the discord bot to the minecraft server via the `screen` session.
> Read the manual for `screen` by typing  `man screen` in your linux terminal.
> Commands are sent to the server in the following format:
```
screen -S minecraft -X stuff "/say this is an automatic server command!^M"
```
> whitelister.py is still a WIP as of 09/19/25, but the commands available to discord admins will look something like this:
- `/whitelist add [playername]` -> `/whitelist add [playername]`
- `/whitelist remove [playername]` -> `/whitelist remove [playername]`
- `/whitelist list` -> `/whitelist list`
> That last command, `list`, requires that the shell output be sent secretly back to the discord admin that sent it. No other discord users may see the output of a command, and the commands sent by discord admins will be automatically deleted from discord channels to prevent spam.
> Shell output is provided to whitelist.py in a digestible manner using the following command:
```
screen -S minecraft -X hardcopy ~/DiscordBots/hardcopy.txt
```
> whitelister.py may then process the output text
