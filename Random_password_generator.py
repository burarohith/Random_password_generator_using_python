import random
import string

lenth = int(input('enter the length of password'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symobls = string.punctuation

all = lower + upper + num +symobls

temp = random.sample(all,lenth)
password = "".join(temp)
print(password)
