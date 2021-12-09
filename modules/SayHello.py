class SayHello:
    def __init__(self, target="World"):
         self.targe=target

    def say(self):
        print(f"Hello, {self.target}!!")
if __name__ == '__main__':
    app = SayHello()
    app.say()
    app = SayHello("Someone")
    app.say()