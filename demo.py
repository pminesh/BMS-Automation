# progressbar terminal
import time
from tqdm import tqdm
for _ in tqdm(range(20)):
    time.sleep(0.01)