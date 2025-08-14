from flask import Flask, render_template
from alert_logic import check_kpis

app = Flask(__name__)

@app.route("/")
def dashboard():
    alerts, kpi_data = check_kpis()
    return render_template("dashboard.html", alerts=alerts, kpi_data=kpi_data)

if __name__ == "__main__":
    app.run(debug=True)
