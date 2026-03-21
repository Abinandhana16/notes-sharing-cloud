# Cloud Notes - Notes Sharing Web Application

A beginner-friendly Flask-based web application to share and save notes. This app uses in-memory storage and is ready for deployment on Render.

## Features
- Add notes via a simple UI.
- View all notes instantly on the same page.
- Clean and modern design.

## 1. How to Run Locally

### Prerequisites
- Python 3.x installed.

### Steps
1. **Clone or Download** this project to your local machine.
2. **Open a Terminal/CMD** in the project folder.
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the App**:
   ```bash
   python app.py
   ```
5. **View the App**:
   Open your browser and go to `http://127.0.0.1:5000`.

## 2. How to Upload to GitHub

1. Create a new repository on [GitHub](https://github.com/new).
2. Follow the instructions to push your local code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

## 3. How to Deploy on Render

1. Create a free account on [Render](https://render.com/).
2. Click **New +** and select **Blueprint**.
3. Connect your GitHub account and select your repository.
4. Render will automatically detect the `render.yaml` file.
5. Click **Approve** to deploy.
6. Once the build is complete, you'll receive a URL for your live app (e.g., `https://cloud-notes-app.onrender.com`).

---

## Technical Details
- **Backend**: Python Flask
- **Frontend**: HTML5, Vanilla CSS
- **Deployment**: Render Cloud Platform
- **Production Server**: Gunicorn

## Sample Output
- When you open the app, you'll see a header "Cloud Notes".
- A text area to type your note.
- An "Add Note" button.
- A list of notes displayed below the form, with the most recent one at the top.

## Common Errors & Fixes
- **Error**: `ModuleNotFoundError: No module named 'flask'`
  - **Fix**: Run `pip install flask` or `pip install -r requirements.txt`.
- **Error**: `Port already in use`
  - **Fix**: Close any other running Flask apps or restart your terminal.
- **Error**: `No such file or directory: 'templates/index.html'`
  - **Fix**: Ensure the `templates` folder exists and contains `index.html`.
