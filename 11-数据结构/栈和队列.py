# %% [markdown]
# 232. 用栈实现队列
# >尝试使用栈（stack）来实现队列（queue）。

#%%
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = list()
        self.stack2 = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # self.stack1用于接受元素
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # self.stack2用于弹出元素，如果self.stack2为[],则将self.stack1中元素全部弹出给self.stack2
        if self.stack2 == []:
            while self.stack1:
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2 == []:
            while self.stack1:
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack1 == [] and self.stack2 == []

#%%
queue = MyQueue()
queue.push(1)
queue.push(2)
res1=queue.peek()
res2=queue.pop()
queue.empty()
print(res1,res2)
# %%
