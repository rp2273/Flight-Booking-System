import mysql.connector
con = mysql.connector.connect(host= 'localhost', user= 'root', password= "123456789", database= 'jetairways')
print("Enter 1 for viewing a passenger's ticket")
print("Enter 2 for changing the flight's timings")
print("Enter 3 for adding a passenger's ticket")
print("Enter 4 for changing phone no.")
print("Enter 5 for cancelling a passenger's ticket")
ch = int(input("Enter your choice: "))
query1 = "select p_id, Fl_id from passenger"
cur = con.cursor()
cur.execute(query1)
fetch1 = cur.fetchall()

if ch == 1:
    s = input("Enter passenger id: ")
    q = input("Enter flight id: ")
    r = (s,) + (q,)
    if r in fetch1:
        query = "select p.p_id,p.p_name,f.Fl_id,f.Fl_name,f.departure,f.arrival,f.source, f.destination from passenger p, flight f WHERE p.p_id='{}' AND p.Fl_id = f.Fl_id".format(s,)
        curs = con.cursor()
        curs.execute(query)
        fetch= curs.fetchone()
        print("The passenger's ticket is: ")
        print("Passenger id= ",fetch[0])
        print("Passenger name= ",fetch[1])
        print("Flight id= ",fetch[2])
        print("Flight name= ",fetch[3])
        print("Departure= ",fetch[4])
        print("Arrival= ",fetch[5])
        print("Source= ",fetch[6])
        print("Destination= ",fetch[7])
    else:
        print("No such passenger exists. Kindly recheck the passenger id.")
if ch == 2:
    q = input("Enter flight id: ")
    for i in range(len(fetch1)):
        if q in fetch1[i][1]:
            a = input("Enter the details of departure: ")
            b = input("Enter the details of arrival: ")
            c = input("Previous departure time: ")
            d = input("Previous arrival time: ")
            query = "UPDATE flight SET departure = '{}', arrival = '{}' WHERE departure = '{}' AND arrival = '{}' ".format(a,b,c,d)
            cur1 = con.cursor()
            cur.execute(query)
            con.commit()
            print("The timings of the flight has been updated.")
            break
    else:
        for i in range(1):
            print("Enter a valid flight id.")

if ch == 3:
    d = input("Enter flight id: ")
    query1 = "Select no_of_available_seats_150 from flight WHERE Fl_id = '{}'".format(d)
    cur = con.cursor()
    cur.execute(query1)
    fetch= cur.fetchone()
    if fetch[0]>0:
        print("Seats are available. Proceeding to book a seat.")
        a = input("Enter passenger no.: ")
        b = input("Enter passenger id: ")
        c = input("Enter passenger name: ")
        e = input("Enter passenger's phone no.: ")
        query = "INSERT INTO passenger(p_no, p_id, p_name, Fl_id, p_phn)VALUES({},'{}', '{}', '{}', '{}')".format(a,b,c,d,e)
        cur.execute(query)
        con.commit()
        query2 = fetch[0] - 1
        print("Seat booked!")
    else:
        print("OOPS! THE FLIGHT IS FULL.")
    query3 = "UPDATE flight SET no_of_available_seats_150 = '{}' WHERE no_of_available_seats_150 = '{}'".format(query2,fetch[0])
    cur.execute(query3)
    con.commit()

if ch == 4:
    s = input("Enter passenger id: ")
    q = input("Enter flight id: ")
    r = (s,) + (q,)
    if r in fetch1:
        a = input("Enter passenger's new phone no.: ")
        b = input("Enter passenger's previous phone no.: ")
        query = 'UPDATE passenger SET p_phn = "{}" WHERE p_phn = "{}"'.format(a,b)
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        print("The passenger's phone no. has been updated.")
    else:
        print("No such passenger exists. Kindly recheck the passenger id or flight id.")


if ch == 5:
    s = input("Enter passenger id: ")
    q = input("Enter flight id: ")
    r = (s,) + (q,)
    if r in fetch1:
        print("Passenger found! Proceeding to cancel the ticket.")
        query1 = "Select no_of_available_seats_150 from flight WHERE Fl_id = '{}'".format(q)
        cur = con.cursor()
        cur.execute(query1)
        fetch= cur.fetchone()
        query = "DELETE FROM passenger WHERE p_id='{}' ".format(s)
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        query2 = fetch[0] + 1
        query3 = "UPDATE flight SET no_of_available_seats_150 = '{}' WHERE no_of_available_seats_150 = '{}'".format(query2,fetch[0])
        cur.execute(query3)
        con.commit()
        print("The passenger's ticket has been cancelled.")
    else:
        print("No such passenger exists. Kindly recheck the passenger id or flight id.")
