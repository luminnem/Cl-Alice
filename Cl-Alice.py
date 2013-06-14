# Encoding: UTF-8
# -*- coding: utf-8 -*-

__author__ = 'JerryMrSlime'

import twitter
import time


def main():
    consumerKey = ""
    consumerSecret = ''
    accessKey = '-'
    accessSecret = ''
    api = twitter.Api(consumerKey, consumerSecret, accessKey, accessSecret)

    while True:

        followers = api.GetFollowers(screen_name='')
        try:
            for follower in followers:
                tweets = api.GetUserTimeline(screen_name=follower.screen_name, count='1')
                for tweet in tweets:
                    print follower.screen_name, ' ', tweet._text
                    api.PostRetweet(tweet._id)
        except twitter.TwitterError:
            pass

        tags = api.GetSearch("#")
        for tag in tags:
            if tag.user.screen_name != '':
                api.CreateFriendship(screen_name=tag.user.screen_name)
                print "New friendship", tag.user.screen_name

        try:
            for tweet in api.GetUserTimeline(screen_name=''):
                api.PostRetweet(tweet._id)
        except twitter.TwitterError:
            pass

		try:
            for tweet in api.GetUserTimeline(screen_name='', count='5'):
                api.PostRetweet(tweet._id)
        except twitter.TwitterError:
            pass

        for mention in api.GetMentions(count=10):
            if mention._text == '@USER Hello, how are you?' and mention.n:
                api.PostUpdate(in_reply_to_status_id=mention._id, status="I'm very fine thanks and what about you?")
        time.sleep(600)

if __name__ == "__main__":
    main()
