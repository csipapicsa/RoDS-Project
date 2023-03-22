import praw

def user_login(client_id, client_secret,username,password,user_agent):
    # reddit api login
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         username=username,

                         password=password,
                         user_agent=user_agent)
    return reddit
    
reddit = user_login('Dh9jkbjqVfypy4JtfOcGlw', 
                    'GZIAAePsuJh5qWUTw2ESEE9Xg0VGtw',
                    'csipapicsa',
                    'cs1pap1csa1',
                    'put here your user agent')