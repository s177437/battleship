class Scorestat():
    scoredict = {}

    def set_scoredict(self, value):
        """
        :param value:
        Function to set scorevalues
        """
        self.scoredict = value

    def get_scoredict(self):
        """
        :return scoredict:
        Get function for score stats.
        """
        return self.scoredict

    def update_score_stats(self, boardnumber, boardlocationid):
        """
        :param boardnumber:
        :param boardlocationid:
        Function to update score stats with a new boatid.
        """
        scoredict = self.get_scoredict()
        if boardnumber in scoredict:
            scoredict[boardnumber].append(boardlocationid)
        else:
            scoredict[boardnumber] = [boardlocationid]
        self.set_scoredict(scoredict)

    def check_for_winner(self,playerlist):
        """
        :return:
         Function that is performed after every move to count the number of bombed boats for a board. When the number
         reaches nine. All boats are bombed in a board.
        """
        scoredict = self.get_scoredict()
        player=""
        for key, value in scoredict.iteritems():
            if len(value) == 9:
                if key =="board0" :
                    player=playerlist[0]
                else:
                    player=playerlist[1]
                print ("We have a winner: " + player.upper() + " who took out the following boats: " + str(value))
                exit(0)
