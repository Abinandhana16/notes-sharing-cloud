from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for notes
# In a real-world app, you would use a database like PostgreSQL or MongoDB
notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get note from form
        note_content = request.form.get("note")
        if note_content:
            # Add note to the top of the list
            notes.insert(0, note_content)
        return redirect(url_for("index"))
    
    # Render the page with the list of notes
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    # Run the app locally for development
    app.run(debug=True)
