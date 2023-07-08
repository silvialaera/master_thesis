import sqlite3
import csv

try:
    sqliteConnection = sqlite3.connect('TEMOA_Italy.sqlite')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    # import csv resulting from taxonomy application
    inFile = csv.reader(open("tech_year_taxonomy.csv", "r"))
    taxonomy_rows = []
    for row in inFile:
        if len(row) > 0:
            taxonomy_rows.append(row)

    taxonomy_map = dict()
    for elem in taxonomy_rows:
        tech = elem[0]
        year = elem[1]
        delta = elem[2]
        key = str(tech) + "-" + str(year)
        value = delta
        if key not in taxonomy_map.keys():
            taxonomy_map.update({key: value})

# filter: delete all techs not being present in CostInvest table
    query = "SELECT tech, vintage FROM CostInvest ORDER by tech"
    cursor.execute(query)
    invest_tuples = cursor.fetchall()

    invest_rows = []
    for row in invest_tuples:
        invest_rows.append(list(row))

    # invest map
    cost_invest_map = dict()
    for elem in invest_rows:
        tech = elem[0]
        year = elem[1]
        key = str(tech) + "-" + str(year)
        if key not in cost_invest_map.keys():
            cost_invest_map.update({key: 0.0})

