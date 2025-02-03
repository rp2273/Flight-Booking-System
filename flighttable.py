import mysql.connector
class DBHelper:
    def __init__(self):
        self.con = mysql.connector.connect(host= 'localhost', user= 'root', password="123456789", database = 'jetairways')
        query = "Create table if not exists flight(Fl_id varChar(20) primary key, Fl_name varChar(200), departure varChar(300), arrival varChar(300), source varChar(100), destination varChar(100), price_of_seat_economy_Rs int(50), no_of_available_seats_150 int(30))"
        query1 = "Create table if not exists passenger(p_no int(30) NOT NULL, p_id varChar(20) primary key, p_name varChar(200), Fl_id varChar(20) REFERENCES flight(Fl_id), p_phn varChar(50))"
        cur = self.con.cursor()
        cur.execute(query)
        cur.execute(query1)
        print("Created")
    def insert_flight(self, Fl_id, Fl_name, departure, arrival, source, destination, price_of_seat_economy_Rs, no_of_available_seats_150):
        query = """insert into flight (Fl_id, Fl_name, departure, arrival, source, destination, price_of_seat_economy_Rs, no_of_available_seats_150)values("{}","{}", "{}", "{}","{}","{}", {}, {})""".format(Fl_id, Fl_name, departure, arrival, source, destination, price_of_seat_economy_Rs, no_of_available_seats_150)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Flight saved to DB")
    def insert_passenger(self, p_no, p_id, p_name, Fl_id, p_phn):
        query = """insert into passenger (p_no, p_id, p_name, Fl_id, p_phn)
        values({},"{}", "{}", "{}", "{}")""".format(p_no, p_id, p_name, Fl_id, p_phn)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Passenger saved to DB")


helper = DBHelper()
helper.insert_flight("TK1484", "Turkish Airlines", "10-02-2022/10:50:00", "10-02-2022/18:00:00", "Mumbai","Istanbul", 27957, 56)
helper.insert_flight("MV1122", "Maldives Airlines", "10-02-2022/11:25:00", "10-02-2022/15:59:00", "Delhi","Male", 9478, 121)
helper.insert_flight("JP2823", "Tokyo Airlines", "10-02-2022/11:30:00", "10-02-2022/22:20:00", "Chennai","Tokyo", 29747, 139)
helper.insert_flight("CA3245", "Canada Airlines", "10-02-2022/12:30:00", "11-02-2022/05:15:00", "Kolkata","Toronto", 56069, 75)
helper.insert_flight("SG5685", "Singa Airlines", "10-02-2022/14:25:00", "10-02-2022/19:00:00", "Bangalore","Singapore", 12324, 43)
helper.insert_flight("AN2422", "AndNico Airlines", "10-02-2022/16:10:00", "11-02-2022/10:45:00", "Ranchi","Port Blair", 6859, 10)
helper.insert_flight("FC9756", "French Airlines", "10-02-2022/17:40:00", "11-02-2022/22:45:00", "Guwahati","Paris", 27161, 28)
helper.insert_flight("GM7685", "German Airlines", "10-02-2022/18:00:00", "11-02-2022/07:15:00", "Hyderabad","Berlin", 59904, 15)


helper.insert_passenger(1, "3245001", "Shiwani Jain", "CA3245", "9845208903")
helper.insert_passenger(2, "7685002", "Harry Styles", "GM7685", "8547301206")
helper.insert_passenger(3, "2422003", "Sriparna Banerjee", "AN2422", "9957123902")
helper.insert_passenger(4, "1122004", "Sarah J. Topno", "MV1122", "7469200315")
helper.insert_passenger(5, "9756005", "Mahima Singhvi", "FC9756", "9465017223")
helper.insert_passenger(6, "1484006", "Arijit Singh", "TK1484", "8579621001")
helper.insert_passenger(7, "2823007", "Shawn Mendes", "JP2823", "8269301746")
helper.insert_passenger(8, "5685008", "Risa Pandey", "SG5685", "9222158023")
