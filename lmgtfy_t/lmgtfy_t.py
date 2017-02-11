import twitter
from googleapiclient.discovery import build
import config

def last_reply_status_id(api):
    last_reply_status_id = None
    last_status_list = api.GetUserTimeline(screen_name=config.account, count=1)
    if last_status_list:
        last_status = api.GetStatus(last_status_list[0].id)
        last_reply_status_id = last_status.in_reply_to_status_id
    return last_reply_status_id

def last_status(api):
    statuses = api.GetUserTimeline(screen_name=config.follow_account,
                                   count=1,
                                   include_rts=False)
    return statuses[0]

def im_feeling_lucky_url(key, cx, query):
    url = None
    service = build('customsearch', 'v1', developerKey=key)
    result = service.cse().list(q=query, cx=cx).execute()
    if 'items' in result:
        url = result['items'][0]['link']
    return url

def main():
    api = twitter.Api(consumer_key        = config.consumer_key,
                      consumer_secret     = config.consumer_secret,
                      access_token_key    = config.access_token,
                      access_token_secret = config.access_token_secret)

    status = last_status(api)
    reply = None
    if status.id != last_reply_status_id(api):
        url = im_feeling_lucky_url(config.google_api_key, config.google_cx, status.text)
        if url:
            reply = '.@{0} {1}'.format(config.follow_account, url)
            api.PostUpdate(reply, in_reply_to_status_id=status.id)
    return reply
