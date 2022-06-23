import re
from collections import Counter
import praw

#for using reddit API
r = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',
                     client_id='hEoLceE15pxrmg', client_secret="NLTjoniv-38kKzpDtL6Q-mS9pkk",
                     username='', password='')
#gets the redditor whos comments you want
user = r.redditor('Laundry_Hamper')

#for each comment found this prints them to a.txt file
for comment in user.posts.top(limit=1000):
    f= open("comments.txt","w+")
    f.write(comment.body)


with open('comments.txt') as f:
    passage = f.read()

words = re.findall(r'\w+', passage)

cap_words = [word.upper() for word in words]

word_counts = Counter(cap_words)

f = open("Comments_Count.txt", "w")
f.write(str(word_counts))
