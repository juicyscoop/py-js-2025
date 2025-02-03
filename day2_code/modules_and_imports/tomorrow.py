from datetime import datetime
import time

def tomorrow():
    # Returns day of tomorrow
    # ma kalendar metoda "dnesek"?
    # tomorrow = (datetime.now() + timedelta(days=1)).strftime("%B/%d/%Y")
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return tomorrow

print(time.time())