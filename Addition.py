class Addition:
    def add_No(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.n1, self.n2 = map(int, input("Enter the n1 and n2 value: ").split())

    def sum(self):
        print(f"The sum of a,b,c : {self.a + self.b + self.c}")
        print(f"The sum of n1 and n2 : {self.n1 + self.n2}")

add = Addition()
add.add_No(2, 1, 3)
add.sum()