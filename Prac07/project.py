"""CP1404/CP5632 Practical - Project class example.
Record start doing time: 9:00 a.m.
Completed time: 3:00 p.m.
Estimate using time: 3h 30m
Real using time: 5h
"""
COMPLETED_MAX_PERCENTAGE = 100


class Project:
    def __init__(self, name, start_date, priority, cost, percentage):
        """Initialize the project attitude."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __repr__(self):
        """Output the result."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost}, "
                f"completion: {self.percentage}%")

    def __lt__(self, other):
        """Queuing by priority number."""
        return self.priority < other.priority

    def is_completed(self):
        """Identify whether the project is completed based on percentage."""
        return self.percentage == COMPLETED_MAX_PERCENTAGE
