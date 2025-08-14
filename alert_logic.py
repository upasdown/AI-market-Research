def check_kpis():
    # Demo KPI values (simulate from Google Ads)
    kpi_data = {
        "CPC": 2.5,
        "ConversionRate": 2.8,
        "DailySpend": 92
    }

    alerts = []

    if kpi_data["CPC"] > 2:
        alerts.append("CPC ist über 2 €")

    if kpi_data["ConversionRate"] < 3:
        alerts.append("Conversion Rate ist unter 3 %")

    if kpi_data["DailySpend"] > 90:
        alerts.append("Tagesbudget ist über 90 % aufgebraucht")

    return alerts, kpi_data
