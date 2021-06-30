from datetime import datetime
import requests
import os
import time
c=0

while True:
    
    start_date = datetime.now()
    
     def get_for_seven_days(start_date):
        try:
            url = os.environ['REQUEST_URL2']+"?pincode={0}&date={1}".format(os.environ['PIN'],start_date.strftime("%d-%m-%Y"))
            time.sleep(3)
            #params = {"pincode": os.environ['PIN'], "date": start_date.strftime("%d-%m-%Y")}
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
            resp = requests.get(url, headers=headers)
            data = resp.json()
            return [session for session in get_sessions(data) if is_eighteen_plus(session) and is_available(session) and is_free(session)]
        except Exception:
            print("something went wrong...restarting the program....")
            handle_excp()
    
    def create_session_info(center, session):
        return {"name": center["name"],
                "date": session["date"],
                "capacity": session["available_capacity"],
                "age_limit": session["min_age_limit"],
               "fee_type": center["fee_type"]}

    def get_sessions(data):
        for center in data["centers"]:
            for session in center["sessions"]:
                yield create_session_info(center, session)

    def is_available(session):
        return session["capacity"] > 2

    def is_eighteen_plus(session):
        return session["age_limit"] == 18
    def is_free(session):
        return session["fee_type"] == "Free"

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
        avi_req2 = requests.get(url="http://api.callmebot.com/start.php?source=web&user=@aruavidesh&text=Vaccine%20slots%20available%20book%20fast.&lang=en-US-Standard-B",headers=headers)
        req2 = requests.get(url=os.getenv('REQUEST_URL1'), headers=headers)
        avi_req3 = requests.get(url="http://api.callmebot.com/text.php?source=web&user=@aruavidesh&text=Vaccine%20Slots%20Available!!",headers=headers)
        avi_req4 = requests.get(url="http://api.callmebot.com/text.php?source=web&user=@aruavidesh&text=Made%20with%20❤%20by%20Ani",headers=headers)
        req3 = requests.get(url=os.getenv('REQUEST_URL3'), headers=headers)
        req4 = requests.get(url="http://api.callmebot.com/text.php?source=web&user=@Anirban_Sinha&text=Made%20with%20❤%20by%20Ani",headers=headers)
       
    def handle_excp():
        get_for_seven_days(start_date)
        pass
