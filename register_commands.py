import requests
import yaml
from key import get_key, get_application_id

# need to find a way to export this code and run it from main
URL = f"https://discord.com/api/v9/applications/{get_application_id()}/commands"

with open("discord_commands.yaml", "r") as file:
    yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
headers = {
    "Authorization": f"Bot {get_key()}",
    "Content-type": "application/json"
}

# send POST request
for command in commands:
    response = requests.post(URL, json=command, headers=headers)
    command_name = command["name"]
    print(f"Command {command_name} created: {response.status_code}")
