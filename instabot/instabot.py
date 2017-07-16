import requests, urllib
from termcolor import colored
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer          #importing library to check negativity and positivity of a comment

APP_ACCESS_TOKEN ='5701374384.6a7409d.6f1f926003d14c6b9a5a603181e5636b'     #token of id :nikki_mikki
#Sandbox Users :

BASE_URL = 'https://api.instagram.com/v1/'

#Function declaration start to get user own info...

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s\n' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print colored('User does not exist!','red')
    else:
        print 'Status code other than 200 received!'



# Function declaration start to get the ID of a user by username

def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()                                               #function to get id od user ends here..........


#Function declaration start to get the info of a user by username

def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s\n' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print colored('There is no data for this user!','red')
    else:
        print 'Status code other than 200 received!'            #function to get the info of a user ends here........



# Function declaration start to get your recent post.....

def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print colored('Post does not exist!','red')
    else:
        print 'Status code other than 200 received!'              #function to get your recent post ends here...........


# Function declaration start to get the recent post of a user by username

def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print colored('Sorry User does not exist!..Try again','red')
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print colored('Post does not exist!','red')
    else:
        print 'Status code other than 200 received!'                        #function to get recent post ends here........


# Function declaration start to get the ID of the recent post of a user by username

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print colored('There is no recent post of the user!','red')
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()                                                             #function to get the id of recent post ends here.......



# Function declaration start to like the recent post of a user

def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Yeah..like was successful!'
    else:
        print colored('Oops....Your like was unsuccessful. Try again!','red')        #function to start the recent post ends here......

# Function declaration to Get the like lists on the recent post of a user.........


def get_like_list(insta_username):            # Defining the Function ............
    media_id = get_post_id(insta_username)  # Getting post id by passing the username .......
    request_url = BASE_URL + 'media/%s/likes?access_token=%s' % (media_id, APP_ACCESS_TOKEN)    #    passing the end points and media id along with access token ..
    print colored('GET request url : %s\n', 'blue') % (request_url)
    like_list = requests.get(request_url).json()

    if like_list['meta']['code'] == 200:  # checking the status code .....
        if len(like_list['data']):
            position = 1
            print colored("List of people who Liked Your Recent post", 'blue')
            for users in like_list['data']:
                if users['username']!= None:
                    print position, colored(users['username'],'green')
                    position = position + 1
                else:
                    print colored('No one had liked Your post!\n', 'red')
        else:
            print colored("User Does not have any post.\n",'red')
    else:
        print colored('Status code other than 200 recieved.\n', 'red')           #function to get the like list ends here.......

#Function declaration to Get the lists of comments on  the recent post of a user.........

def get_comment_list(insta_username):  # Defining the Function ............
    media_id = get_post_id(insta_username)  # Getting post id by passing the username .......
    request_url = BASE_URL + 'media/%s/comments?access_token=%s' % (media_id, APP_ACCESS_TOKEN)   #    passing the end points and media id along with access token ..
    print colored('GET request url : %s\n', 'blue') % (request_url)
    comment_list = requests.get(request_url).json()

    if comment_list['meta']['code'] == 200:  # checking the status code .....
        if len(comment_list['data']):
            position = 1
            print colored("List of people who commented on Your Recent post", 'blue')
            for _ in range(len(comment_list['data'])):
                if comment_list['data'][position-1]['text']:
                    print colored(comment_list['data'][position-1]['from']['username'],'magenta') +colored( ' said: ','magenta') + colored(comment_list['data'][position-1]['text'],'blue')      #    Json Parsing ..printing the comments ..
                    position = position+1
                else:
                    print colored('No one had commented on Your post!\n', 'red')
        else:
            print colored("There is no Comments on User's Recent post.\n", 'red')
    else:
        print colored('Status code other than 200 recieved.\n', 'red')            #function to get the list of comments ends here.....


# Function declaration start to make a comment on the recent post of the user

def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully a comment is added!"
    else:
        print colored(" Sorry , Unable to add this comment.Please Try again!",'red')      #function to make comment on recent post ends here......


# Function declaration start to make delete negative comments from the recent post

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive library is implemented to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment deleted successfully!\n'
                    else:
                        print colored('Request to delete a comment is cancelled!','red')
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print colored('No comments are exist on this post!','red')
    else:
        print 'Status code other than 200 received!'


def start_bot():
    while True:
        print '\n'
        print colored('Hey! Welcome to the INSTABOT!','blue')
        print 'Here are your menu options:\n'
        print colored("A. Get your own user details",'green')
        print colored("B. Get details of a user by username",'green')
        print colored("C. Get your own recent post",'green')
        print colored("D. Get the recent post of a user by username",'green')
        print colored("E. Get a list of people who have liked the recent post of a user",'green')
        print colored("F. Like the recent post of a user",'green')
        print colored("G. Get a list of comments on the recent post of a user",'green')
        print colored("H. Make a comment on the recent post of a user",'green')
        print colored("I. Delete negative comments from the recent post of a user",'green')
        print colored("J. Exit",'green')

        choice = raw_input("Enter you choice: ")
        if choice.lower() == "a":
            self_info()
        elif choice.lower() == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice.lower() == "c":
            get_own_post()
        elif choice.lower() == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice.lower() =="e":
           insta_username = raw_input("Enter the username of the user: ")
           get_like_list(insta_username)
        elif choice.lower() =="f":
           insta_username = raw_input("Enter the username of the user: ")
           like_a_post(insta_username)
        elif choice.lower() =="g":
           insta_username = raw_input("Enter the username of the user: ")
           get_comment_list(insta_username)
        elif choice.lower() =="h":
           insta_username = raw_input("Enter the username of the user: ")
           post_a_comment(insta_username)
        elif choice.lower() =="i":
           insta_username = raw_input("Enter the username of the user: ")
           delete_negative_comment(insta_username)
        elif choice.lower() == "j":
            exit()
        else:
            print colored("wrong choice",'red')

start_bot()