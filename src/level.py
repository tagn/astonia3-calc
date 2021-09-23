from dataclasses import dataclass, field


@dataclass
class PlayerLevel:
    level: int
    total_exp: int = field(init=False)
    exp_to_next: int = field(init=False)

    def __post_init__(self):
        self.total_exp = self.level ** 4
        self.exp_to_next = (self.level + 1) ** 4 - self.total_exp
