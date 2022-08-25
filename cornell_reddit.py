import praw
import pandas as pd



def extract_data():
    reddit = praw.Reddit(client_id = "4am2ey7nijb_4g", client_secret="BWUwPaUawy5Q6_UBuj99f-pcNgRHag", user_agent= "my user agent", username = "redditkarma_dotcom", password = "Mcqknight1")


    master_df = pd.DataFrame({"title" : [], "score" : [], "id" : [], "url" : [], "comms_num" : [], "created" : [], "body" : [], "query" : [], "school" : []})


    sub = ['Cornell', 'princeton', 'Harvard', 'dartmouth', 'BrownU', 'yale', 'UPenn', 'columbia', 'stanford', 'berkeley','cmu', 'Caltech',
    'mit', 'gatech', 'Tufts', 'nyu', 'notredame', 'Vanderbilt', 'USC', 'Swarthmore', 'WilliamsCollege', 'uchicago', 'Northwestern',
    'northeastern', 'jhu', 'duke', 'riceuniversity', 'washu', 'Emory', 'georgetown','uofm', 'VirginiaTech', 'UVA', 'UNC', 'wfu', 'UCSantaBarbara',
    'UCSD', 'UCI','ucr', 'ucmerced','UCDavis', 'UCSC', 'URochester', 'rit', 'bostoncollege','Tulane', 'williamandmary', 'BostonU', 'brandeis',
    'cwru', 'UTAustin', 'UWMadison', 'UGA', 'UIUC', 'Pepperdine', 'Purdue','RPI', 'SCU', 'villanova', 'fsu', 'Syracuse', 'Pitt', 'udub',
    'PennStateUniversity', 'UCONN', 'Fordham', 'gwu', 'LMU', 'SMU', 'aggies', 'amherstcollege', 'umass', 'uofmn', 'Clemson', 'WVU', 'AmericanU',
    'baylor', 'IndianaUniversity', 'Gonzaga', 'HowardUniversity', 'msu', 'NCSU', 'boulder', 'BinghamtonUniversity', 'SBU', 'UBreddit', 'iastate', 'auburn',
    'ASU', 'udel', 'uofu', 'UofO', 'UTK', 'NJTech', 'Gamecocks', 'UniversityofVermont', 'UniversityofKansas', 'mizzou' , 'UniversityofKentucky', 'Huskers']


    #ucla, osu, rutgers gmu  'sooners', 'SDSU' 'capstone'

    for subreddit_name in sub:
        subreddit = reddit.subreddit(subreddit_name)
        post_dict = {
        "title" : [],
        "score" : [],
        "id" : [],
        "url" : [],
        "comms_num" : [],
        "created" : [],
        "body" : [],
        "query" : [],
        "school" : []


        }


        query = ['depression', 'struggling', 'anxious', 'therapy', 'mental health', 'overwhelmed', 'crying']



        for item in query:


            for submission in subreddit.search(query, sort = 'top'):
                if (submission.url == 'https://www.reddit.com/r/ucla/comments/dixxep/i_always_feel_like_the_stupidest_one_in_my_stem/' ):
                    pass

                post_dict['title'].append(submission.title)
                post_dict['score'].append(submission.score)
                post_dict['id'].append(submission.id)
                post_dict['url'].append(submission.url)
                post_dict['comms_num'].append(submission.num_comments)
                post_dict['created'].append(submission.created)
                post_dict['body'].append(submission.selftext)
                post_dict['query'].append(item)
                post_dict['school'].append(subreddit_name)
                print(post_dict)


        post_data = pd.DataFrame(post_dict)
        master_df = master_df.append(post_data, ignore_index = True)
    return master_df
