import os
import pandas as pd
from flask import Flask, render_template_string

app = Flask(__name__)

# ------------------------------------------------------------------------------
# 1. Load Dataset (Cache locally in pandda folder for fast offline access)
# ------------------------------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "titanic.csv")
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

if os.path.exists(csv_path):
    print("Loading Titanic dataset from local cache...")
    titanic_df = pd.read_csv(csv_path)
else:
    print("Downloading Titanic dataset from URL...")
    titanic_df = pd.read_csv(url)
    titanic_df.to_csv(csv_path, index=False)
    print("Dataset saved to local file: titanic.csv")

# Print first few rows to console (maintains original file.py functionality)
print("\n--- Titanic Dataset Head ---")
print(titanic_df.head())
print("-----------------------------\n")

# ------------------------------------------------------------------------------
# 2. HTML & CSS Template with Interactive Table, Stats Cards & Search
# ------------------------------------------------------------------------------
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titanic Dataset Viewer | Pandas & Flask</title>
    <style>
        :root {
            --bg-color: #f1f5f9;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --border: #e2e8f0;
            --badge-survived-bg: #dcfce7;
            --badge-survived-text: #15803d;
            --badge-died-bg: #fee2e2;
            --badge-died-text: #b91c1c;
            --badge-class1-bg: #fef3c7;
            --badge-class1-text: #b45309;
            --badge-class2-bg: #e0e7ff;
            --badge-class2-text: #4338ca;
            --badge-class3-bg: #f3f4f6;
            --badge-class3-text: #4b5563;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            padding: 24px 32px;
            line-height: 1.5;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
            flex-wrap: wrap;
            gap: 16px;
        }

        .header-title h1 {
            font-size: 28px;
            font-weight: 800;
            color: #1e293b;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .header-title p {
            color: var(--text-muted);
            font-size: 14px;
            margin-top: 4px;
        }

        /* Stats Cards */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }

        .stat-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05), 0 1px 2px rgba(0,0,0,0.1);
            border: 1px solid var(--border);
            display: flex;
            flex-direction: column;
        }

        .stat-card .label {
            font-size: 13px;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .stat-card .value {
            font-size: 28px;
            font-weight: 700;
            color: var(--text-main);
            margin-top: 8px;
        }

        .stat-card .subtext {
            font-size: 12px;
            color: var(--text-muted);
            margin-top: 4px;
        }

        /* Controls Section */
        .controls-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 18px 24px;
            margin-bottom: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            border: 1px solid var(--border);
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            align-items: center;
            justify-content: space-between;
        }

        .search-box {
            flex: 1;
            min-width: 260px;
            position: relative;
        }

        .search-box input {
            width: 100%;
            padding: 10px 14px;
            border: 1px solid var(--border);
            border-radius: 8px;
            font-size: 14px;
            outline: none;
            transition: border-color 0.2s, box-shadow 0.2s;
        }

        .search-box input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
        }

        .filters {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .filters select {
            padding: 10px 14px;
            border: 1px solid var(--border);
            border-radius: 8px;
            font-size: 14px;
            background: #fff;
            color: var(--text-main);
            outline: none;
            cursor: pointer;
        }

        .filters select:focus {
            border-color: var(--primary);
        }

        /* Table Container */
        .table-card {
            background: var(--card-bg);
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -2px rgba(0,0,0,0.05);
            border: 1px solid var(--border);
            overflow: hidden;
        }

        .table-scroll {
            max-height: 560px;
            overflow-y: auto;
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13.5px;
            text-align: left;
        }

        thead {
            position: sticky;
            top: 0;
            background-color: #f8fafc;
            border-bottom: 2px solid var(--border);
            z-index: 10;
        }

        th {
            padding: 14px 16px;
            font-weight: 700;
            color: #475569;
            text-transform: uppercase;
            font-size: 11.5px;
            letter-spacing: 0.6px;
            white-space: nowrap;
        }

        td {
            padding: 12px 16px;
            border-bottom: 1px solid var(--border);
            white-space: nowrap;
            color: #334155;
        }

        tbody tr:hover {
            background-color: #f8fafc;
        }

        /* Badges */
        .badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            text-align: center;
        }

        .badge-survived {
            background-color: var(--badge-survived-bg);
            color: var(--badge-survived-text);
        }

        .badge-died {
            background-color: var(--badge-died-bg);
            color: var(--badge-died-text);
        }

        .badge-class1 {
            background-color: var(--badge-class1-bg);
            color: var(--badge-class1-text);
        }

        .badge-class2 {
            background-color: var(--badge-class2-bg);
            color: var(--badge-class2-text);
        }

        .badge-class3 {
            background-color: var(--badge-class3-bg);
            color: var(--badge-class3-text);
        }

        .footer-info {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 20px;
            border-top: 1px solid var(--border);
            background: #f8fafc;
            font-size: 13px;
            color: var(--text-muted);
        }
    </style>
