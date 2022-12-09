from datetime import datetime
import pytz

def print_time(region):
    country_time_zone = pytz.timezone(region)
    country_time = datetime.now(country_time_zone)
    print(country_time.strftime("\n\nDate: %d/%m/%y. Time: %H:%M:%S"))

time_zones = pytz.all_timezones
user_input = ""
while user_input.lower() != "q":
    user_input = input("\n\n\nSelect an option\n1) Search by continent/large region\n2) Search by timezone name\n3) Search by timezone code\nQ) Quit program\n\n")

    if user_input == "1":
        checksum = False
        while checksum == False:
            user_input = input("Pick from the following list\n\nAfrica\nAmerica\nAntarctica\nArctic\nAsia\nAtlantic\nAustralia\nEurope\nIndian\nPacific\n\n")
            if user_input.title() in ("Africa", "America", "Antarctica", "Arctic", "Asia", "Atlantic", "Australia", "Europe", "Indian", "Pacific"):
                checksum = True
                user_input = user_input.title()
                continent = user_input

                print("\nPick from this list of locations\n")

                counter = 0
                list = []
                for i in time_zones:
                    if i.split("/",1)[0] == user_input:
                        print(i.split("/")[-1] + "; ", end="")
                        counter += 1
                        list.append(i.split("/")[-1])
                        if counter % 4 == 0:
                            print("")
                while user_input not in list:
                    user_input = input("\n")
                    user_input = user_input.title()
                    user_input = user_input.replace(" ", "_")
                    if user_input in list:
                        print_time(continent + "/" + user_input)
                    else:
                        print("ERROR: entry not found, try again.\n")
            else:
                print("ERROR: entry not found, try again.\n")
    elif user_input == "2":
        print("\nPick from this list of timezones\n")

        counter = 0
        list = []
        for i in time_zones:
            if ("/" not in i) and ("+" not in i) and ("-" not in i):
                print(i + "; ", end="")
                counter += 1
                list.append(i)
                if counter % 4 == 0:
                    print("")
        while user_input.upper() not in list and user_input.title() not in list:
            user_input = input("\n")
            if user_input.title() in list:
                print_time(user_input.title())
            elif user_input.upper() in list:
                print_time(user_input.upper())
            else:
                print("ERROR: entry not found, try again.")
                user_input = input("")


    elif user_input == "3":
        print("\nPick from GMT offset\n")

        counter = 0
        list = []
        for i in time_zones:
            if ("Etc/" in i):
                print(i.split("/")[-1] + "; ", end="")
                counter += 1
                list.append(i.split("/")[-1])
                if counter % 4 == 0:
                    print("")
        while user_input not in list:
            user_input = input("\n")
            user_input = user_input.upper()
            if user_input in list:
                print_time("Etc/" + user_input)
            else:
                print("ERROR: entry not found, try again.")
                user_input = input("")
    elif user_input.lower() == "q":
        print("Exiting program...")
    else:
        print("ERROR: invalid input")