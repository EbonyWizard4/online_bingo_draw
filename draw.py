import numpy as np

numbers_lucky = []
def draw():
    number_draw = 45
    for number in range(number_draw):
        num_lucky = np.random.randint(1, 75)
        if num_lucky in numbers_lucky:
            pass
        else:
            numbers_lucky.append(num_lucky)
    print(numbers_lucky)

draw()

