from flask import Flask, request, jsonify

app = Flask(__name__)

# Global state
state = 0

# RESET API (VERY IMPORTANT)
@app.route("/reset", methods=["POST"])
def reset():
    global state
    state = 0
    return jsonify({
        "state": state
    })

# STEP API
@app.route("/step", methods=["POST"])
def step():
    global state

    data = request.get_json()
    action = data.get("action", 0)

    # Simple logic (you can customize later)
    if action == 1:
        state += 1
    elif action == 2:
        state -= 1

    reward = 1 if state == 10 else 0
    done = True if state == 10 else False

    return jsonify({
        "state": state,
        "reward": reward,
        "done": done
    })

# RUN SERVER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
