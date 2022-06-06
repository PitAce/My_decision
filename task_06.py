class WrongNumberOfPlayersError(Exception):
    pass
class NoSuchStrategyError(Exception):
    pass
    
def rps_game_winner(game_m):
    win1, win2 = ['PP', 'PR', 'SP', 'SS', 'RS', 'RR'], ['PS', 'SR', 'RP'] # winning moves
    
    game_move = ''
    for i in game_m:
        game_move += i[1]

    if len(game_move) > 2:
        raise WrongNumberOfPlayersError
    elif game_move in win1:
        return(' '.join(game_m[0]))
    elif game_move in win2:
        return(' '.join(game_m[1]))
    else:
        raise NoSuchStrategyError
