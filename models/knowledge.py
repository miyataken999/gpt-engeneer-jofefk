from dataclasses import dataclass

@dataclass
class Knowledge:
    data: list = None

    def add(self, data):
        if self.data is None:
            self.data = []
        self.data.extend(data)