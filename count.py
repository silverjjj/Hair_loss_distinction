'''
갯수확인하는 코드
'''
import os, os.path

# # simple version for working with CWD
# print len([name for name in os.listdir('.') if os.path.isfile(name)])

# path joining version for other paths
DIR = './images/test/hair'
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

DIR1 = './images/test/hair_loss'
print(len([name for name in os.listdir(DIR1) if os.path.isfile(os.path.join(DIR1, name))]))