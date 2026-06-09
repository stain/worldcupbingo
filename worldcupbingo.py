#!/usr/bin/env python3

import random
import sys
import codecs
from string import Template
import requests
import uuid
import json

DEFAULT_BINGOS=1
DEFAULT_ROWS=3
DEFAULT_COLUMNS=3
DEFAULT_PRICE="£2/board"
DEBUG=False

cellTemplate = Template(open("tablecell.html").read())
boardTemplate = Template(open("div.html").read())
boardidsTemplate = Template(open("boardids.html").read())
mainTemplate = Template(open("main.html").read())

with open('flags.json', 'r') as file:
    flags = json.load(file)
    
def getGroups():
    with open('groups.json', 'r') as file:
        gg = json.load(file)
    groups = {}
    for key, teams in gg.items():
        groups[key] = set(teams)
        
    allTeams = set()
    longestTeamName = 0
    teams = {}
    for group in groups:
        for team in groups[group]:
            teams[team] = group
            longestTeamName = max(longestTeamName, len(team))
    return groups,teams,longestTeamName

def main(cmd,bingos=DEFAULT_BINGOS,rows=DEFAULT_ROWS,columns=DEFAULT_COLUMNS,*args):
    if not args:
        price = DEFAULT_PRICE
    else:
        price = " ".join(args)

    boards = ""
    boardids = []
    for n in range(int(bingos)):
        board = generateBoard(int(rows), int(columns))
        boardHtml = boardAsTable(board, int(rows), int(columns))
        boardId = getBoardHash(board)
        boardids.append(boardId)
        boards += boardTemplate.substitute(board=boardHtml,
		boardId=boardId, price=price)
    boardids.sort()
    if (len(boardids) > 1):
        ids = boardidsTemplate.substitute(boardids=
		"\n</p><p>\n".join(boardids))
    else:
        ids = "" # No point for a single board!
    print((mainTemplate.substitute(boards=boards, ids=ids)))

def generateBoard(rows, columns):
    groups,teams,longestTeamName = getGroups()
    needed = rows*columns
    board = []
    candidates = set(teams)
    if (needed > len(candidates)):
        raise Exception("Need %s candidates for board %sX%s, but only %s teams in "\
                "world cup" % (needed,rows,columns,len(candidates)))

    while len(board) < needed:
        team = random.choice(list(candidates))
        board.append(team)
        # Disable candidate's team
        group = teams[team]
        teamsInGroup = groups[group]
        candidates -= teamsInGroup
        if len(candidates) == 0:
            # Bring in again all groups
            candidates = set(teams) - set(board)

    return board

NAMESPACE_WORLDCUP=uuid.UUID("dedaeff9-2834-51b1-afda-9d8e2ea53d38")

def getBoardHash(board):
    s=[]
    board.sort()
    for t in board:
        s.append(t)
    joined = "\n".join(s)
    return str(uuid.uuid5(NAMESPACE_WORLDCUP, joined))

def boardAsTable(board, rows, columns):
    html = "<table>\n"
    for row in range(rows):
        html += "  <tr>\n"
        for column in range(columns):
            team = board[row*columns + column]
            html += "      <td>\n"
            html += cellTemplate.substitute(flag=flags[team], team=team)
            #print "<object data='%s' type='image/svg+xml' height='100'></object>" % flags[team]
            #print "<img src='%s' /><br />" % flags[team]
            #print team.encode("utf8")
            html += "</td>"
            #print format % team,
        html += "  </tr>"
    html += "</table>"
    return html

def checkFlags():
    _,teams,_ = getGroups()
    for team in teams.keys():
        flags.get(team)
    for country,flag_url in list(flags.items()):
        r = requests.get(flag_url)
        status = "✓" if r.status_code == requests.codes.ok else "✗"
        print(("%s - %s" % (country, status)))

def help(cmd):
    print(("""%s [bingos] [columns] [rows] [price]
Generate a World Cup 2026 bingo card.

  bingos  - number of bingo boards to generate. Default: %s
  rows    - number of rows on bingo board. Default: %s
  columns - number of columns on bingo board: Default %s
  price   - price to print on card: Default %s
""" % (cmd, DEFAULT_BINGOS, DEFAULT_ROWS, DEFAULT_COLUMNS, DEFAULT_PRICE)))


if __name__ == "__main__":
    args = sys.argv
    if "-f" in args:
        checkFlags()
        args.remove('-f')
    if "-d" in args:
        DEBUG=True
    if "-h" in args or "--help" in args:
        help(args[0])
    else:
        main(*sys.argv)
