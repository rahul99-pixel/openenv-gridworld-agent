from flask import Flask, request, jsonify

app = Flask(__name__)

state = 0

# ✅ IMPORTANT: allow POST + GET (fixes your error)
@app.route("/reset", methods=["POST", "GET"])
def reset():
    global state
    state = 0
    return jsonify({"state": state})

# ✅ IMPORTANT: allow POST + GET
@app.route("/step", methods=["POST", "GET"])
def step():
    global state

    if request.method == "POST":
        data = request.get_json(silent=True) or {}
    else:
        data = request.args or {}

    action = int(data.get("action", 0))

    if action == 1:
        state += 1
    elif action == 2:
        state -= 1

    reward = 1 if state == 5 else 0
    done = state == 5

    return jsonify({
        "state": state,
        "reward": reward,
        "done": done
    })

# ✅ VERY IMPORTANT: correct port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
