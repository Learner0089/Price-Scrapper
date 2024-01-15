import requests #Access the url(page)
from bs4 import BeautifulSoup #With it we can import individual items from it
import smtplib   #This package enables you to send emails

URL = 'https://www.amazon.in/Sony-ILCE-7M4-Full-Frame-Interchangeable-Lens-Mirrorless/dp/B09SB6H876/ref=sr_1_1_sspa?crid=3Q27IMDVN2QEV&keywords=sony+alpha+ilce+7m3e&qid=1664780924&qu=eyJxc2MiOiIxLjYzIiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=Sunny+alpha+ilce+7m3%2Caps%2C219&sr=8-1-spons&psc=1'

headers ={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
#It gives us info about our browser.
def check_price():
    page = requests.get(URL, headers=headers) #It returns all the data from the web site


    soup = BeautifulSoup(page.content, 'html.parser')#Will parse things for us

    title = soup.find(id= "productTitle").get_text()
    price = soup.find(class_= "a-price-whole").get_text()
    s = price.replace(',', '') 
    converted_price =float(s[0:7])

    if(converted_price < 242990.0):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 242990.0):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)  
     #Establish connectivity between our connection and gmails(gmailsmtp, connection number)
    server.ehlo()  
    #It is a command sent by email server to identify itself while connecting to another email server to start the process of sending an email
    server.starttls() #Encrypts our connection
    server.ehlo()


    server.login('mihir.2024csit1023@kiet.edu','Kiet@123#') #Sender

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Sony-ILCE-7M4-Full-Frame-Interchangeable-Lens-Mirrorless/dp/B09SB6H876/ref=sr_1_1_sspa?crid=3Q27IMDVN2QEV&keywords=sony+alpha+ilce+7m3e&qid=1664780924&qu=eyJxc2MiOiIxLjYzIiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=Sunny+alpha+ilce+7m3%2Caps%2C219&sr=8-1-spons&psc=1'

    msg = f"Subject: {subject}\n\n{body}" #Helps in combining subject and body

    server.sendmail(
        'mihir.2024csit1023@kiet.edu',     #Sender
        'marockstar01@gmail.com',          #Receiver
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

check_price()


