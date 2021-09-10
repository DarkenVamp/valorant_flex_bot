from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

open_bold = ImageFont.truetype('assets/fonts/OpenSans-Bold.ttf', 26)
open_bold_small = ImageFont.truetype('assets/fonts/OpenSans-Bold.ttf', 22)
open_bold_ss = ImageFont.truetype('assets/fonts/OpenSans-Bold.ttf', 16)


def getImg(d):
    canvas = Image.open('assets/canvas.png')
    draw = ImageDraw.Draw(canvas)
    # ===================================================================
    rank = d['rank']
    player_name = d['name'].split('#')[0]
    total_time = d['timePlayed'].upper()

    head_body = f"Head - {d['headPct']}% | Body - {d['bodyPct']}%"
    headshots = f"Headshots - {d['headshots']}"

    total_matches = f"{d['matchesPlayed']} total matches"
    wins_loses = f"{d['matchesWon']} / {d['matchesLost']} - wins / loses"
    kills_deaths = f"{d['kills']} kills | {d['deaths']} deaths"

    top_agent1, top_agent2, top_agent3 = d['agents']

    top_agent1_stats = f"{top_agent1['matchesPlayed']} matches | {top_agent1['matchesWinPct']} wins | {top_agent1['kDRatio']} K/D"
    top_agent2_stats = f"{top_agent2['matchesPlayed']} matches | {top_agent2['matchesWinPct']} wins | {top_agent2['kDRatio']} K/D"
    top_agent3_stats = f"{top_agent3['matchesPlayed']} matches | {top_agent3['matchesWinPct']} wins | {top_agent3['kDRatio']} K/D"

    # ===================================================================

    # PILL - 1
    rank = Image.open(f'assets/ranks/{rank}.png')
    rank.thumbnail((50, 50), Image.ANTIALIAS)
    canvas.paste(rank, (20, 19))

    draw.text((82, 25), player_name, fill='#ffffff', font=open_bold)

    draw.text((337, 28), total_time, fill='#ffffff', font=open_bold_small)
    draw.text((80, 103), "Accuracy Last 20 matches",
              fill='#ffffff', font=open_bold_ss)
    draw.text((80, 137), head_body,
              fill='#ffffff', font=open_bold_ss)
    draw.text((80, 170), headshots, fill='#ffffff', font=open_bold_ss)

    # PILL - 2
    draw.text((356, 103), total_matches, fill='#ffffff', font=open_bold_ss)
    draw.text((356, 137), wins_loses,
              fill='#ffffff', font=open_bold_ss)
    draw.text((356, 170), kills_deaths,
              fill='#ffffff', font=open_bold_ss)

    # PILL - 3 | part I
    agent1 = Image.open(f'assets/agents/{top_agent1["name"]}.png')
    agent1.thumbnail((35, 35), Image.ANTIALIAS)
    canvas.paste(agent1, (26, 234))

    agent2 = Image.open(f'assets/agents/{top_agent2["name"]}.png')
    agent2.thumbnail((35, 35), Image.ANTIALIAS)
    canvas.paste(agent2, (26, 274))

    agent3 = Image.open(f'assets/agents/{top_agent3["name"]}.png')
    agent3.thumbnail((35, 35), Image.ANTIALIAS)
    canvas.paste(agent3, (26, 314))

    # agent type
    agent_type1 = Image.open(f'assets/roles/{top_agent1["role"]}.png')
    agent_type1.thumbnail((19, 19), Image.ANTIALIAS)
    canvas.paste(agent_type1, (80, 243))

    agent_type2 = Image.open(f'assets/roles/{top_agent2["role"]}.png')
    agent_type2.thumbnail((19, 19), Image.ANTIALIAS)
    canvas.paste(agent_type2, (80, 282))

    agent_type3 = Image.open(f'assets/roles/{top_agent3["role"]}.png')
    agent_type3.thumbnail((19, 19), Image.ANTIALIAS)
    canvas.paste(agent_type3, (80, 323))

    # PILL - 3 | part II
    draw.text((118, 240), top_agent1['name'],
              fill='#ffffff', font=open_bold_ss)
    draw.text((118, 280), top_agent2['name'],
              fill='#ffffff', font=open_bold_ss)
    draw.text((118, 320), top_agent3['name'],
              fill='#ffffff', font=open_bold_ss)

    draw.text((263, 240), top_agent1_stats,
              fill='#ffffff', font=open_bold_ss)
    draw.text((263, 280), top_agent2_stats,
              fill='#ffffff', font=open_bold_ss)
    draw.text((263, 320), top_agent3_stats,
              fill='#ffffff', font=open_bold_ss)

    image = BytesIO()
    canvas.save(image, 'PNG', quality=500)
    image.seek(0)
    return image
