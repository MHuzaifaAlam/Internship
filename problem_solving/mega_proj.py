class Task:
    def __init__(self,title):
        self.title=title
        self.done=False

    def mark_done(self):
        self.done=True

    def __str__(self):
        if self.done:
            return f" [x] {self.title} "
        else:
            return f"[] {self.title}"
        
t1=Task("Buy grocries")
print(t1)
t1.mark_done()
print(t1)
