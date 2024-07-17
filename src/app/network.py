from flask import Flask, jsonify, request
from discord_interactions import verify_key_decorator
from key import get_public_key

app = Flask(__name__)

# I have no idea what this does


def start_network() -> None:
    @app.route("/", methods=["POST"])
    async def interactions():
        raw_request = request.json
        print(f"Request: {raw_request}")
        return interact(raw_request)

    # @verify_key_decorator(get_public_key())
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

app.run(debug=True)