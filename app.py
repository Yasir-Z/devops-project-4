from flask import Flask, jsonify

app = Flask(__name__)


def calculate_priority(task_count):
    """Logic to determine task priority based on quantity."""
    if task_count > 5:
        return "High"
    elif task_count > 0:
        return "Medium"
    return "Low"


@app.route("/status")
def get_status():
    """Health check endpoint that includes logic results."""
    priority = calculate_priority(3)
    return jsonify({"status": "Active", "priority": priority})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
