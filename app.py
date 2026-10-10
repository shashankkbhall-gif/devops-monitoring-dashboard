from flask import Flask, render_template
import psutil
import platform

app = Flask(__name__)

@app.route("/")
def dashboard():
    stats = {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent if platform.system() != "Windows" else psutil.disk_usage("C:\\").percent,
        "system": platform.system(),
        "hostname": platform.node()
    }
    return render_template("index.html", stats=stats)

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)