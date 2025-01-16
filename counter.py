class Counter:
    def __init__(self, countername,max=100):
        self.coutername = countername
        self.count = 0
        self.max = max
        print(f"Counter {countername} created")
        

    def increment(self):
        if self.count < self.max:
            self.count += 1
            print(self.count)
        else:
            print("Counter is full")

    def decrement(self):
        if self.count > 0:
            self.count -= 1
            print(self.count)
        else:
            print("Counter is empty")

    def reset(self):
        self.count = 0
        print(f"counter Reset to {self.count}")
        print(self.count)

    def get_count(self):
        print(self.count)
        return self.count

    def get_max(self):
        print(self.max)
        return self.max
    
    def set_max(self,max):
        self.count = 0
        self.max = max
        print(f"counter max set to {self.max}")

    def set_count(self,count):
        self.count = count
        print(f"counter count set to {self.count}")

    def __str__(self):
        return f"{self.coutername}: {self.count}/{self.max}"
    
first=Counter("first")
first.increment()
first.set_count(50)
first.get_count()
first.get_max()
first.set_max(100)
first.get_max()
first.increment()
first.set_count(50)
first.decrement()
