import mysql.connector

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='indigo'
            )

            if self.conn.is_connected():
                self.mycursor = self.conn.cursor()
                print("DB class → Connection Established")
            else:
                print("DB class → Connection Failed")
                self.mycursor = None

        except mysql.connector.Error as e:
            print("DB class → Connection Error:", e)
            self.mycursor = None

    def fetch_city_names(self):
        if not self.mycursor:
            print("No database cursor available.")
            return []

        # Fetch distinct cities from both source and destination columns
        self.mycursor.execute("""
            SELECT DISTINCT(destination) FROM flights
            UNION
            SELECT DISTINCT(source) FROM flights
        """)

        data = self.mycursor.fetchall()
        city = [item[0] for item in data]
        return city

    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
        SELECT Airline,Route,Dep_Time,Duration,Price FROM flights
        WHERE Source = '{}' AND Destination = '{}'""".format(source,destination))

        data = self.mycursor.fetchall()

        return data

    def fetch_airline_data(self):
        airline = []
        frequency = []

        self.mycursor.execute("""
        SELECT Airline,COUNT(*) FROM flights
        GROUP BY Airline""")

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency

    def busy_airport(self):
        city = []
        frequency1 = []

        self.mycursor.execute("""
        SELECT Source,COUNT(*) FROM (SELECT Source FROM flights 
                            UNION ALL 
                            SELECT Destination FROM flights) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC""")

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency1.append(item[1])

        return city,frequency1
