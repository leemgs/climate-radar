from backend import db
from random import uniform, choice

db.init()
names = ["Kim","Lee","Park","Choi","Jung","Han","Kang"]
needs = ["medical","water","evacuation","checkin"]
caps  = ["medical","logistics","rescue","general"]

for _ in range(5):
    db.add_request(choice(names), uniform(37.5,37.6), uniform(126.95,127.02), choice(needs), 2)

for _ in range(6):
    db.add_volunteer(choice(names), uniform(37.5,37.6), uniform(126.95,127.02), choice(caps))

print("Seeded.")    
