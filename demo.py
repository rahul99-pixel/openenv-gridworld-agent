from env import OpenEnv

env = OpenEnv()
state = env.reset()
done = False

print("Starting Demo...\n")

while not done:
    env.render()
    
    # Simple policy: move right (3) then down (1)
    if state[1] < env.size - 1:
        action = 3
    else:
        action = 1

    state, reward, done, _ = env.step(action)

print("\nGoal Reached!")
