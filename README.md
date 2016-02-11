# Senior Design :boom:

Hanabi is a cooperative game in which players try to create the perfect fireworks show by placing the cards on the table in the right order.

The card deck consists of five different colors of cards, numbered 1–5 in each color. For each color, the players try to place a row in the correct order from 1–5. Sounds easy, right? Well, not quite, as in this game you hold your cards so that they're visible only to other players. To assist other players in playing a card, you must give them hints regarding the numbers or the colors of their cards. Players must act as a team to avoid errors and to finish the fireworks display before they run out of cards.

This project seeks to create an online version of this game, providing the players only the information they may see. 

##Game Pieces

The game pieces are as follows:
- 50 cards consisting of 5 suits, each with:
	- Three 1's
	- Two 2's
	- Two 3's
	- Two 4's
	- One 5
- 12 Tokens:
	- 8 Blue Clock Tokens
	- 3 Black Fuse Tokens
	- 1 Black Explosion Token

A clock token is lost when a player uses their turn to give another player a piece of information. A clock token can be regained if a player uses their turn to discard a card.

A fuse token is lost when a player plays a card that is not a valid move at that point. When all fuse tokens have been lost, an invalid move results in losing the black explosion token. When this token is lost, the game is over and the players have lost.

##Rules

On their turn, a player has three options:
- Play a card from their hand
- Discard a card from their hand
- Give another player information

At the end of their turn, a player must have four (4) cards in their hand.

###Playing a Card

On their turn, a player may play a card from their hand. 
A move is valid if it is the next number in sequence of a color on the board.
For example, a player my place a red '1' if the red sequence has not been started.
If a blue '1' has been played, a player may place a blue '2' to continue that sequence.

If an invalid move is made, one fuse token is removed from play. 

###Discarding a Card

On their turn, a player may discard a card from their hand. 
This earns back one information token that has been spent.
The number of information tokens may not exceed eight (8).

#####Discard Pile

When a player discards a card from their hand, it enters the discard pile.
Discarded cards remain visible to all players for the remainder of the game.
This allows players to track what cards are still in play and determine moves.

###Giving Information

On their turn, a player may give another player a piece of information.
Valid information is either the color or number of a card or cards in their hand.

For example, given the following hand:

[(Red 1), (Blue1), (Red 2), (Green 4)]

Valid information could be any of the following:
- Cards 1 and 3 are Red
- Cards 1 and 2 are '1'
- Card 1 is Red
- Card 1 is '1'
- Card 2 is Blue
- Card 2 is '1'
- Card 3 is Red
- Card 3 is '2'
- Card 4 is Green
- Card 4 is '4'

Information for multiple cards can only be about what is common between the cards.


###Completing a sequence

When a sequence of cards is completed (1 to 5 played in the same color), a clock token is earned.
This number still may not exceed eight (8).

##End Game

The game has three (3) scenarios to end the game:
- The Explosion token is lost
- Each color sequence has been completed
- There are no more cards in the draw pile

###Explosion Token Lost

One way for the game to end is for the Explosion Token to be lost. 
This occurs when the players have made a total of four (4) invalid plays.
When this occurs, the game ends and the players have lost and they should feel bad.

###Color Sequences Completed

The victory condition is that all color sequences have been completed.
This means each of the five (5) colors has been laid out from 1 to 5 on the board.
If this happens, the players have won and they should feel good about themselves.

###Draw Pile Exhausted

If a player takes the last card out of the draw pile, each player receives one (1) more turn.
At this point, any player can effectively figure out what four cards they have based on what other players have, what is already played, and what has been discarded.
Because players can determine their cards, each player is only given one more turn to complete the sequences.
If any sequence remains incomplete after the final turn, they players have lost but only barely, so they don't have to feel bad.


