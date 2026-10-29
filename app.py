from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)
candidates = []

PAGE = """
<!doctype html><html><head><title>Simple Voting System — v1</title>
<style>body{font-family:Arial;max-width:760px;margin:40px auto;padding:0 16px;background:#f5f7fb}
.card{background:white;padding:24px;border-radius:12px;box-shadow:0 2px 12px #ddd}
input,button{padding:10px;margin:5px 0}button{cursor:pointer}li{margin:8px 0}</style></head>
<body><div class="card"><h1>Simple Voting System — v1</h1>
<p>Version 1: Add candidates and view the candidate list.</p>
<form method="post" action="/add"><input name="name" placeholder="Enter candidate name" required>
<button type="submit">Add Candidate</button></form>
<h2>Candidates</h2>{% if candidates %}<ul>{% for c in candidates %}<li>{{c}}</li>{% endfor %}</ul>
{% else %}<p>No candidates added yet.</p>{% endif %}
</div></body></html>
"""

@app.get("/")
def home():
    return render_template_string(PAGE, candidates=candidates)

@app.post("/add")
def add_candidate():
    name = request.form.get("name", "").strip()
    if name and name not in candidates:
        candidates.append(name)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
