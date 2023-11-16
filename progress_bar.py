# pip install tqdm
from tqdm import tqdm
from time import sleep

def method_one():
  for i in tqdm(range(10)):
    sleep(1)


# method_one()

def method_two():
  list = [1, 2, 3, 4, 5, 10]
  for item in tqdm(list):
    sleep(1)


method_two()
