import itertools
import random
from operator import itemgetter
from typing import List, Tuple

from .logger import error, log
from .player import Other
from .timeout import Timeout
from .core.deck import Deck, draw, flop, init, shuffle
from .core.game import ActivePlayer, Game, GameState, Player, PlayerGameStatus
from .core.madehands import evaluate
from .core.player import Player as MetaPlayer


PROCESS = [
    GameState.bet,
    GameState.flop,
    GameState.flop,
    GameState.flop,
    GameState.bet,
    GameState.flop,
    GameState.bet,
    GameState.flop,
    GameState.bet
]

STARTING_CHIPS, MIN_BET_AMT = 200, 1

MIN_NR_OF_WINNERS = 2
MAX_NR_OF_TURNS = 100


def get_chip(player: Player):
    return player.chips


def main(players: List[MetaPlayer]):
    players = [
        Player(
            p,
            STARTING_CHIPS
        ) for p in players
    ]

    t = 1
    while len(players) > MIN_NR_OF_WINNERS and t < MAX_NR_OF_TURNS:
        players = run(t, players)
        t += 1

        players = [p for p in players if p.chips > 0]
        random.shuffle(players)

    # TODO: ON GAME FINISHED
    sorted_players = sorted(players, key=get_chip, reverse=True)
    for p in sorted_players:
        print(f'Player: {p.meta.name} Chips: {p.chips}')


