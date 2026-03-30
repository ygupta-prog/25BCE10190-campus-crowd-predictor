import csv

class CrowdPredictor:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = self.load_data()

    def load_data(self):
        # load data into a dict
        history = {}
        try:
            with open(self.csv_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    fac = row["Facility"]
                    day = row["DayOfWeek"]
                    t = row["Time"]
                    cnt = int(row["Headcount"])
                    
                    if fac not in history:
                        history[fac] = {}
                    if day not in history[fac]:
                        history[fac][day] = {}
                    if t not in history[fac][day]:
                        history[fac][day][t] = []
                        
                    history[fac][day][t].append(cnt)
            return history
        except FileNotFoundError:
            print("Error: dataset.csv not found. run generator first.")
            exit()

    def get_prediction(self, fac, day, time_str):
        try:
            hr = int(time_str.split(':')[0])
            
            # check if open
            if fac == "Gym" and not (4 <= hr <= 23):
                return "Status: CLOSED (Gym hours are 04:00 to 23:00)"
            elif fac == "Cafeteria" and not (10 <= hr <= 23 or hr <= 1):
                return "Status: CLOSED (Cafeteria hours are 10:00 to 01:00)"
            elif fac == "Library" and not (8 <= hr <= 22):
                return "Status: CLOSED (Library hours are 08:00 to 22:00)"

            t_format = f"{hr:02d}:00"
            
            records = self.data[fac][day][t_format]
            if len(records) == 0:
                return "No data found for this time."
                
            avg = sum(records) / len(records)
            
            if avg < 25:
                stat = "Empty"
            elif avg < 60:
                stat = "Moderate"
            else:
                stat = "Crowded"
                
            return f"Status: {stat}\nAverage people: {avg:.1f}"
            
        except KeyError:
            return "Error: Data not found. Check spelling."
        except ValueError:
            return "Error: Use HH:00 format."

def main():
    print("--- Campus Crowd Predictor ---")
    
    f = input("Enter facility (Gym, Library, Cafeteria): ").strip().title()
    d = input("Enter day (e.g. Monday): ").strip().title()
    t = input("Enter time (e.g. 14:00): ").strip()
    
    print("\nCalculating...")
    
    # run prediction
    model = CrowdPredictor("dataset.csv")
    ans = model.get_prediction(f, d, t)
    
    print(ans)
    print("------------------------------")

if __name__ == "__main__":
    main()