from flask import Flask, url_for, render_template, jsonify, request, redirect
import json



app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232dfhskadfghjkoasdfghgyhjilthtghuo;[#'
socketio = SocketIO(app)
setbutton = False


things = [
    { 'direction': None, 'forwards': None}
]
def movel():
    global thing
    print("hit")
    thing = [
    { 'direction': 1, 'forwards': 1}
]
    return(thing)
def mover():
    global thing
    thing = [
    { 'direction': 2, 'forwards': 1}
]
    return(thing)
def movef():
    global thing
    thing = [
    { 'direction': 0, 'forwards': 1}
]
    return(thing)

@app.route('/api/main', methods=['POST', 'GET'])
def main():
    return(jsonify(thing))


@app.route('/', methods=['POST'])
def main2():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('movel') == 'movel':
            movel()
            print("movel")
        elif  request.form.get('movef') == 'movef':
            mover()
            print("movef")
        elif  request.form.get('mover') == 'mover':
            movef()
            print("mover")
        else:
            # pass # unknown
            return(render_template('main.html'))
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return(render_template('main.html'))
    





if __name__ == "__main__":
    app.run()
