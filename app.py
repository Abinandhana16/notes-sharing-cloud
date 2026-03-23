from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

notes = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud Notes App</title>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(to right, #667eea, #764ba2);
            color: white;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: white;
            color: black;
            padding: 20px;
            border-radius: 10px;
            width: 400px;
            margin: auto;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        input {
            width: 70%;
            padding: 10px;
            margin: 10px;
        }
        button {
            padding: 10px 15px;
            background: #667eea;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        button:hover {
            background: #5a67d8;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            background: #f1f1f1;
            margin: 5px;
            padding: 10px;
            border-radius: 5px;
        }
        h2 {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>☁️ Cloud Notes App</h2>

    <form method="post">
        <input type="text" name="note" placeholder="Enter your note" required>
        <br>
        <button type="submit">Add Note</button>
    </form>

    <ul>
    {% for n in notes %}
        <li>{{n}}</li>
    {% endfor %}
    </ul>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        notes.append(request.form["note"])
    return render_template_string(HTML, notes=notes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
