from datetime import datetime
import requests
import os
import time
c=0

while True:
    def create_session_info(center, session):
        return {"name": center["name"],
                "date": session["date"],
                "capacity": session["available_capacity"],
                "age_limit": session["min_age_limit"]}

    def get_sessions(data):
        for center in data["centers"]:
            for session in center["sessions"]:
                yield create_session_info(center, session)

    def is_available(session):
        return session["capacity"] > 0

    def is_eighteen_plus(session):
        return session["age_limit"] == 18

    def get_for_seven_days(start_date):
        url = os.environ['REQUEST_URL2']+"?pincode={0}&date={1}".format(os.environ['PIN'],start_date.strftime("%d-%m-%Y"))
        time.sleep(3)
        #params = {"pincode": os.environ['PIN'], "date": start_date.strftime("%d-%m-%Y")}
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
        resp = requests.get(url, headers=headers)
        data = resp.json()
        return [session for session in get_sessions(data) if is_eighteen_plus(session) and is_available(session)]

    def create_output(session_info):
        return f"{session_info['date']} - {session_info['name']} ({session_info['capacity']})"

    print(get_for_seven_days(datetime.today()))
    content = "\n".join([create_output(session_info) for session_info in get_for_seven_days(datetime.today())])

    if not content:
        c+=1
        print(c)
        print("No availability")
    else:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
        req2 = requests.get(url=os.getenv('REQUEST_URL1'), headers=headers)
        req3 = requests.get(url=os.getenv('REQUEST_URL3'), headers=headers)
