#need to install "pip install requests"
#need to install "pip install fake_useragent"

import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus


def get_user_agent():
    ua = UserAgent()
    return ua.firefox


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

            writer.writerow([str(slno), user_input])
            slno+=1

    output = csv.reader(file, delimiter=" ")
    for row in output:
        print(", ".join(row))



def main():
    print("Please select one from below: ")
    print("1. Create new website list.")
    print("2. Access existing website list.")
    print()
    try:
        num = int(input("Please enter your choice: "))
        if num==1:
            new_csv = generate_csv()

    except ValueError:
        print("Please enter a valide selection")



if __name__=="__main__":
    main()




    
    