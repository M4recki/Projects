from turtle import Turtle

Up = 90
Down = 270
Left = 180
Right = 0

class Snake:

    def __init__(self):
        self.Segments = []
        self.XPosition = -20
        self.CreateSnake()
        self.Head = self.Segments[0]

    def AddSegment(self, position):
            t = Turtle("square")
            t.color("lime")
            t.penup()
            t.goto(position)
            self.Segments.append(t)
            self.XPosition += 20

    def CreateSnake(self):
        for i in range(3):
            self.AddSegment((-20, 0))

        self.Segments[0].color("red")

    def ExtendSnake(self):
        self.AddSegment(self.Segments[-1].position())

    def move(self):
        for SegmentNumber in range(len(self.Segments) - 1, 0, -1):
            NewXCor = self.Segments[SegmentNumber - 1].xcor()
            NewYCor = self.Segments[SegmentNumber - 1].ycor()
            self.Segments[SegmentNumber].goto(NewXCor, NewYCor)
        self.Head.forward(20)

    def up(self):
        if self.Head.heading() != Down:
            self.Head.setheading(Up)

    def down(self):
        if self.Head.heading() != Up:
            self.Head.setheading(Down)

    def left(self):
        if self.Head.heading() != Right:
            self.Head.setheading(Left)

    def right(self):
        if self.Head.heading() != Left:
            self.Head.setheading(Right)
