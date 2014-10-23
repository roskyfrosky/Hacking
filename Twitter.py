#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import tweepy, argparse
from random import choice

#Argparser
parser = argparse.ArgumentParser()
parser.add_argument("User",help="User's name or User's id")
args=parser.parse_args()

 
#Twitter Information
CONSUMER_KEY = "your consumer key"
CONSUMER_SECRET="Your consumer secret key"
ACCESS_KEY="your access key"
ACCESS_SECRET="Your access secret key"
API=""
tweets=""

def autentication(user):
	global API ,tweets
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	API = tweepy.API(auth)
	tweets=API.user_timeline(user) #UserID

def followers(user):
	user = API.get_user(user)
	print "User name: " + user.screen_name
	print "Amount of User follorwer: " + str(user.followers_count)
	if not user.friends:
		for friend in user.friends():
			print friend.screen_name
	else:
		print "He/She doesn't have any friends yet!"	

def main(): 
	idUser= args.User
	autentication(idUser)
	followers(idUser)

if __name__=="__main__":
	main()
