from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

BASE = Path(__file__).resolve().parent
DB = BASE / "instance" / "support.db"

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

def db():
    DB.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = db()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        severity TEXT NOT NULL,
        status TEXT NOT NULL,
        owner TEXT NOT NULL,
        customer TEXT NOT NULL,
        created_at TEXT NOT NULL,
        sla_hours INTEGER NOT NULL,
        rca TEXT DEFAULT '',
        resolution TEXT DEFAULT ''
    );

    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        owner TEXT NOT NULL,
        status TEXT NOT NULL,
        progress INTEGER NOT NULL,
        risk TEXT NOT NULL,
        due_date TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL,
        owner TEXT NOT NULL,
        type TEXT NOT NULL,
        status TEXT NOT NULL,
        due_date TEXT NOT NULL
    );
    """)
    if conn.execute("SELECT COUNT(*) FROM incidents").fetchone()[0] == 0:
        now = datetime.now()
        incidents = [
            ("API authentication timeout", "High", "Open", "Support Team", "PSU Bank", now.isoformat(), 4, "", ""),
            ("Certificate renewal warning", "Medium", "In Progress", "Infra Team", "PSU Bank", (now-timedelta(hours=5)).isoformat(), 8, "Certificate nearing expiry; renewal scheduled.", ""),
            ("Database connection alert", "Critical", "Resolved", "DB Team", "PSU Bank", (now-timedelta(days=1)).isoformat(), 2, "Connection pool exhaustion caused intermittent failures.", "Pool size increased and service restarted.")
        ]
        conn.executemany("INSERT INTO incidents(title,severity,status,owner,customer,created_at,sla_hours,rca,resolution) VALUES(?,?,?,?,?,?,?,?,?)", incidents)
        projects = [
            ("CryptoBind Department Onboarding", "Customer Engineering", "In Progress", 72, "Medium", "2026-09-15"),
            ("Production Certificate Renewal", "Infrastructure", "On Track", 85, "Low", "2026-09-05"),
            ("Support SOP Modernization", "Customer Success", "At Risk", 48, "High", "2026-09-10"),
        ]
        conn.executemany("INSERT INTO projects(name,owner,status,progress,risk,due_date) VALUES(?,?,?,?,?,?)", projects)
        activities = [
            ("Prepare weekly production report", "Program Coordinator", "Report", "Open", "2026-08-28"),
            ("Approve certificate change window", "Change Manager", "Change", "Pending", "2026-08-29"),
            ("Complete RCA for database incident", "DB Team", "RCA", "Closed", "2026-08-26"),
            ("Review onboarding dependencies", "Customer Engineering", "Dependency", "Open", "2026-09-01"),
        ]
        conn.executemany("INSERT INTO activities(item,owner,type,status,due_date) VALUES(?,?,?,?,?)", activities)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/health")
def health():
    return jsonify({"status":"UP","service":"JISA Enterprise Support Platform","timestamp":datetime.now().isoformat()})

@app.route("/api/incidents", methods=["GET","POST"])
def incidents():
    conn = db()
    if request.method == "POST":
        data = request.get_json() or {}
        required = ["title","severity","owner","customer"]
        if any(not data.get(k) for k in required):
            return jsonify({"error":"title, severity, owner and customer are required"}), 400
        conn.execute("""INSERT INTO incidents(title,severity,status,owner,customer,created_at,sla_hours,rca,resolution)
                        VALUES(?,?,?,?,?,?,?,?,?)""",
                     (data["title"], data["severity"], "Open", data["owner"], data["customer"],
                      datetime.now().isoformat(), int(data.get("sla_hours", 8)), "", ""))
        conn.commit()
        conn.close()
        return jsonify({"message":"Incident created"}), 201
    rows = [dict(x) for x in conn.execute("SELECT * FROM incidents ORDER BY id DESC")]
    conn.close()
    return jsonify(rows)

@app.route("/api/projects")
def projects():
    conn = db()
    rows = [dict(x) for x in conn.execute("SELECT * FROM projects ORDER BY id")]
    conn.close()
    return jsonify(rows)

@app.route("/api/activities")
def activities():
    conn = db()
    rows = [dict(x) for x in conn.execute("SELECT * FROM activities ORDER BY id DESC")]
    conn.close()
    return jsonify(rows)

@app.route("/api/metrics")
def metrics():
    conn = db()
    total = conn.execute("SELECT COUNT(*) FROM incidents").fetchone()[0]
    open_count = conn.execute("SELECT COUNT(*) FROM incidents WHERE status NOT IN ('Resolved','Closed')").fetchone()[0]
    critical = conn.execute("SELECT COUNT(*) FROM incidents WHERE severity='Critical' AND status NOT IN ('Resolved','Closed')").fetchone()[0]
    projects = conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0]
    at_risk = conn.execute("SELECT COUNT(*) FROM projects WHERE risk='High' OR status='At Risk'").fetchone()[0]
    conn.close()
    return jsonify({"incidents":total,"open_incidents":open_count,"critical_open":critical,
                    "projects":projects,"at_risk_projects":at_risk})

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
