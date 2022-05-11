from bs4 import BeautifulSoup
import requests
import smtplib
import datetime

# ~~~~~ This is the part that gets all the html data ~~~~~
response = requests.get("https://nationaldaycalendar.com/what-day-is-it/")
response.raise_for_status()
site = response.text

# ~~~~~ Getting the date ~~~~~
today = datetime.date.today()
format_date = today.strftime("%B %d, %Y")
now = datetime.datetime.now()
day_of_week = now.weekday()

# ~~~~~ The Soup ~~~~~
soup = BeautifulSoup(site, "html.parser")

# ~~~~~ Scraping for holidays ~~~~~
holidays = []
holiday_dump = soup.find_all("span", class_="evcal_desc2 evcal_event_title")
for i in holiday_dump:
    text = i.getText()
    holidays.append(text)

# ~~~~~ Scraping for hyperlinks ~~~~~
holiday_links = []
divs = soup.find_all("div", class_="evo_event_schema")
for i in divs:
    holiday_links.append(i.find('a')['href'])

# ~~~~~ Combining the info into a dicitonary ~~~~~

master_list = dict(zip(holidays, holiday_links))


# ~~~~~ Fancy Function ~~~~~
#  This is the OLD function, which worked in terminal but not in reality.

# def master_print():
#     for i in master_list.items():
#         print(i)

# This is the NEW function, developed with the help of @aetimmes.
def master_print():
    result = ""
    for k in master_list:
        result += f"{k} {master_list[k]}\n"
    return result


# ~~~~~ Email ~~~~~
my_email = "eyeheartnickelback@gmail.com"
password = "l00k@thisph0togr4ff"


if day_of_week == 2:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="fake-email@cox.net",
            msg=f"Subject:National Days!\n\nHello! Here are the National Days for {format_date}:\n{master_print()}".encode("ascii", "ignore")
        )

