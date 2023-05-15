#no problem to import when testing your code
from importlib import reload
import math
import logging
import itertools

from Shay_Rozin import bet

reload(logging)
LEVEL = logging.INFO
#LEVEL = logging.DEBUG

logging.basicConfig(level=LEVEL, format="%(levelname)s - %(asctime)s - %(message)s")

class Game:
    class Urn:
        def __init__(self,n,red_balls):
            self.size = n
            self.red_balls = red_balls
            self.next = 0
            self.count = {True:0,False:0}

        def get_next_ball(self):
            assert self.next < self.size, "out of range"
            is_red = self.next in self.red_balls
            self.next += 1
            self.count[is_red] += 1
            return is_red

    def __init__(self, total_tokens, N, K, red1, red2):
        self.tokens = self.total_tokens = total_tokens
        self.N = N
        self.K = K
        self.urn1 = self.Urn(N, red1)
        self.urn2 = self.Urn(N, red2)
        self.cur_iter = 0

    def get_urn(self, is_first):
        res_urn = self.urn1 if is_first else self.urn2
        return res_urn

    def get_ball(self, is_red, is_first, tokens):
        cur_urn = self.get_urn(is_first)
        assert tokens >=1 and tokens <= self.tokens , "bad bet: tokens {} self.tokens {}".format(tokens, self.tokens)
        return cur_urn.get_next_ball()

    def run(self):
        logging.debug("Starting tokens={} N={} K={}".format(self.tokens, self.N, self.K))
        while self.cur_iter < 2*self.N and self.tokens > 0:
            self.cur_iter += 1
            bet_tokens, is_first, bet_is_red = bet(self.N, self.K, self.tokens,
                                                   self.urn1.count[False], self.urn1.count[True],
                                                   self.urn2.count[False], self.urn2.count[True])
            cur_urn = self.get_urn(is_first)
            result_is_red = self.get_ball(bet_is_red, is_first, bet_tokens)
            bet_factor = 1 if result_is_red == bet_is_red else -1
            self.tokens += bet_factor*bet_tokens
            bet_urn="1" if is_first else "2"
            bet_color="r" if bet_is_red else "g"
            res="r" if result_is_red else "g"
            logging.debug("{:-3}: [{},{}],[{},{}] {}=>{} ({}) left: {}".format(self.cur_iter,
                                                                       self.urn1.count[False], self.urn1.count[True],
                                                                       self.urn2.count[False], self.urn2.count[True],
                                                                       bet_color + bet_urn, res + bet_urn, bet_tokens,
                                                                       self.tokens))
        logging.debug("Finished with {}".format(self.tokens))
        return self.tokens

#Note that this function support small values of N as it runs over all combinations
def get_worst_case(M, N, K):
    assert N < 10, "only small values of N are supported"
    min_val = math.inf
    for sub1 in itertools.combinations(range(N),K):
        for sub2 in itertools.combinations(range(N),N-K):
            for pair in [(sub1,sub2), (sub2,sub1)]:
                min_val = min(min_val, Game(M, N, K, pair[0], pair[1]).run())

    logging.info(f"M:{M}, N:{N}, K:{K} - {min_val}")
    return min_val

if __name__ == '__main__':
    get_worst_case(1000, 5, 3)
