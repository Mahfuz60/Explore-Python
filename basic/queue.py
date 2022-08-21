# first in first out
from collections import deque

bank=deque(["Mahfuz","hridoy","chamak","dollar","rafsan"])
print(bank)
bank.popleft()
print(bank)


# check empty customer
if not bank:
    print("Customer service not available")