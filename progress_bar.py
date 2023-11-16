# pip install tqdm
from tqdm import tqdm
from time import sleep

def method_one():
  for i in tqdm(range(10)):
    sleep(1)


method_one()
