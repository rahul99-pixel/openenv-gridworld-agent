import numpy as np
import random
from env import OpenEnv

env = OpenEnv()

q_table = np.zeros((env.size, env.size, 4))

episodes = 500
alpha = 0.1
gamma = 0.9
epsilon = 0.2

for ep in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 3)
        else:
            action = np.argmax(q_table[state[0], state[1]])

        next_state, reward, done, _ = env.step(action)

        old_value = q_table[state[0], state[1], action]
        next_max = np.max(q_table[next_state[0], next_state[1]])

        new_value = old_value + alpha * (reward + gamma * next_max - old_value)
        q_table[state[0], state[1], action] = new_value

        state = next_state
        total_reward += reward

    if (ep + 1) % 100 == 0:
        print(f"Episode {ep+1}, Total Reward: {total_reward}")

print("\nTraining Complete!")
