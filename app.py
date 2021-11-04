from flask import Flask, request, jsonify
app = Flask(__name__) 

@app.route('/getmsg/', methods=['GET'])
def respond():
    name = request.args.get("name", None)
    print(f"got name {name}")

    response = {}

    if not name:
        response["ERROR"] = 'name not found, please send a name.'
    elif str(name).isdigit():
        response['ERROR'] = "Name can't be numeric."
    else:
        response['MESSAGE'] = F"Welcome {name} to here."
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)

    if param:
        return jsonify({
            "Message": f"Welcome {name} to here.",
            "METHOD": "POST"
        })

@app.route('/')
def index():
    return "Welcome to our server"
if __name__ == '__main__':
    app.run(threaded=True, port=5000)