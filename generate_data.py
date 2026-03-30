import csv
import random
from datetime import datetime, timedelta

# generating fake data for my project
def make_data(file_name="dataset.csv", num_days=90):
    print("making data   ")
    places = ["Gym", "Library", "Cafeteria"]
    rows = []
    
    start = datetime.now() - timedelta(days=num_days)
    
    for d in range(num_days):
        curr = start + timedelta(days=d)
        day_str = curr.strftime("%A")
        
        for h in range(24):
            for p in places:
                # check timings
                is_open = False
                if p == "Gym" and (4 <= h <= 23):
                    is_open = True
                elif p == "Library" and (8 <= h <= 22):
                    is_open = True
                elif p == "Cafeteria" and (10 <= h <= 23 or h <= 1):
                    is_open = True

                if is_open:
                    # random base crowd
                    count = random.randint(10, 30)
                    
                    # rush hours
                    if p == "Gym" and (17 <= h <= 20):
                        count += random.randint(40, 70)
                    if p == "Library" and (10 <= h <= 15):
                        count += random.randint(30, 60)
                    if day_str == "Saturday" or day_str == "Sunday":
                        count = max(5, count - 20)
                    
                    # set status
                    if count < 25:
                        status = "Empty"
                    elif count < 60:
                        status = "Moderate"
                    else:
                        status = "Crowded"
                        
                    time_format = f"{h:02d}:00"
                    rows.append([curr.strftime("%Y-%m-%d"), day_str, time_format, p, count, status])
                
    # save to csv
    with open(file_name, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(["Date", "DayOfWeek", "Time", "Facility", "Headcount", "Status"])
        w.writerows(rows)
        
    print("done. saved", len(rows), "rows.")

if __name__ == "__main__":
    make_data()