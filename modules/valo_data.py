import requests
import os
profile = 'https://api.tracker.gg/api/v2/valorant/standard/profile/riot/'
matches = profile.replace('profile', 'matches')
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
}
cookie = {'__cf_bm': os.environ.get('API_COOKIE')}


def getShots(name):
    heads = body = legs = 0
    r = requests.get(matches + name.replace('#', '%23'),
                     headers=header, cookies=cookie).json()
    if 'errors' in r:
        return r['errors'][0]['message']

    for i in range(20):
        stats = r['data']['matches'][i]['segments'][0]['stats']
        heads += stats['dealtHeadshots']['value']
        body += stats['dealtBodyshots']['value']
        legs += stats['dealtLegshots']['value']

    total = heads + body + legs
    return (round(heads*100/total, 2), round(body*100/total, 2), round(legs*100/total, 2))


def getData(name):
    r = requests.get(profile + name.replace('#', '%23'),
                     headers=header, cookies=cookie).json()
    if 'errors' in r:
        return r['errors'][0]['message']

    agents = []
    d = {'name': name}
    for x in r['data']['segments']:
        if x['type'] == 'agent':
            agents.append({'name': x['metadata']['name'], 'role': x['metadata']['role'], 'matchesPlayed': x['stats']['matchesPlayed']['value'],
                           'matchesWinPct': x['stats']['matchesWinPct']['displayValue'], 'kDRatio': x['stats']['kDRatio']['displayValue']})

    agents.sort(key=lambda x: x['matchesPlayed'], reverse=True)
    d['agents'] = agents[:3]

    for x in r['data']['segments']:
        if x['metadata']['name'] == 'Competitive':
            stats = x['stats']
            d['timePlayed'] = stats['timePlayed']['displayValue']
            d['kDRatio'] = stats['kDRatio']['displayValue']
            d['rank'] = stats['rank']['metadata']['tierName']
            d['kills'] = stats['kills']['displayValue']
            d['deaths'] = stats['deaths']['displayValue']
            d['matchesPlayed'] = stats['matchesPlayed']['displayValue']
            d['matchesWon'] = stats['matchesWon']['displayValue']
            d['matchesLost'] = stats['matchesLost']['displayValue']
            d['headshots'] = stats['headshots']['displayValue']
            d['headPct'], d['bodyPct'], d['legPct'] = getShots(name)
            return d

    return "You haven't played Competitive in recent 20 matches."
