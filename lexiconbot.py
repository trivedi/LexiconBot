import praw
import auth

from time import sleep

r = praw.Reddit('Lex Luthor the Lexicon Bot')
visited = {}


def login():
	""" Login to account """
	r.login(auth.USERNAME, auth.PASSWORD)

	if r.is_logged_in():
		print "Logged into /u/%s successfully!" % auth.USERNAME
	else:
		print "Incorrect username or password!\nPlease check auth.py."

def defien(word):
	""" DReturns the definition of <word>. """
	

def watch(subreddit="all", limit=10):
	""" Watch a subreddit for LexiconBot definition request """
	sub = r.get_subreddit(subreddit)
	# Go through the top <limit> subreddits sorted by 'hot'
	for submission in sub.get_hot(limit=limit):
		if submission in visited:
			continue
		else:
			visited[submission] = 1
			for comment in submission.comments:
				if "LexiconBot define" in comment.body:
					print comment, "from", comment.permalink, " / ", comment.submission
					msg = define(comment.body.split()[2])
					comment.reply(msg)

	print "Sleeping..."
	sleep(3)


if __name__ == '__main__':
	login()
	while True:
		watch("test")
