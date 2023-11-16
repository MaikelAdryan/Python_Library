# pip install tqdm
from tqdm import tqdm
from time import sleep

def method_one():
  for i in tqdm(range(10)):
    sleep(1)


def method_two():
  list = [1, 2, 3, 4, 5, 10]
  for item in tqdm(list):
    sleep(1)


def method_three():
  steps = 100
  with tqdm(total=steps) as progress_bar:
    for i in range(steps):
      sleep(0.1)
      progress_bar.update(1)


# method_one()
# method_two()
method_three()
