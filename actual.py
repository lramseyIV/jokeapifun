import logging
import requests
import smtplib
import json

#logging config
logging.basicConfig(filemode='a', filename='sample.log', level=logging.INFO, format='%(levelname)s - %(asctime)s - %(message)s')

#global vars
URL='https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Pun'
# get creds and recipients from file
# I hate doing with open blah blah blah this is a simple read and close!
f = open('config.json', 'r')
config = json.load(f)
f.close()
SENDER = config['email_creds']['email']
PASSWORD = config['email_creds']['password']
RECIPIENTS = config['recipients']



# funtion definitions

def send_email(joke):
    s = smtplib.SMTP('smtp.gmail.com', 587) # will change if not using gmail
    s.starttls()
    try:
        s.login(SENDER, PASSWORD)
    except smtplib.SMTPAuthenticationError:
        logging.error('Authentication Failed when sending email')
        exit()
    message = f'\n{joke}'
    try:
        s.sendmail(SENDER, RECIPIENTS, message)
    except smtplib.SMTPException:
        logging.error('Email failed to send - not authentication error')
        exit()
    s.quit()

def make_request():
    try:
        res = requests.get(URL)
    except requests.HTTPError: # no authentication-specific exceptions will occur
        logging.error('HTTP request unsuccessful')
        exit()
    return res.json()

def extract_joke(result):
    if result['type'] == "twopart":
        setup = result['setup']
        delivery = result['delivery']
        joke_string = f'Setup: {setup}\n Delivery: {delivery}'
    else:
        joke_string = result['joke']
    return joke_string

if __name__=='__main__":
    result = make_request()
    joke = extract_joke(result)
    logging.info('Joke Successfully Created')
    send_email(joke)
    logging.info('Joke Email Complete')
