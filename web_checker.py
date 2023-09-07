#need to install "pip install requests"
#need to install "pip install fake_useragent"

import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus


def generate_csv():
    print("Please enter your website link. enter 'q' / 'Q' to end the entry.")
    with open("new_list.csv", "w", newline="") as file:
        writer = csv.writer(file)
        slno = 1
        writer.writerow(['SNo', 'Website-Address'])

        while True:
            
            user_input = input(f"Enter {slno} number website:")
            if user_input.lower()=="q":
                break
            if "https://" not in user_input :
                if "http://" not in user_input:
                    user_input = "https://"+user_input
                else:
                    user_input = user_input[:4]+ "s" +user_input[4:]
            

            writer.writerow([str(slno), user_input])
            slno+=1

        return


def get_user_agent():
    ua = UserAgent()
    return ua.firefox


def get_status_des(status_code):
    for value in HTTPStatus:
        if value == status_code:
            description = f"({value} {value.name}), {value.descrition}"

    return "(???) Unknown Status Code!!!"



    
def get_websites(csv_path, choice):
    websites = []

    if choice==1:
        with open(csv_path, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if "address" in row[1].lower():
                    continue
                websites.append(row[1])

    return websites


def check_website(web_link:str, user_agent):
    try:
        code = int(requests.get(web_link, headers={"User-Agent":user_agent}).status_code)
        print(web_link, get_status_des(code))

    except Exception:
        print(f"Could not get information for website: {web_link}")

def get_user_agent():
    ua = UserAgent()






def main():
    print("Please select one from below: ")
    print("1. Create new website list.")
    print("2. Access existing website list.")
    print()
    try:
        num = int(input("Please enter your choice: "))
        if num==1:
            new_csv = generate_csv()
            websites = get_websites("new_list.csv", 1)
            print(websites)



        if num==2:
            pass


    except ValueError:
        print("Please enter a valide selection")



if __name__=="__main__":
    main()




    
    