from percolation import Percolation
import random
import math

class Percolation_Stats:

    def __init__(self, n, trials):
        self.size = n
        self.trials = trials

    def run_trial(self):
        trial = Percolation(self.size)
        samples = [i for i in range(1,self.size**2)]
        random.shuffle(samples)
        p = 0
        while not trial.percolates():
            sample = samples[p]
            trial.open(sample)
            p+=1
        return trial

    def mean(self):
        trials_sum = 0
        for _ in range(self.trials):
            trial = self.run_trial()
            trials_sum += trial.number_of_open_sites()
        return trials_sum/self.trials

    def stddev(self):
        mean = self.mean()
        stdevsum = 0
        for _ in range(self.trials):
            trial = self.run_trial()
            stdevsum += (trial.number_of_open_sites() - mean)**2
        return math.sqrt(stdevsum / (self.trials - 1))

    def confidence_low(self):
        mean = self.mean()
        stddev = self.stddev()
        return(mean - (1.96*stddev/math.sqrt(self.trials)))

    def confidence_high(self):
        mean = self.mean()
        stddev = self.stddev()
        return(mean + (1.96*stddev/math.sqrt(self.trials)))