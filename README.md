# UEFA EURO 2016 knockout bingo

Generate bingo cards for the [UEFA European Championships 2016](http://www.uefa.com/uefaeuro/index.html).

Cross out teams as they are *eliminated* from the Euros. The first player to complete their bingo card wins.

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="http://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">worldcupbingo.py</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://orcid.org/0000-0001-9842-9718" property="cc:attributionName" rel="cc:attributionURL">Stian Soiland-Reyes</a> 
<a property="cc:attributionName" rel="cc:attributionURL" href="https://github.com/stain/worldcupbingo/graphs/contributors">et al.</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/stain/worldcupbingo" rel="dct:source">https://github.com/stain/worldcupbingo</a>.

If you are not able to run this generation script, you can always use our
[pre-made 100 bingo cards](https://rawgit.com/stain/worldcupbingo/master/hundreds.html) - but
only print it once - do not sell duplicates!

## Card generation

The card (see [example bingo card](https://rawgit.com/stain/worldcupbingo/master/example.html)) is drawn randomly according
to these rules:

1.   The first team is chosen randomly.
2.   The *group* of the chosen team is removed from the pool of possible teams.
3.   The next team is chosen randomly from the remaining teams.
4.   This continues from step 2 until there are no more possible teams.
5.   When there are no more possible teams, remaining teams not already on the bingo card are put back into the pool, and the process continues from step 1 onwards until the card is complete.
6.   This draw is performed independently for each bingo card. Although theoretically two bingo boards could contain the same teams, for all practical purposes bingo boards will be unique, and will contain teams evenly drawn from across the groups.

This rota between the groups helps ensure that all cards contain a mixture of
'good' and 'not so good' teams, so that it is not easy to predict in advance who
will win. This also makes it quite unlikely for a 3x4 board to win during the
group stages (~ 0.02%).


There is a small chance that several boards would contain the same teams (but
possibly printed in a different order). The size of the board has been
optimized to 3x4 as a trade-off between the whole bingo game finishing too
early and adding some excitement towards the end game.  From our experience,
the winner(s) will typically be in the early quarter finals if about 40 cards are
being played.

## Playing

This game is most fun playing in a shared space, like a lunch room,
so that everyone can track progress on each other's cards.

1. Generate the required number of bingo boards. Save the HTML file somewhere for later. You can
   email it to independent witnesses who should also monitor and verify that
   you ran the generation without modifications to script or HTML.
2. Print out the bingo boards (the stylesheet will split it over several
   pages).  Don't worry if you run out, you can print more later!
3. Sell tickets to the bingo draw to your colleagues, and let the purchaser pick
   a card without looking at its content. (So she can't prefer the "best" card!).
   * You may allow fresh players to "buy in" even if the game has started.
   * If you allow multiple cards for the same player, then you should only
   allow this in a single purchase (so that the player cannot inspect which
   teams he got on his first board before opting to buy a second board)
4. Write down separately the player's name against the board ID. It is
   usually unique enough so you only need to match the first 4-5 digits.
   The first page contains a list of the generated board IDs which should be
   kept by the organizer for this purpose.
5. Write the name of the player on the board, and put it on a bulletin board next
   to the other player's cards. (In a multi-site setup, you can instead choose to
   publish the generated HTML on the Intranet)
6. As the competition progresses, players will tick off their losing teams
   (cheering for everyone on their board to drop out of the World Cup!).
7. The winner(s) of the bingo are the first player(s) to complete their board
   according to their team's knockout. It is not the time of the
   physical completion of the board that matters (you do not need to arrive superearly
   to work to complete the board!), but which team was eliminated first.
   (See below)

## Deciding the winner


1. The ordering of eliminations are based on the _scheduled kickoff time_ of the
   eliminating matches (not when the bingo board is physically completed)
2. The third-place game is not included (those teams were kicked out in the semi-final)
3. In the event of several players completing their bingo card after the same
   team is eliminated, they will equally share the prize.
4. If two concurrent matches have the same scheduled kick off (e.g. in quarter
   finals), then any concurrent bingo winners resulting from either matches are
   considered to be in a tie, which is resolved depending on which way the
   matches finish:

   a) If both matches complete at the end of second half, then both loosing
   teams are considered knocked out at the same time (ignoring the wall clock)
   and the bingo prize is shared.

   b) If any of the matches extend into extra-time, then the loser of the match
   which was extended the least (or not at all) are considered to be knocked
   out earlier.

   c) If both matches extend into penalty kickoffs, then both matches are
   considered to be finished at the same time and the prize is shared; ignoring
   the number of penalty kicks needed for the knockout and any eventual coin
   toss.

5. If the prize is shared according to these rules, it is split equally between
   the winning players, ignoring their number of boards or in which way their
   particular team was eliminated.


## Script usage

```
$ python worldcupbingo.py -h
worldcupbingo.py [bingos] [columns] [rows] [price]
Generate a Euro 2016 bingo.

  bingos  - number of bingo boards to generate. Default: 1
  rows    - number of rows on bingo board. Default: 4
  columns - number of columns on bingo board: Default 3
  prise   - price to print on card: Default £2/board
```

The card is printed on stdout, so redirect to a filename of your choice:

    $ python worldcupbingo.py >bingo.html

Then open in a browser to print the card:

    linux ~ $   gnome-open bingo.html  
    osx ~ $     open bingo.html   
    C:\WINDOWS> start bingo.html

You can print as many cards as you like, at any time, as each card is generated independently.
To generate many cards in one go (printed on separate pages), add the number of cards as a parameter:

    $ python worldcupbingo.py 30 >bingo.html

You can also specify the board size, which might be useful if you are printing particularly few or many cards:


    $ python worldcupbingo.py 1 3 3 "$5/board" >bingo.html

To change the board price, specify it as the last parameter:

    $ python worldcupbingo.py 1 4 4 100 EUR/board >bingo.html

If you are not able to run the generation script, you can always use our
[pre-made 100 bingo cards](http://stain.github.io/worldcupbingo/hundreds.html) - but
only print it once - do not sell duplicates!

## Customization

If you don't want to specify these on the command line every time, you can
modify these settings within [worldcupbingo.py](worldcupbingo.py) to change the
number of teams on a board or the price per board.

```python
DEFAULT_ROWS=4
DEFAULT_COLUMNS=3
DEFAULT_PRICE="£2/board"
```

To modify the generation for a different cup, edit `getGroups()` to reflect the
teams. You may need to add additional flags from Wikipedia to `flags = ...`
above.  You should also modify [div.html](div.html) for the new name of the cup.

Note that the number of rows and columns determines how likely boards are to
overlap, for smaller number of groups you should shrink the board, e.g. for the
Euros use 3x3.

# Authenticity

To verify that players have not printed their own card with more favourable
teams, you are advised to keep a copy of the generated HTML and make note of
the mapping between the *Board ID* and the player. If you generate multiple
cards, the first page will contain a list of the board IDs for this purpose.

The Board ID is generated as a SHA-1 hash of the alphabetically sorted list of
teams on the board (as UTF-8), with trailing newlines (`\n`).

# Authors and license

(c) 2010-2014
  [Stian Soiland-Reyes](http://orcid.org/0000-0001-9842-9718),
  [Matthew Gamble](http://orcid.org/0000-0003-4913-1485)

Licensed under the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/").
