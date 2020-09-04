from main import spambot
import configparser
import json

config_path = './config.ini'
cparser = configparser.ConfigParser()
cparser.read(config_path)

username = cparser['AUTH']['USERNAME']
password = cparser['AUTH']['PASSWORD']

comments_file = "1person_comments.json"

# parse the json file to return the appropriate list of comments

def get_comments_data(comments_file, num_of_tags):
    with open("1person_comments.json", "r") as read_file:
         data = json.load(read_file)
    if(num_of_tags == 1):
         return data['list1tag']
    elif(num_of_tags == 2):
         return data['list2tags']
    else:
         return data['list3tags']

if __name__ == '__main__':
    
    comments = get_comments_data(comments_file, 1)    

     # this function takes the actual username (not email or phone number) 
     # and password along with the list of comments that needs to be spammed
    spambot(username, password, comments)