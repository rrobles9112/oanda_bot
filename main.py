from oanda_bot import Bot

class MyBot(Bot):
    def strategy(self):
        fast_ma = self.sma(period=5)
        slow_ma = self.sma(period=25)
        # golden cross
        self.sell_exit = self.buy_entry = (fast_ma > slow_ma) & (
            fast_ma.shift() <= slow_ma.shift()
        )
        # dead cross
        self.buy_exit = self.sell_entry = (fast_ma < slow_ma) & (
            fast_ma.shift() >= slow_ma.shift()
        )


if __name__ == '__main__':
    MyBot(
        account_id='101-011-13291497-002',
        access_token='7c743f29b9cd0554b794f741a4c65ca7-4cace56fcf2c67ed8a5822d8eea9512b',
    ).run()