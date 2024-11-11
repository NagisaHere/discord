import os
from dotenv import load_dotenv

from flask import Flask, jsonify, request
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi

from discord_interactions import verify_key_decorator

# use a WSGI server
app = Flask(__name__)
asgi_app = WsgiToAsgi(app)
handler = Mangum(asgi_app)


# I have no idea what this does

def start_network() -> None:
    @app.route("/", methods=["POST"])
    async def interactions():
        raw_request = request.json
        print(f"Request: {raw_request}")
        return interact(raw_request)

# @verify_key_decorator(os.getenv("PUBLIC_KEY"))
def interact(raw_request):
    """raw_request is in a json file"""
    if raw_request["type"] == 1:  # ping
        response_data = {"type": 1}
    else:
        # I presume the data would just be whatever is passed by the slash
        # command
        data = raw_request["data"]
        command_name = data["name"]

        if command_name == "echo":
            original_message = data["options"][0]["value"]
            message_content = f"Echoing {original_message}"

        response_data = {
            "type": 4,
            "data": {"content": message_content}
        }

    return jsonify(response_data)

# this might be the reason why this runs first before the discord client
# starts
app.run(debug=True)