import numpy as np

class OpenEnv:
    def __init__(self, size=5):
        self.size = size
        self.reset()

    def reset(self):
        self.agent_pos = [0, 0]
        self.goal_pos = [self.size - 1, self.size - 1]
        self.obstacles = [(1, 2), (2, 2), (3, 1)]
        self.done = False
        return self.state()

    def state(self):
        return tuple(self.agent_pos)

    def step(self, action):
        if self.done:
            return self.state(), 0, True, {}

        moves = {
            0: (-1, 0),
            1: (1, 0),
            2: (0, -1),
            3: (0, 1)
        }

        move = moves[action]
        new_pos = [
            self.agent_pos[0] + move[0],
            self.agent_pos[1] + move[1]
        ]

        if 0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size:
            self.agent_pos = new_pos

        reward = -1

        if tuple(self.agent_pos) in self.obstacles:
            reward = -10

        if self.agent_pos == self.goal_pos:
            reward = 100
            self.done = True

        return self.state(), reward, self.done, {}

    def render(self):
        grid = np.zeros((self.size, self.size))
        for obs in self.obstacles:
            grid[obs] = -1

        grid[self.goal_pos[0]][self.goal_pos[1]] = 2
        grid[self.agent_pos[0]][self.agent_pos[1]] = 1

        print(grid)
