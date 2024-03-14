#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    returns the name of the player that won
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_game(n):
        primes = get_primes(n)
        game_set = set(range(1, n + 1))

        maria_turn = True
        while True:
            valid_moves = set()
            for prime in primes:
                valid_moves.update(range(prime, n + 1, prime))

            if len(valid_moves.intersection(game_set)) == 0:
                return "Ben" if maria_turn else "Maria"

            move = min(valid_moves.intersection(game_set))
            game_set -= set(range(move, n + 1, move))
            maria_turn = not maria_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
