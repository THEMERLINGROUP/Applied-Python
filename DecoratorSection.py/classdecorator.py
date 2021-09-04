class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(self.num_calls)
        return self.func(*args, **kwargs)


@CountCalls
def welcome_user():
    print('Welcome')
welcome_user()
