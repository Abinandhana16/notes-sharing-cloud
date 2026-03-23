from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

notes = []

HTML = """
<h2>Cloud Notes App</h2>
<form method="post">
    <input type="text" name="note" placeholder="Enter note">
    <button type="submit">Add</button>
</form>
<ul>
{% for n in notes %}
<li>{{n}}</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        notes.append(request.form["note"])
    return render_template_string(HTML, notes=notes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