</head>
<body>

    <!-- Header -->
    <div class="header">
        <div class="header-title">
            <h1>🚢 Titanic Dataset Explorer</h1>
            <p>Pandas DataFrame visualized with interactive HTML & CSS on Localhost</p>
        </div>
    </div>

    <!-- Summary KPI Cards -->
    <div class="stats-grid">
        <div class="stat-card">
            <span class="label">Total Passengers</span>
            <span class="value">{{ total_passengers }}</span>
            <span class="subtext">100% of dataset sample</span>
        </div>
        <div class="stat-card">
            <span class="label">Total Survived</span>
            <span class="value" style="color: #16a34a;">{{ survived_count }}</span>
            <span class="subtext">{{ survival_rate }}% Survival Rate</span>
        </div>
        <div class="stat-card">
            <span class="label">Average Age</span>
            <span class="value">{{ avg_age }} yrs</span>
            <span class="subtext">Min: {{ min_age }} | Max: {{ max_age }}</span>
        </div>
        <div class="stat-card">
            <span class="label">Average Ticket Fare</span>
            <span class="value">${{ avg_fare }}</span>
            <span class="subtext">Max Fare: ${{ max_fare }}</span>
        </div>
    </div>

    <!-- Controls (Search & Filters) -->
    <div class="controls-card">
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="🔍 Search passenger name, ticket, cabin..." onkeyup="filterTable()">
        </div>
        <div class="filters">
            <select id="survivedFilter" onchange="filterTable()">
                <option value="ALL">All Outcomes</option>
                <option value="1">🟢 Survived Only</option>
                <option value="0">🔴 Died Only</option>
            </select>
            <select id="classFilter" onchange="filterTable()">
                <option value="ALL">All Ticket Classes</option>
                <option value="1st Class">1st Class (Upper)</option>
                <option value="2nd Class">2nd Class (Middle)</option>
                <option value="3rd Class">3rd Class (Lower)</option>
            </select>
            <select id="genderFilter" onchange="filterTable()">
                <option value="ALL">All Genders</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
            </select>
        </div>
    </div>

    <!-- Data Table Card -->
    <div class="table-card">
        <div class="table-scroll">
            <table id="dataTable">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Status</th>
                        <th>Class</th>
                        <th>Passenger Name</th>
                        <th>Sex</th>
                        <th>Age</th>
                        <th>SibSp</th>
                        <th>Parch</th>
                        <th>Ticket</th>
                        <th>Fare ($)</th>
                        <th>Cabin</th>
                        <th>Embarked</th>
                    </tr>
                </thead>
                <tbody id="tableBody">
                    {% for row in rows %}
                    <tr data-survived="{{ row.Survived }}" data-pclass="{{ row.Pclass_Label }}" data-gender="{{ row.Sex }}">
                        <td><strong>{{ row.PassengerId }}</strong></td>
                        <td>
                            {% if row.Survived == 1 %}
                                <span class="badge badge-survived">🟢 Survived</span>
                            {% else %}
                                <span class="badge badge-died">🔴 Died</span>
                            {% endif %}
                        </td>
                        <td>
                            {% if row.Pclass == 1 %}
                                <span class="badge badge-class1">⭐ 1st Class</span>
                            {% elif row.Pclass == 2 %}
                                <span class="badge badge-class2">🥈 2nd Class</span>
                            {% else %}
                                <span class="badge badge-class3">🥉 3rd Class</span>
                            {% endif %}
                        </td>
                        <td>{{ row.Name }}</td>
                        <td style="text-transform: capitalize;">{{ row.Sex }}</td>
                        <td>{{ row.Age if row.Age != "nan" else "-" }}</td>
                        <td>{{ row.SibSp }}</td>
                        <td>{{ row.Parch }}</td>
                        <td><code>{{ row.Ticket }}</code></td>
                        <td>${{ "%.2f"|format(row.Fare) }}</td>
                        <td>{{ row.Cabin if row.Cabin != "nan" else "-" }}</td>
                        <td>{{ row.Embarked if row.Embarked != "nan" else "-" }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        <div class="footer-info">
            <span id="rowCount">Showing {{ total_passengers }} passengers</span>
            <span>Dataset: <code>datasciencedojo/titanic.csv</code></span>
        </div>
    </div>

    <!-- Client-side Interactive Filter Script -->
    <script>
        function filterTable() {
            const query = document.getElementById('searchInput').value.toLowerCase();
            const survivedFilter = document.getElementById('survivedFilter').value;
            const classFilter = document.getElementById('classFilter').value;
            const genderFilter = document.getElementById('genderFilter').value;

            const rows = document.querySelectorAll('#tableBody tr');
            let visibleCount = 0;

            rows.forEach(row => {
                const text = row.innerText.toLowerCase();
                const survived = row.getAttribute('data-survived');
                const pclass = row.getAttribute('data-pclass');
                const gender = row.getAttribute('data-gender');

                const matchesSearch = text.includes(query);
                const matchesSurvived = (survivedFilter === 'ALL' || survived === survivedFilter);
                const matchesClass = (classFilter === 'ALL' || pclass === classFilter);
                const matchesGender = (genderFilter === 'ALL' || gender === genderFilter);

                if (matchesSearch && matchesSurvived && matchesClass && matchesGender) {
                    row.style.display = '';
                    visibleCount++;
                } else {
                    row.style.display = 'none';
                }
            });

            document.getElementById('rowCount').innerText = `Showing ${visibleCount} of {{ total_passengers }} passengers`;
        }
    </script>
</body>
</html>
"""

# ------------------------------------------------------------------------------
# 3. Flask Route
# ------------------------------------------------------------------------------
@app.route("/")
def index():
    # Calculate Summary Statistics
    total_passengers = len(titanic_df)
    survived_count = int(titanic_df["Survived"].sum())
    survival_rate = round((survived_count / total_passengers) * 100, 2)
    avg_age = round(titanic_df["Age"].mean(), 1)
    min_age = round(titanic_df["Age"].min(), 1)
    max_age = round(titanic_df["Age"].max(), 1)
    avg_fare = round(titanic_df["Fare"].mean(), 2)
    max_fare = round(titanic_df["Fare"].max(), 2)

    # Prepare rows dictionary for clean rendering
    df_copy = titanic_df.copy()
    pclass_map = {1: "1st Class", 2: "2nd Class", 3: "3rd Class"}
    df_copy["Pclass_Label"] = df_copy["Pclass"].map(pclass_map)
    df_copy = df_copy.astype(str)

    rows = df_copy.to_dict(orient="records")
    for r in rows:
        r["Survived"] = int(float(r["Survived"]))
        r["Pclass"] = int(float(r["Pclass"]))
        r["Fare"] = float(r["Fare"])

    return render_template_string(
        HTML_TEMPLATE,
        total_passengers=total_passengers,
        survived_count=survived_count,
        survival_rate=survival_rate,
        avg_age=avg_age,
        min_age=min_age,
        max_age=max_age,
        avg_fare=avg_fare,
        max_fare=max_fare,
        rows=rows,
    )

# ------------------------------------------------------------------------------
# 4. Run Application on Localhost
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Starting Flask web server on http://127.0.0.1:5000 ...")
    app.run(host="127.0.0.1", port=5000, debug=False)

print("-----------------------------\n")

# ------------------------------------------------------------------------------
# 2. HTML & CSS Template with Interactive Table, Stats Cards & Search
# ------------------------------------------------------------------------------
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titanic Dataset Viewer | Pandas & Flask</title>
    <style>
        :root {
            --bg-color: #f1f5f9;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --border: #e2e8f0;
            --badge-survived-bg: #dcfce7;
            --badge-survived-text: #15803d;
            --badge-died-bg: #fee2e2;
            --badge-died-text: #b91c1c;
            --badge-class1-bg: #fef3c7;
            --badge-class1-text: #b45309;
            --badge-class2-bg: #e0e7ff;
            --badge-class2-text: #4338ca;
            --badge-class3-bg: #f3f4f6;
            --badge-class3-text: #4b5563;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            padding: 24px 32px;
            line-height: 1.5;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
            flex-wrap: wrap;
            gap: 16px;
        }

        .header-title h1 {
            font-size: 28px;
            font-weight: 800;
            color: #1e293b;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .header-title p {
            color: var(--text-muted);
            font-size: 14px;
            margin-top: 4px;
        }

        /* Stats Cards */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }

        .stat-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05), 0 1px 2px rgba(0,0,0,0.1);
            border: 1px solid var(--border);
            display: flex;
            flex-direction: column;
        }

        .stat-card .label {
            font-size: 13px;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .stat-card .value {
            font-size: 28px;
            font-weight: 700;
            color: var(--text-main);
            margin-top: 8px;
        }

        .stat-card .subtext {
            font-size: 12px;
            color: var(--text-muted);
            margin-top: 4px;
        }

        /* Controls Section */
        .controls-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 18px 24px;
            margin-bottom: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            border: 1px solid var(--border);
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            align-items: center;
            justify-content: space-between;
        }

        .search-box {
            flex: 1;
            min-width: 260px;
            position: relative;
        }

        .search-box input {
            width: 100%;
            padding: 10px 14px;
            border: 1px solid var(--border);
            border-radius: 8px;
            font-size: 14px;
            outline: none;
            transition: border-color 0.2s, box-shadow 0.2s;
        }

        .search-box input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
        }

        .filters {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }

        .filters select {
            padding: 10px 14px;
            border: 1px solid var(--border);
            border-radius: 8px;
            font-size: 14px;
            background: #fff;
            color: var(--text-main);
            outline: none;
            cursor: pointer;
        }

        .filters select:focus {
            border-color: var(--primary);
        }

        /* Table Container */
        .table-card {
            background: var(--card-bg);
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -2px rgba(0,0,0,0.05);
            border: 1px solid var(--border);
            overflow: hidden;
        }

        .table-scroll {
            max-height: 560px;
            overflow-y: auto;
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13.5px;
            text-align: left;
        }

        thead {
            position: sticky;
            top: 0;
            background-color: #f8fafc;
            border-bottom: 2px solid var(--border);
            z-index: 10;
        }

        th {
            padding: 14px 16px;
            font-weight: 700;
            color: #475569;
            text-transform: uppercase;
            font-size: 11.5px;
            letter-spacing: 0.6px;
            white-space: nowrap;
        }

        td {
            padding: 12px 16px;
            border-bottom: 1px solid var(--border);
            white-space: nowrap;
            color: #334155;
        }

        tbody tr:hover {
            background-color: #f8fafc;
        }

        /* Badges */
        .badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            text-align: center;
        }

        .badge-survived {
            background-color: var(--badge-survived-bg);
            color: var(--badge-survived-text);
        }

        .badge-died {
            background-color: var(--badge-died-bg);
            color: var(--badge-died-text);
        }

        .badge-class1 {
            background-color: var(--badge-class1-bg);
            color: var(--badge-class1-text);
        }

        .badge-class2 {
            background-color: var(--badge-class2-bg);
            color: var(--badge-class2-text);
        }

        .badge-class3 {
            background-color: var(--badge-class3-bg);
            color: var(--badge-class3-text);
        }

        .footer-info {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 20px;
            border-top: 1px solid var(--border);
            background: #f8fafc;
            font-size: 13px;
            color: var(--text-muted);
        }
    </style>
</head>
<body>

    <!-- Header -->
    <div class="header">
        <div class="header-title">
            <h1>🚢 Titanic Dataset Explorer</h1>
            <p>Pandas DataFrame visualized with interactive HTML & CSS on Localhost</p>
        </div>
    </div>

    <!-- Summary KPI Cards -->
    <div class="stats-grid">
        <div class="stat-card">
            <span class="label">Total Passengers</span>
            <span class="value">{{ total_passengers }}</span>
            <span class="subtext">100% of dataset sample</span>
        </div>
        <div class="stat-card">
            <span class="label">Total Survived</span>
            <span class="value" style="color: #16a34a;">{{ survived_count }}</span>
            <span class="subtext">{{ survival_rate }}% Survival Rate</span>
        </div>
        <div class="stat-card">
            <span class="label">Average Age</span>
            <span class="value">{{ avg_age }} yrs</span>
            <span class="subtext">Min: {{ min_age }} | Max: {{ max_age }}</span>
        </div>
        <div class="stat-card">
            <span class="label">Average Ticket Fare</span>
            <span class="value">${{ avg_fare }}</span>
            <span class="subtext">Max Fare: ${{ max_fare }}</span>
        </div>
    </div>

    <!-- Controls (Search & Filters) -->
    <div class="controls-card">
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="🔍 Search passenger name, ticket, cabin..." onkeyup="filterTable()">
        </div>
        <div class="filters">
            <select id="survivedFilter" onchange="filterTable()">
                <option value="ALL">All Outcomes</option>
                <option value="1">🟢 Survived Only</option>
                <option value="0">🔴 Died Only</option>
            </select>
            <select id="classFilter" onchange="filterTable()">
                <option value="ALL">All Ticket Classes</option>
                <option value="1st Class">1st Class (Upper)</option>
                <option value="2nd Class">2nd Class (Middle)</option>
                <option value="3rd Class">3rd Class (Lower)</option>
            </select>
            <select id="genderFilter" onchange="filterTable()">
                <option value="ALL">All Genders</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
            </select>
        </div>
    </div>

    <!-- Data Table Card -->
    <div class="table-card">
        <div class="table-scroll">
            <table id="dataTable">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Status</th>
                        <th>Class</th>
                        <th>Passenger Name</th>
                        <th>Sex</th>
                        <th>Age</th>
                        <th>SibSp</th>
                        <th>Parch</th>
                        <th>Ticket</th>
                        <th>Fare ($)</th>
                        <th>Cabin</th>
                        <th>Embarked</th>
                    </tr>
                </thead>
                <tbody id="tableBody">
                    {% for row in rows %}
                    <tr data-survived="{{ row.Survived }}" data-pclass="{{ row.Pclass_Label }}" data-gender="{{ row.Sex }}">
                        <td><strong>{{ row.PassengerId }}</strong></td>
                        <td>
                            {% if row.Survived == 1 %}
                                <span class="badge badge-survived">🟢 Survived</span>
                            {% else %}
                                <span class="badge badge-died">🔴 Died</span>
                            {% endif %}
                        </td>
                        <td>
                            {% if row.Pclass == 1 %}
                                <span class="badge badge-class1">⭐ 1st Class</span>
                            {% elif row.Pclass == 2 %}
                                <span class="badge badge-class2">🥈 2nd Class</span>
                            {% else %}
                                <span class="badge badge-class3">🥉 3rd Class</span>
                            {% endif %}
                        </td>
                        <td>{{ row.Name }}</td>
                        <td style="text-transform: capitalize;">{{ row.Sex }}</td>
                        <td>{{ row.Age if row.Age != "nan" else "-" }}</td>
                        <td>{{ row.SibSp }}</td>
                        <td>{{ row.Parch }}</td>
                        <td><code>{{ row.Ticket }}</code></td>
                        <td>${{ "%.2f"|format(row.Fare) }}</td>
                        <td>{{ row.Cabin if row.Cabin != "nan" else "-" }}</td>
                        <td>{{ row.Embarked if row.Embarked != "nan" else "-" }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        <div class="footer-info">
            <span id="rowCount">Showing {{ total_passengers }} passengers</span>
            <span>Dataset: <code>datasciencedojo/titanic.csv</code></span>
        </div>
    </div>

    <!-- Client-side Interactive Filter Script -->
    <script>
        function filterTable() {
            const query = document.getElementById('searchInput').value.toLowerCase();
            const survivedFilter = document.getElementById('survivedFilter').value;
            const classFilter = document.getElementById('classFilter').value;
            const genderFilter = document.getElementById('genderFilter').value;

            const rows = document.querySelectorAll('#tableBody tr');
            let visibleCount = 0;

            rows.forEach(row => {
                const text = row.innerText.toLowerCase();
                const survived = row.getAttribute('data-survived');
                const pclass = row.getAttribute('data-pclass');
                const gender = row.getAttribute('data-gender');

                const matchesSearch = text.includes(query);
                const matchesSurvived = (survivedFilter === 'ALL' || survived === survivedFilter);
                const matchesClass = (classFilter === 'ALL' || pclass === classFilter);
                const matchesGender = (genderFilter === 'ALL' || gender === genderFilter);

                if (matchesSearch && matchesSurvived && matchesClass && matchesGender) {
                    row.style.display = '';
                    visibleCount++;
                } else {
                    row.style.display = 'none';
                }
            });

            document.getElementById('rowCount').innerText = `Showing ${visibleCount} of {{ total_passengers }} passengers`;
        }
    </script>
</body>
</html>
"""

# ------------------------------------------------------------------------------
# 3. Flask Route
# ------------------------------------------------------------------------------
@app.route("/")
def index():
    # Calculate Summary Statistics
    total_passengers = len(titanic_df)
    survived_count = int(titanic_df["Survived"].sum())
    survival_rate = round((survived_count / total_passengers) * 100, 2)
    avg_age = round(titanic_df["Age"].mean(), 1)
    min_age = round(titanic_df["Age"].min(), 1)
    max_age = round(titanic_df["Age"].max(), 1)
    avg_fare = round(titanic_df["Fare"].mean(), 2)
    max_fare = round(titanic_df["Fare"].max(), 2)

    # Prepare rows dictionary for clean rendering
    df_copy = titanic_df.copy()
    pclass_map = {1: "1st Class", 2: "2nd Class", 3: "3rd Class"}
    df_copy["Pclass_Label"] = df_copy["Pclass"].map(pclass_map)
    df_copy = df_copy.astype(str)

    rows = df_copy.to_dict(orient="records")
    for r in rows:
        r["Survived"] = int(float(r["Survived"]))
        r["Pclass"] = int(float(r["Pclass"]))
        r["Fare"] = float(r["Fare"])

    return render_template_string(
        HTML_TEMPLATE,
        total_passengers=total_passengers,
        survived_count=survived_count,
        survival_rate=survival_rate,
        avg_age=avg_age,
        min_age=min_age,
        max_age=max_age,
        avg_fare=avg_fare,
        max_fare=max_fare,
        rows=rows,
    )

# ------------------------------------------------------------------------------
# 4. Run Application on Localhost
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Starting Flask web server on http://127.0.0.1:5000 ...")
    app.run(host="127.0.0.1", port=5000, debug=False)