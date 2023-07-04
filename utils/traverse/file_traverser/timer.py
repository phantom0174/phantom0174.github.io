from time import perf_counter

class Timer:
    times = []

    def toggle(self):
        self.times.append(perf_counter())

        if len(self.times) != 2:
            return 
    
        duration = self.times[1] - self.times[0]
        self.times.clear()

        return duration * 1000  # to ms
