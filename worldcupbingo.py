#!/usr/bin/env python
# -*- coding: utf8 -*-

import random
import sys
import hashlib
from string import Template

DEFAULT_BINGOS=1
DEFAULT_ROWS=3
DEFAULT_COLUMNS=3
DEFAULT_PRICE="£2/board"
DEBUG=False

cellTemplate = Template(open("tablecell.html").read())
boardTemplate = Template(open("div.html").read())
mainTemplate = Template(open("main.html").read())

flags = {
    "South Africa": "http://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Flag_of_South_Africa.svg/2000px-Flag_of_South_Africa.svg.png",
    "Mexico": "http://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/2000px-Flag_of_Mexico.svg.png",
    "Uruguay": "http://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Uruguay.svg/2000px-Flag_of_Uruguay.svg.png",
    "France":"http://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/2000px-Flag_of_France.svg.png",
    "Korea Republic": "http://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/2000px-Flag_of_South_Korea.svg.png",
    "Argentina": "http://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/2000px-Flag_of_Argentina.svg.png",
    "Nigeria": "http://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Flag_of_Nigeria.svg/2000px-Flag_of_Nigeria.svg.png",
    "Greece":"http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Greece.svg/2000px-Flag_of_Greece.svg.png",
    "Slovenia":"http://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/2000px-Flag_of_Slovenia.svg.png",
    "United States": "http://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Flag_of_the_United_States.svg/2000px-Flag_of_the_United_States.svg.png",
    "England":"http://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/2000px-Flag_of_England.svg.png",
    "Algeria": "http://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Flag_of_Algeria.svg/2000px-Flag_of_Algeria.svg.png",
    "Germany": "http://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/2000px-Flag_of_Germany.svg.png",
    "Ghana":"http://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag_of_Ghana.svg/2000px-Flag_of_Ghana.svg.png",
    "Serbia":"http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/2000px-Flag_of_Serbia.svg.png",
    "Australia": "http://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/2000px-Flag_of_Australia.svg.png",
    "Netherlands": "http://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/2000px-Flag_of_the_Netherlands.svg.png",
    "Japan": "http://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/2000px-Flag_of_Japan.svg.png",
    "Cameroon": "http://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Flag_of_Cameroon.svg/2000px-Flag_of_Cameroon.svg.png",
    "New Zealand": "http://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Flag_of_New_Zealand.svg/2000px-Flag_of_New_Zealand.svg.png",
    "Paraguay": "http://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Flag_of_Paraguay.svg/2000px-Flag_of_Paraguay.svg.png",
    "Italy": "http://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/2000px-Flag_of_Italy.svg.png",
    "Slovakia": "http://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Flag_of_Slovakia.svg/2000px-Flag_of_Slovakia.svg.png",
    "Brazil": "http://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/2000px-Flag_of_Brazil.svg.png",
    u"Côte d'Ivoire": "http://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Flag_of_Cote_d%27Ivoire.svg/2000px-Flag_of_Cote_d.svg.png",
    "Portugal": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/2000px-Flag_of_Portugal.svg.png",
    "Korea DPR": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Flag_of_North_Korea.svg/2000px-Flag_of_North_Korea.svg.png",
    "Spain": "http://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/2000px-Flag_of_Spain.svg.png",
    "Switzerland": "http://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Switzerland.svg/2000px-Flag_of_Switzerland.svg.png",
    "Honduras": "http://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Flag_of_Honduras.svg/2000px-Flag_of_Honduras.svg.png",
    "Chile": "http://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Flag_of_Chile.svg/2000px-Flag_of_Chile.svg.png",
    "Denmark": "http://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/2000px-Flag_of_Denmark.svg.png",
    "Croatia": "http://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Flag_of_Croatia.svg/2000px-Flag_of_Croatia.svg.png",
    "Colombia":"http://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Colombia.svg/2000px-Flag_of_Colombia.svg.png",
    "Costa Rica": "http://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Costa_Rica_%28state%29.svg/2000px-Flag_of_Costa_Rica_%28state%29.svg.png",
    "Ecuador":"http://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Flag_of_Ecuador.svg/2000px-Flag_of_Ecuador.svg.png",
    "Bosnia and Herzegovina":"http://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Flag_of_Bosnia_and_Herzegovina.svg/2000px-Flag_of_Bosnia_and_Herzegovina.svg.png",
    "Iran":"http://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Flag_of_Iran.svg/2000px-Flag_of_Iran.svg.png",
    "Belgium":"http://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Flag_of_Belgium.svg/2000px-Flag_of_Belgium.svg.png",
    "Russia":"http://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/2000px-Flag_of_Russia.svg.png",
    "South Korea":"http://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/2000px-Flag_of_South_Korea.svg.png",
    }


def getGroups():

    groups = {'A': set(("Brazil", "Croatia", "Mexico", "Cameroon")),
              'B': set(("Spain", "Netherlands", "Chile", "Australia")),
              'C': set(("Colombia", "Greece", u"Côte d'Ivoire", "Japan")),
              'D': set(("Uruguay", "Costa Rica", "England", "Italy")),
              'E': set(("Switzerland", "Ecuador", "France", "Honduras")),
              'F': set(("Argentina", "Bosnia and Herzegovina", "Iran", "Nigeria")),
              'G': set(("Germany", "Portugal", "Ghana","United States")),
              'H': set(("Belgium", "Algeria", "Russia", "South Korea")),

             }
    allTeams = set()
    longestTeamName = 0
    teams = {}
    for group in groups:
        for team in groups[group]:
            teams[team] = group
            longestTeamName = max(longestTeamName, len(team))
    return groups,teams,longestTeamName

def main(cmd,bingos=DEFAULT_BINGOS,rows=DEFAULT_ROWS,columns=DEFAULT_COLUMNS,price=DEFAULT_PRICE,*args):
    boards = ""
    for n in range(int(bingos)):
        board = generateBoard(int(rows), int(columns))
        boardHtml = boardAsTable(board, int(rows), int(columns))
        boardId = getBoardHash(board)
        boards += boardTemplate.substitute(board=boardHtml,
        boardId=boardId, price=price)
    print mainTemplate.substitute(boards=boards)

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

def getBoardHash(board):
    boardHash = hashlib.sha1()
    board.sort()
    for t in board:
        boardHash.update(t.encode("utf8"))
    return boardHash.hexdigest()


def boardAsTable(board, rows, columns):
    html = "<table>\n"
    for row in range(rows):
        html += "  <tr>\n"
        for column in range(columns):
            team = board[row*columns + column]
            html += "      <td>\n"
            html += cellTemplate.substitute(flag=flags[team], team=team.encode('utf8'))
            #print "<object data='%s' type='image/svg+xml' height='100'></object>" % flags[team]
            #print "<img src='%s' /><br />" % flags[team]
            #print team.encode("utf8")
            html += "</td>"
            #print format % team,
        html += "  </tr>"
    html += "</table>"
    return html

def help(cmd):
    print """%s [bingos] [columns] [rows]
Generate a UEFA 2012 EURO Cup bingo.

  bingos  - number of bingo boards to generate. Default: %s
  rows    - number of rows on bingo board. Default: %s
  columns - number of columns on bingo board: Default %s
""" % (cmd, DEFAULT_BINGOS, DEFAULT_ROWS, DEFAULT_COLUMNS)


if __name__ == "__main__":
    args = sys.argv
    if "-d" in args:
        DEBUG=True
    if "-h" in args or "--help" in args:
        help(args[0])
    else:
        main(*sys.argv)
