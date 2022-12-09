"""
    Sh#t no one reads.

    ! SUMMARY !
    This is a simple flask app that uses the flask framework to create a web app.
    It would then grab the Webhook from WebCaptioner and prints the data to the console.

    ! HOW TO USE !
    1. Install the requirements
    2. Run the app.py file
    3. Go to the WebCaptioner website and create a new project
    4. Add the webhook to the project based on the ROUTE and PORT variables
        4.1 EG: http://localhost:52842/listener
        4.2 > ROUTE = "listener"
        4.3 > PORT = 52842
    5. Start the project
    6. Edit to your hearts content
    7. Profit

"""

import os, json, logging
from flask import Flask, request, make_response

ROUTE = "listener"
PORT = 52842

os.system("cls")
app = Flask(__name__)
    
@app.route(f'/{ROUTE}', methods=['POST', 'PUT'])
def listener():
    print(f"\033[95m{json.loads(request.get_data(as_text=True))['transcript']}\033[0m")
    return make_response(json.dumps({"message": "Success"}), 200)

logging.getLogger("werkzeug").setLevel(logging.ERROR)
app.run(host="localhost", port=PORT, debug=False)