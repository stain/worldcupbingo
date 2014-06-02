# FIFA World Cup 2014 bingo

Generate bingo cards for the [FIFA World Cup](http://www.fifa.com/worldcup/index.html) 2014.

Cross out teams as they are *eliminated* from the World Cup. The first player to complete their bingo card wins.

## Card generation

The card (see [example bingo card](http://stain.github.com/worldcupbingo/bingo.html)) is drawn randomly according
to these rules:

1.   The first team is chosen randomly.
2.   The *group* of the chosen team is removed from the pool of possible teams.
3.   The next team is chosen randomly from the remaining teams.
4.   This continues from step 2 until there are no more possible teams.
5.   When there are no more possible teams, remaining teams not already on the bingo card are put back into the pool, and the process continues from step 1 onwards until the card is complete.
6.   This draw is performed independently for each bingo card. Although theoretically two bingo boards could contain the same teams, for all practical purposes bingo boards will be unique, and will contain teams evenly drawn from across the groups.

This rota between the groups helps ensure that all cards contain a mixture of
'good' and 'not so good' team, so that it is not easy to predict in advance who
will win.


There is a small chance that several boards would contain the same teams (but
possibly printed in a different order). The size of the board has been
optimized to 3x4 as a trade-off between the whole bingo game finishing too
early and adding some excitement towards the end game.  From our experience,
the winner(s) will typically be in the quarter finals if about 30-40 cards are
being played.

## Playing

This game is most fun playing in a shared space, like an office or lunch room,
so that one can track progress on each other's cards: 

1. Generate the required number of bingo boards. Save the HTML file somewhere for later. You can
   email it to independent witnesses who should also monitor and verify that
   you ran the generation without modifications to script or HTML.
2. Print out the bingo boards (the stylesheet will split it over several
   pages). Don't worry, you can print more later! 
3. Sell tickets to the bingo draw to your colleages, and let the purchaser pick
   a card without looking at its content. (So she can't prefer the "best" card!)
4. Write down separately the player's name against the board ID. It is
   usually unique enough so you only need to write down the first 4-5 digits.
5. Write the name of the player on the board, and put it on a bulletin board next
   to the other player's cards.
6. As the World Cup progresses, players will tick off their losing teams
   (cheering for everyone on their board to lose early).
7. The winner(s) are the first player(s) to complete their board. Note that this
   is ordered by the scheduled kickoff time of World Cup matches - not by when
   the board is ticket. Thus, if one night Brazil first wins over Germany, and
   2 hours later, Italy wins over France, then the player which only unticked
   box was "Brazil" will win, while the player missing just "Italy" will not
   win.  On the other hand, if two concurrent matches have kick off at 18:00,
   then bingo winners resulting from both matches are in a tie.
   
## Deciding the winner


1. The ordering is based on the scheduled kickoff date and time of the
   eliminating matches (at the final groups stage, the final match of the
   group)
2. In the event of several players completing their bingo card after the same
   elimination, they will share the prize.
3. The third-place game is not included.


## Usage

    $ python worldcupbingo.py > bingo.html

Then open in a browser to print the card.

    $ gnome-open bingo.html


You can print as many cards as you like, at any time, as each card is generated independently. 
To generate many cards in one go (printed on separate pages), add the number of cards as a parameter:

    $ python worldcupbingo.py 30 > bingo.html

If you are not able to run the generation script, you can always use our 
pre-made [100 cards](http://stain.github.io/worldcupbingo/hundreds.html) - but
only print it once - do not sell duplicates!

## Customization

Modify these settings within [worldcupbingo.py](worldcupbingo.py) to change the
number of teams on a board or the price per board.

```python
DEFAULT_ROWS=4
DEFAULT_COLUMNS=3
DEFAULT_PRICE="£2/board"
```

To modify the generation for a different cup, edit `getGroups()` to reflect the 
teams. You may need to add additional flags from Wikipedia to `flags = ...`
above.  You should also modify [div.html](div.html) for the new name of the cup.

# Authenticity

To verify that players have not printed their own card with more favourable
teams, you are advised to keep a copy of the generated HTML and make not of
the mapping between the *Board ID* and the player.

The Board ID is generated as a SHA-1 hash of the alphabetically sorted list of
teams on the board (as UTF-8), separated with newlines (`\n`). 

# Authors and license

(c) 2010-2014 
  [Stian Soiland-Reyes](http://orcid.org/0000-0001-9842-9718), 
  [Matthew Gamble](http://orcid.org/0000-0003-4913-1485)

Licensed under the [MIT license](LICENSE).


