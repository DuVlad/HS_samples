import requests

def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

print exists('http://files.hearthscry.com/collectobot/2019-01-28.zip')