def run(t: int, players: List[Player]) -> List[Player]:
    deck = init()
    deck = shuffle(deck)

    initial_game = Game(
        t,
        deck,
        [
            ActivePlayer(
                p,
                PlayerGameStatus([], 0, False)
            ) for p in players
        ],
        0
    )

    game = players_draw(initial_game); log(game)
    game = players_draw(game); log(game)

    def _run(g: Game, process: List[GameState]) -> List[Player]:
        if process:
            curr = process[0]

            if curr == GameState.flop:
                d = flop(g.deck)

                g = Game(
                    g.round,
                    d,
                    [
                        ActivePlayer(
                            p.player,
                            PlayerGameStatus(
                                p.status.cards,
                                0,
                                False
                            )
                        ) for p in g.players
                    ],
                    g.acc_chips
                ); log(g)

                return _run(g, process[1:])
            elif curr == GameState.bet:
                g = players_bet(g); log(g)

                left_players = [p for p in g.players if not p.status.died]
                if not left_players:
                    return [p.player for p in g.players]
                elif len(left_players) == 1:
                    winner: ActivePlayer = left_players[0]
                    return [
                        p.player for p in g.players if p.status.died
                    ] + [
                        Player(
                            winner.player.meta,
                            winner.player.chips + g.acc_chips
                        )
                    ]
                else:
                    return _run(g, process[1:])
        else:
            # TODO(sunghyunzz): Handle logging on win
            left_players = {
                k: [p for _, p in v]
                for k, v in itertools.groupby(
                    sorted(
                        (
                            (
                                evaluate(
                                    p.status.cards,
                                    g.deck.community_cards
                                ),
                                p.player
                            ) for p in g.players if not p.status.died
                        ), key=itemgetter(0)
                    ),
                    key=itemgetter(0)
                )
            }

            winners: List[Player] = left_players.pop(max(left_players))

            died = [p.player for p in g.players if p.status.died]

            lost_players: List[Player] = sum(
                (x for x in left_players.values()), []
            )

            return died + lost_players + [
                Player(w.meta, w.chips + (g.acc_chips // len(winners)))
                for w in winners
            ]

    return _run(
        game,
        PROCESS
    )


def players_draw(g: Game) -> Game:

    def _draw(
        d, ps: List[ActivePlayer], acc: List[ActivePlayer]
    ) -> Tuple[Deck, List[ActivePlayer]]:
        if ps:
            c, d2 = draw(d)

            p = ps[0]
            p = ActivePlayer(
                p.player,
                PlayerGameStatus(
                    p.status.cards + [c],
                    p.status.bet_amt,
                    p.status.died
                )
            )

            return _draw(d2, ps[1:], acc + [p])
        else:
            return d, acc

    deck, players = _draw(g.deck, g.players, [])
    return Game(g.round, deck, players, g.acc_chips)


def players_bet(g: Game) -> Game:

    def _bet(
        last_bet_amt: int, ps: List[ActivePlayer], acc: List[ActivePlayer]
    ) -> List[ActivePlayer]:
        if ps:
            p = ps[0]
            if p.status.died:
                return _bet(last_bet_amt, ps[1:], acc + [p])

            min_bet_amt = max(last_bet_amt, MIN_BET_AMT) - p.status.bet_amt
            max_bet_amt = min(
                p.player.chips for p in ps + acc if not p.status.died
            )

            try:
                with Timeout(seconds=1):
                    bet_amt = int(
                        p.player.meta.bet(
                            p.player.chips,
                            p.status.cards,
                            [
                                Other(
                                    p.player.chips,
                                    p.status.bet_amt,
                                    p.status.died
                                ) for p in acc
                            ],
                            [
                                Other(
                                    p.player.chips,
                                    p.status.bet_amt,
                                    p.status.died
                                ) for p in ps[1:]
                            ],
                            g.deck.community_cards,
                            min_bet_amt,
                            max_bet_amt,
                            g.acc_chips + sum(
                                p.status.bet_amt for p in ps + acc
                            )
                        )
                    )

                assert max_bet_amt >= bet_amt >= min_bet_amt

                if bet_amt == min_bet_amt:
                    return _bet(
                        last_bet_amt,
                        ps[1:],
                        acc + [
                            ActivePlayer(
                                Player(
                                    p.player.meta,
                                    p.player.chips - bet_amt
                                ),
                                PlayerGameStatus(
                                    p.status.cards,
                                    p.status.bet_amt + bet_amt,
                                    p.status.died
                                )
                            )
                        ]
                    )
                else:
                    return _bet(
                        bet_amt + p.status.bet_amt,
                        ps[1:] + acc,
                        [
                            ActivePlayer(
                                Player(
                                    p.player.meta,
                                    p.player.chips - bet_amt
                                ),
                                PlayerGameStatus(
                                    p.status.cards,
                                    bet_amt,
                                    p.status.died
                                )
                            )
                        ]
                    )
            except AssertionError:
                error(
                    f'{p.player.meta.name} tried to bet {bet_amt} chips. '
                    f'(min: {min_bet_amt}, max: {max_bet_amt})'
                )
                return _bet(
                    last_bet_amt,
                    ps[1:],
                    acc + [
                        ActivePlayer(
                            p.player,
                            PlayerGameStatus(
                                p.status.cards,
                                p.status.bet_amt,
                                True
                            )
                        )
                    ]
                )
            except TimeoutError:
                error(
                    f'{p.player.meta.name} tried to bet, '
                    f'but it took too long!'
                )
                return _bet(
                    last_bet_amt,
                    ps[1:],
                    acc + [
                        ActivePlayer(
                            p.player,
                            PlayerGameStatus(
                                p.status.cards,
                                p.status.bet_amt,
                                True
                            )
                        )
                    ]
                )
            except Exception as e:
                error(
                    f'{p.player.meta.name} tried to bet, '
                    f'but something went wrong ({e.__class__.__name__})!'
                )
                return _bet(
                    last_bet_amt,
                    ps[1:],
                    acc + [
                        ActivePlayer(
                            p.player,
                            PlayerGameStatus(
                                p.status.cards,
                                p.status.bet_amt,
                                True
                            )
                        )
                    ]
                )
        else:
            return acc

    bet_players = _bet(
        0,
        [
            ActivePlayer(
                p.player,
                PlayerGameStatus(
                    p.status.cards,
                    0,
                    p.status.died
                )
            ) for p in g.players
        ],
        []
    )

    return Game(
        g.round,
        g.deck,
        bet_players,
        g.acc_chips + sum(p.status.bet_amt for p in bet_players)
    )


if __name__ == '__main__':
    from . import example

    main(
        [
            MetaPlayer(
                'A',
                example.always_bet
            ),
            MetaPlayer(
                'B',
                example.always_bet
            ),
            MetaPlayer(
                'C',
                example.always_bet
            ),
            MetaPlayer(
                'D',
                example.always_bet
            ),
            MetaPlayer(
                'E',
                example.always_bet
            )
        ]
    )
