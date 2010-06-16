#!/usr/bin/env python
# -*- coding: utf8 -*-

import random
import sys
import hashlib

DEFAULT_BINGOS=1
DEFAULT_ROWS=4
DEFAULT_COLUMNS=3
DEBUG=False

def getGroups():
    groups = {'A': set(("South Africa", "Mexico", "Uruguay", "France")),
              'B': set(("Korea Republic", "Argentina", "Nigeria", "Greece")),
              'C': set(("Slovenia", "United States", "England", "Algeria")),
              'D': set(("Germany", "Ghana", "Serbia", "Australia")),
              'E': set(("Netherlands", "Japan", "Cameroon", "Denmark")),
              'F': set(("New Zealand", "Paraguay", "Italy", "Slovakia")),
              'G': set(("Brazil", u"Côte d'Ivoire", "Portugal", "Korea DPR")),
              'H': set(("Spain", "Switzerland", "Honduras", "Chile")),
             }
    allTeams = set()         
    longestTeamName = 0
    teams = {}
    for group in groups:
        for team in groups[group]:
            teams[team] = group 
            longestTeamName = max(longestTeamName, len(team))
    return groups,teams,longestTeamName

def main(cmd,bingos=DEFAULT_BINGOS,rows=DEFAULT_ROWS,columns=DEFAULT_COLUMNS,*args):
    if "-h" in args or "--help" in args:
        help(cmd)
        return
    if "-d" in args:
        global DEBUG
        DEBUG=True    
    print """<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <style type="text/css">
    <!--
    table {
        width: 100%;
        height: 28em;
        border-collapse: collapse;
        border-style: solid;
        border-color: gray;
        border-width: 1px;
    }
    td {  
        width: 33%;
        border: black 1px dotted;
        border-color: gray;
        margin: 0;
        text-align: center;
    }
    tr {
        height: 25%;
    }
    h1 {
        page-break-before: always;
    }
    .rules {
        font-size: 90%;
    }
    .hash {
        font-size: 90%;
        text-align: right;
    }


    -->
    </style>
</head>
    <body>
"""
    for n in range(int(bingos)):
        print """<div class='bingo'>
          <h1>FIFA World Cup 2010 Bingo</h1>
          <p>Cross out teams below as they are eliminated from the World Cup.
          The first player to complete his bingo board wins.</p>
          <ul>
          <li>The ordering is based on the time the matches are
          played.</li>
          <li>In the event of a tie, the board with the team which 
          eliminating match was played first will win.</li>
          <li>The third-place game is not included. </li>
          </ul>

          <p>This board has been computationally drawn randomly
         according to these rules:</p>
         <ol class='rules'>
            <li>The first team is chosen randomly.</li>
            <li>The whole group of the chosen team is removed from the
                pool of teams, choosing randomly from the remaining
                teams.</li>
            <li>This continues until there are no more possible teams.</li>
            <li>When there are no more possible teams, all teams not
                already on the bingo board are put back to the pool, 
                and the draws continues from the top, until the 
                board is complete.</li>  
            <li>This draw is performed independently for each bingo
            board. Although theoretically two bingo boards could contain
            the same teams, for all practical purposes bingo boards will
            be unique, and will contain teams evenly drawn from across
            the groups.</li>   
         </ol>
        """
        generateBoard(int(rows), int(columns))
        print "</div>"
    print "</body></html>"
    
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

    format = "%%-%ss" % longestTeamName
    if DEBUG:
        board.sort()
    print "<table>"    
    for row in range(rows):
        print "  <tr>"
        for column in range(columns):
            team = board[row*columns + column]
            print "      <td>%s</td>" % team.encode("utf8")
            #print format % team,    
        print "  </tr>"
    print "</table>"        

    boardHash = hashlib.sha1()
    board.sort()
    for t in board:
        boardHash.update(t.encode("utf8"))
    print "<div class='hash'>Board id %s</div>" % boardHash.hexdigest()


def help(cmd):
    print """%s [bingos] [columns] [rows]
Generate a FIFA 2010 World Cup bingo.

  bingos  - number of bingo boards to generate. Default: %s
  rows    - number of rows on bingo board. Default: %s
  columns - number of columns on bingo board: Default %s
""" % (cmd, DEFAULT_BINGOS, DEFAULT_ROWS, DEFAULT_COLUMNS)


if __name__ == "__main__":
    main(*sys.argv)

