#Changed name from uuid.py to uuid1.py because I had some issues with importing the correct library
from uuid import uuid4
import pandas as pd
import datetime 
from random import *


myuuid = uuid4()
df = pd.read_csv('./Hospital General Information.csv', delimiter=',', encoding='cp1252')
df_new = df[['Hospital Name','Address']][:10]
l = []
for i in range(10):
    l.append(str(uuid4()))

list_of_hos_id = l
queries = []
for i, row in df_new.iterrows():
    queries.append(f"""INSERT INTO Hospital(h_id, address, name) VALUES("{l[i]}", "{row['Address']}", "{row['Hospital Name']}");""")

for l in queries:
    print(l)
print("\n\n\n\n\n\n\n\n\n\n\n")

hos_id = []
for i in range(20):
    hos_id.append(list_of_hos_id[randrange(10)])

doctor_names = ["Liam Olivia",
                "Noah Emma",
                "Oliver	Ava",
                "Elijah	Charlotte",
                "William Sophia"
                "James Amelia",
                "Benjamin Isabella",
                "Lucas Mia",
                "Henry Evelyn",
                "Alexander Harper"
                "James Smith",
                "Michael Smith",
                "Robert Smith",
                "Maria Garcia",
                "David Smith",
                "Maria Rodriguez",
                "Mary Smith",
                "Maria Hernandez",
                "Maria Martinez",
                "James Johnson",
                "Yoan Palacios",
                "Aayush Koirala"
            ]
start = []
for i in range(20):
    start_date = datetime.date(2001, 1, 1)
    end_date = datetime.date(2021, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    start.append(random_date)

phone_number = []
for i in range(20):
    ph_no = []
    # the first number should be in the range of 6 to 9
    ph_no.append(randint(6, 9))
    
    # the for loop is used to append the other 9 numbers.
    # the other 9 numbers can be in the range of 0 to 9.
    for i in range(1, 10):
        ph_no.append(randint(0, 9))
    
    # printing the number
    l = ""
    for i in ph_no:
        l += str(i)
    phone_number.append(l)

l = []
for i in range(20):
    l.append(str(uuid4()))

doctor = pd.DataFrame()

doctor['name'] = doctor_names
doctor['id'] = l
doctor['started_working'] = start
doctor['phone_number'] = phone_number
doctor['hospital'] = hos_id


queries = []
for i, row in doctor.iterrows():
    queries.append(f"""INSERT INTO Doctor(d_id, name, started_working, phone_number, h_id) VALUES("{row['id']}", "{row['name']}", "{row['started_working']}", "{row['phone_number']}", "{row['hospital']}");""")

for l in queries:
    print(l)
print("\n\n\n\n\n\n\n\n\n\n\n")