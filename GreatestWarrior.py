class Warrior:
    def __init__(self, name, level, experience, rank):
        self.name = name
        self.level = level
        self.experience = experience
        self.rank = rank


    def __str__(self):
        return '[Warrior: %s, %s,  %s, %s]' % (self.name, self.level, self.experience, self.rank)


    def ranking (self, rank):
        rank_1 = ['Pushover', 'Novice', 'Fighter', 'Warrior', 'Veteran',
                  'Sage', 'Elite', 'Conqueror', 'Champion', 'Master', 'Greatest']
        self.rank = rank_1.pop(rank)


    def training(self, experience):
        self.experience = int(self.experience + experience)
        self.level = int(self.experience // 100)
        if self.level > 10:
            self.rank = int(self.level // 10)
        else:
            self.rank = 1
        print('Defeated Chuck Norris')
        self.ranking(self.rank)


    def battle(self, level):
        if level <= 100:
            if self.level == level:
                self.experience = int(self.experience+10)
                print('a good fight')
            elif (self.level - level) == 1:
                self.experience = int(self.experience+5)
                print('a good fight')
            elif (self.level - level) >= 2:
                print('easy fight')
            elif -5 < (self.level - level) < 0:
                self.experience = int(self.experience + 20*int(level - self.level)**2)
                print('an intence fight')
            elif (self.level - level) < -5:
                print('you loose')
        else:
            print('inavalid level')
        self.level = int(self.experience // 100)
        if self.level > 10:
            self.rank = int(self.level // 10)
        else:
            self.rank = 1
        self.ranking(self.rank)


class FellowFighter(Warrior):
    def __init__(self, name, level, experience, rank):
        Warrior.__init__(self, name, level, experience, rank)


class Fighter(Warrior):
    def __init__(self,  name, level, experience, rank):
        Warrior.__init__(self, name, level, experience, rank)


if __name__ == '__main__':
    bruce_lee = Warrior('Bruce Lee', 1, 100, 0)
    bruce_lee.ranking(bruce_lee.rank)
    print(bruce_lee)
    print ('let start the training')
    print ('your fellow fighter is Chuck Norris')
    chuck_norris = FellowFighter ('Chuck Norris', 1, 100, 1)
    chuck_norris.ranking(chuck_norris.rank)
    print(chuck_norris)
    bruce_lee.training(chuck_norris.experience)
    print(bruce_lee)
    van_dam = Fighter('Van Dam', 1, 700, 1)
    van_dam.ranking(van_dam.rank)
    print('fight with Van Dam')
    print(van_dam)
    bruce_lee.battle(van_dam.level)
    print(bruce_lee)