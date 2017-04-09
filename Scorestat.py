class Scorestat():
    scoredict = {}

    def set_scoredict(self, value):
        self.scoredict = value

    def get_scoredict(self):
        return self.scoredict

    def updateScoreStats(self, boardnumber, boardlocationid):
        scoredict = self.get_scoredict()
        if boardnumber in scoredict:
            scoredict[boardnumber].append(boardlocationid)
        else:
            scoredict[boardnumber] = [boardlocationid]
        self.set_scoredict(scoredict)

    def checkForWinner(self):
        scoredict = self.get_scoredict()
        for key, value in scoredict.iteritems():
            if len(value) == 9:
                print "We have a winner", key, value
                exit(0)
