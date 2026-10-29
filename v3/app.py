from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)
candidates = []
votes = {}

PAGE = """
<!doctype html><html><head><title>Simple Voting System — v3</title>
<style>body{font-family:Arial;max-width:800px;margin:40px auto;padding:0 16px;background:#f5f7fb}
.card{background:white;padding:24px;border-radius:12px;box-shadow:0 2px 12px #ddd}
input,button,select{padding:10px;margin:5px 0}button{cursor:pointer}table{border-collapse:collapse;width:100%;margin-top:12px}
td,th{border:1px solid #ddd;padding:10px;text-align:left}th{background:#eef2ff}.note{color:#555}</style></head>
<body><div class="card"><h1>Simple Voting System — v3</h1>
<p>Version 3: Add candidates, cast votes, and view the vote count.</p>
<form method="post" action="/add"><input name="name" placeholder="Enter candidate name" required>
<button type="submit">Add Candidate</button></form>
<h2>Cast a Vote</h2>
{% if candidates %}<form method="post" action="/vote"><select name="candidate" required>
{% for c in candidates %}<option value="{{c}}">{{c}}</option>{% endfor %}</select>
<button type="submit">Cast Vote</button></form>
{% else %}<p>Add a candidate before voting.</p>{% endif %}
<h2>Results — Vote Count</h2>
{% if candidates %}<table><tr><th>Candidate</th><th>Votes</th></tr>
{% for c in candidates %}<tr><td>{{c}}</td><td>{{votes.get(c, 0)}}</td></tr>{% endfor %}</table>
{% else %}<p>No results yet. Add candidates to begin.</p>{% endif %}
<p class="note">Demo only: votes are stored in memory and reset when the app restarts. Repeat voting is not restricted.</p>
</div></body></html>
"""

@app.get("/")
def home():
    return render_template_string(PAGE, candidates=candidates, votes=votes)

@app.post("/add")
def add_candidate():
    name = request.form.get("name", "").strip()
    if name and name not in candidates:
        candidates.append(name)
        votes[name] = 0
    return redirect(url_for("home"))

@app.post("/vote")
def cast_vote():
    candidate = request.form.get("candidate", "")
    if candidate in votes:
        votes[candidate] += 1
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
