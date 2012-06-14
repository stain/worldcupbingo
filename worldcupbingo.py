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

     "Russia": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Russia.svg/2000px-Flag.svg.png",
     "Czech Republic": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_the_Czech_Republic.svg/2000px-Flag.svg.png",
     "Poland": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Poland.svg/2000px-Flag.svg.png",
    "Greece":"http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Greece.svg/2000px-Flag.svg.png",

    "Germany": "http://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/2000px-Flag.svg.png",
    "Portugal": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/2000px-Flag.svg.png",
    "Denmark": "http://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/2000px-Flag_of_Denmark.svg.png",
    "Netherlands": "http://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/2000px-Flag.svg.png",

    "Croatia": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Croatia.svg/2000px-Flag.svg.png",
    "Spain": "http://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Flag_of_Spain.svg/2000px-Flag.svg.png",
    "Italy": "http://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/2000px-Flag.svg.png",
    "Republic of Ireland": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Ireland.svg/2000px-Flag.svg.png",
    "Ukraine": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Ukraine.svg/2000px-Flag.svg.png",
    "England":"http://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_England.svg/2000px-Flag.svg.png",
    "France":"http://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/2000px-Flag.svg.png",
    "Sweden": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Sweden.svg/2000px-Flag.svg.png",

    ## Remaining are leftovers from world cup 2010
    "South Africa": "http://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Flag_of_South_Africa.svg/2000px-Flag.svg.png",
    "Mexico": "http://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/2000px-Flag.svg.png",
    "Uruguay": "http://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Flag_of_Uruguay.svg/2000px-Flag.svg.png",
    "Korea Republic": "http://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/2000px-Flag.svg.png",
    "Argentina": "http://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/2000px-Flag.svg.png",
    "Nigeria": "http://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Flag_of_Nigeria.svg/2000px-Flag.svg.png",
    "Slovenia":"http://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/2000px-Flag.svg.png",
    "United States": "http://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Flag_of_the_United_States.svg/2000px-Flag.svg.png",
    "Algeria": "http://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Flag_of_Algeria.svg/2000px-Flag.svg.png",
    "Ghana":"http://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Flag_of_Ghana.svg/2000px-Flag.svg.png",
    "Serbia":"http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/2000px-Flag.svg.png",
    "Australia": "http://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/2000px-Flag.svg.png",
    "Japan": "http://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/2000px-Flag.svg.png",
    "Cameroon": "http://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Flag_of_Cameroon.svg/2000px-Flag.svg.png",
    "New Zealand": "http://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Flag_of_New_Zealand.svg/2000px-Flag.svg.png",
    "Paraguay": "http://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Flag_of_Paraguay.svg/2000px-Flag.svg.png",
    "Slovakia": "http://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Flag_of_Slovakia.svg/2000px-Flag.svg.png",
    "Brazil": "http://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/2000px-Flag.svg.png",
    u"Côte d'Ivoire": "http://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Flag_of_Cote_d%27Ivoire.svg/2000px-Flag.svg.png",
    "Korea DPR": "http://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Flag_of_North_Korea.svg/2000px-Flag.svg.png",
    "Switzerland": "http://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Switzerland.svg/2000px-Flag.svg.png",
    "Honduras": "http://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Flag_of_Honduras.svg/2000px-Flag.svg.png",
    "Chile": "http://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Flag_of_Chile.svg/2000px-Flag.svg.png",
    
}


def getGroups():
    groups = {'A': set(("Russia", "Czech Republic", "Poland", "Greece")),
              'B': set(("Germany", "Portugal", "Denmark", "Netherlands")),
              'C': set(("Croatia", "Spain", "Italy", "Republic of Ireland")),
              'D': set(("Ukraine", "England", "France","Sweden")),

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

