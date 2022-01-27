from random import randint
class Gambler:
    def __init__(self, stake, goal):
        self.stake = stake
        self.goal = goal
        
        win = 0
        loss = 0
        bet = 0
        while stake < goal and stake > 0:
            if randint(0,1) == 0:
                loss+=1
                stake-=1
                bet+=1
            else:
                win+=1
                stake+=1
                bet+=1
        print("Sum : {}, Win : {}, Loss : {}, No. of Bets : {}".format(stake, win, loss, bet))

stake = input('Enter the Stake : ')
goal = input('Enter the Goal : ')
Gambler(int(stake),int(goal))