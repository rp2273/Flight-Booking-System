import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry  # for date picker
import mysql.connector
from PIL import Image, ImageTk

class DBHelper:
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost', user='root', password='123456789', database='jetairways')
        self.create_tables()

    def create_tables(self):
        query_flight = """
        CREATE TABLE IF NOT EXISTS flight (
            Fl_id VARCHAR(20) PRIMARY KEY,
            Fl_name VARCHAR(200),
            departure DATE,
            arrival DATE,
            source VARCHAR(100),
            destination VARCHAR(100),
            price_of_seat_economy_Rs INT(50),
            no_of_available_seats_150 INT(30)
        )
        """
        query_passenger = """
        CREATE TABLE IF NOT EXISTS passenger (
            p_no INT(30) NOT NULL AUTO_INCREMENT,
            p_id VARCHAR(20) PRIMARY KEY,
            p_name VARCHAR(200),
            Fl_id VARCHAR(20),
            p_phn VARCHAR(50),
            FOREIGN KEY (Fl_id) REFERENCES flight (Fl_id)
        )
        """
        with self.con.cursor() as cur:
            cur.execute(query_flight)
            cur.execute(query_passenger)
        self.con.commit()

    def insert_flight(self, Fl_id, Fl_name, departure, arrival, source, destination, price_of_seat_economy_Rs, no_of_available_seats_150):
        query = """
        INSERT INTO flight (
            Fl_id, Fl_name, departure, arrival, source, destination, price_of_seat_economy_Rs, no_of_available_seats_150
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (Fl_id, Fl_name, departure, arrival, source, destination, price_of_seat_economy_Rs, no_of_available_seats_150)
        with self.con.cursor() as cur:
            cur.execute(query, data)
        self.con.commit()
        messagebox.showinfo("Success", "Flight saved to DB")

    def insert_passenger(self, p_id, p_name, Fl_id, p_phn):
        query = """
        INSERT INTO passenger (p_id, p_name, Fl_id, p_phn) VALUES (%s, %s, %s, %s)
        """
        data = (p_id, p_name, Fl_id, p_phn)
        with self.con.cursor() as cur:
            cur.execute(query, data)
        self.con.commit()
        messagebox.showinfo("Success", "Passenger saved to DB")

    def get_flight_details(self):
        query = "SELECT Fl_id, Fl_name, departure, arrival, source, destination, price_of_seat_economy_Rs, no_of_available_seats_150 FROM flight"
        with self.con.cursor() as cur:
            cur.execute(query)
            flight_details = cur.fetchall()
        return flight_details

    def get_passenger_details(self):
        query = "SELECT p_no, p_id, p_name, Fl_id, p_phn FROM passenger"
        with self.con.cursor() as cur:
            cur.execute(query)
            passenger_details = cur.fetchall()
        return passenger_details

class WelcomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome to Jet Airways")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        background_image = Image.open("D:/ROSHNI/SRM/2nd yr/4th srm/DBMS/project/Risa/travel.PNG")
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Label(self, text="Welcome to Jet Airways", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333333").pack(pady=(20, 10))

        button_style = {"font": ("Helvetica", 14), "bg": "#007bff", "fg": "white", "width": 15, "height": 2}

        enter_btn = tk.Button(self, text="Enter", command=self.enter_app, **button_style)
        enter_btn.pack(pady=10)

    def enter_app(self):
        self.withdraw()
        db_helper = DBHelper()
        app = GUI(db_helper)
        app.mainloop()

class GUI(tk.Tk):
    def __init__(self, db_helper):
        super().__init__()
        self.db_helper = db_helper
        self.title("Flight Management System")

        self.create_widgets()

    def create_widgets(self):
        background_image = Image.open("D:/ROSHNI/SRM/2nd yr/4th srm/DBMS/project/Risa/flight.PNG")
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=background_photo)
        background_label.image = background_photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.configure(bg="#f0f0f0")

        tk.Label(self, text="Welcome to Jet Airways", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333333").grid(row=0, column=0, columnspan=4, pady=(20, 10))

        tk.Label(self, text="").grid(row=1, column=0)
        tk.Label(self, text="").grid(row=2, column=0)
        tk.Label(self, text="").grid(row=3, column=0)

        button_style = {"font": ("Helvetica", 14), "bg": "#007bff", "fg": "white", "width": 15, "height": 2}

        insert_flight_btn = tk.Button(self, text="Insert Flight", command=self.show_insert_flight, **button_style)
        insert_flight_btn.grid(row=4, column=0, pady=10, padx=20)
        tk.Label(self, text="Add a new flight", font=("Helvetica", 10)).grid(row=4, column=1, pady=10)

        insert_passenger_btn = tk.Button(self, text="Insert Passenger", command=self.show_insert_passenger, **button_style)
        insert_passenger_btn.grid(row=5, column=0, pady=10, padx=20)
        tk.Label(self, text="Add a new passenger", font=("Helvetica", 10)).grid(row=5, column=1, pady=10)

        view_flight_btn = tk.Button(self, text="View Flight Details", command=self.view_flight_details, **button_style)
        view_flight_btn.grid(row=6, column=0, pady=10, padx=20)
        tk.Label(self, text="View all flight details", font=("Helvetica", 10)).grid(row=6, column=1, pady=10)

        view_passenger_btn = tk.Button(self, text="View Passenger Details", command=self.view_passenger_details, **button_style)
        view_passenger_btn.grid(row=7, column=0, pady=10, padx=20)
        tk.Label(self, text="View all passenger details", font=("Helvetica", 10)).grid(row=7, column=1, pady=10)

        tk.Label(self, text="").grid(row=8, column=0)
        tk.Label(self, text="").grid(row=9, column=0)

    def show_insert_flight(self):
        InsertFlightWindow(self, self.db_helper)

    def show_insert_passenger(self):
        InsertPassengerWindow(self, self.db_helper)

    def view_flight_details(self):
        ViewDetailsWindow(self, self.db_helper, "flight")

    def view_passenger_details(self):
        ViewDetailsWindow(self, self.db_helper, "passenger")

class ViewDetailsWindow(tk.Toplevel):
    def __init__(self, master, db_helper, details_type):
        super().__init__(master)
        self.title(f"View {details_type.capitalize()} Details")
        self.geometry("400x300")

        self.db_helper = db_helper
        self.details_type = details_type
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=f"{self.details_type.capitalize()} Details", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=10)

        self.details_text = tk.Text(self, height=10, width=40)
        self.details_text.grid(row=1, column=0, columnspan=2, pady=10)

        if self.details_type == "flight":
            details = self.db_helper.get_flight_details()
        elif self.details_type == "passenger":
            details = self.db_helper.get_passenger_details()
        else:
            details = []

        for detail in details:
            self.details_text.insert(tk.END, detail)
            self.details_text.insert(tk.END, "\n\n")

class InsertFlightWindow(tk.Toplevel):
    def __init__(self, master, db_helper):
        super().__init__(master)
        self.title("Insert Flight")
        self.geometry("400x350")

        self.db_helper = db_helper
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Flight Details", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self, text="Flight ID:", font=("Helvetica", 12)).grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.fl_id_entry = tk.Entry(self)
        self.fl_id_entry.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(self, text="Flight Name:", font=("Helvetica", 12)).grid(row=2, column=0, pady=5, padx=5, sticky="e")
        self.fl_name_entry = tk.Entry(self)
        self.fl_name_entry.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(self, text="Departure:", font=("Helvetica", 12)).grid(row=3, column=0, pady=5, padx=5, sticky="e")
        self.departure_entry = DateEntry(self)
        self.departure_entry.grid(row=3, column=1, pady=5, padx=5)

        tk.Label(self, text="Arrival:", font=("Helvetica", 12)).grid(row=4, column=0, pady=5, padx=5, sticky="e")
        self.arrival_entry = DateEntry(self)
        self.arrival_entry.grid(row=4, column=1, pady=5, padx=5)

        tk.Label(self, text="Source:", font=("Helvetica", 12)).grid(row=5, column=0, pady=5, padx=5, sticky="e")
        self.source_entry = tk.Entry(self)
        self.source_entry.grid(row=5, column=1, pady=5, padx=5)

        tk.Label(self, text="Destination:", font=("Helvetica", 12)).grid(row=6, column=0, pady=5, padx=5, sticky="e")
        self.destination_entry = tk.Entry(self)
        self.destination_entry.grid(row=6, column=1, pady=5, padx=5)

        tk.Label(self, text="Price of Seat (Rs):", font=("Helvetica", 12)).grid(row=7, column=0, pady=5, padx=5, sticky="e")
        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=7, column=1, pady=5, padx=5)

        tk.Label(self, text="Available Seats:", font=("Helvetica", 12)).grid(row=8, column=0, pady=5, padx=5, sticky="e")
        self.seats_entry = tk.Entry(self)
        self.seats_entry.grid(row=8, column=1, pady=5, padx=5)

        tk.Button(self, text="Save", command=self.save_flight, font=("Helvetica", 12), bg="#007bff", fg="white", width=10).grid(row=9, column=0, columnspan=2, pady=10)

    def save_flight(self):
        fl_id = self.fl_id_entry.get()
        fl_name = self.fl_name_entry.get()
        departure = self.departure_entry.get()
        arrival = self.arrival_entry.get()
        source = self.source_entry.get()
        destination = self.destination_entry.get()
        price = int(self.price_entry.get())
        seats = int(self.seats_entry.get())

        self.db_helper.insert_flight(fl_id, fl_name, departure, arrival, source, destination, price, seats)
        self.destroy()

class InsertPassengerWindow(tk.Toplevel):
    def __init__(self, master, db_helper):
        super().__init__(master)
        self.title("Insert Passenger")
        self.geometry("400x300")

        self.db_helper = db_helper
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Passenger Details", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self, text="Passenger ID:", font=("Helvetica", 12)).grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.p_id_entry = tk.Entry(self)
        self.p_id_entry.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(self, text="Passenger Name:", font=("Helvetica", 12)).grid(row=2, column=0, pady=5, padx=5, sticky="e")
        self.p_name_entry = tk.Entry(self)
        self.p_name_entry.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(self, text="Flight ID:", font=("Helvetica", 12)).grid(row=3, column=0, pady=5, padx=5, sticky="e")
        self.fl_id_entry = tk.Entry(self)
        self.fl_id_entry.grid(row=3, column=1, pady=5, padx=5)

        tk.Label(self, text="Phone Number:", font=("Helvetica", 12)).grid(row=4, column=0, pady=5, padx=5, sticky="e")
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=4, column=1, pady=5, padx=5)

        tk.Button(self, text="Save", command=self.save_passenger, font=("Helvetica", 12), bg="#007bff", fg="white", width=10).grid(row=5, column=0, columnspan=2, pady=10)

    def save_passenger(self):
        p_id = self.p_id_entry.get()
        p_name = self.p_name_entry.get()
        fl_id = self.fl_id_entry.get()
        phone = self.phone_entry.get()

        self.db_helper.insert_passenger(p_id, p_name, fl_id, phone)
        self.destroy()

if __name__ == "__main__":
    welcome = WelcomePage()
    welcome.mainloop()
