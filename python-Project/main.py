import os
import

new_dir = input('please input dir name:')
if os.path.exists(f'os.getcwd()/{new_dir}')==False:
    os.mkdir(new_dir)

else:
    print('this dir is exists!!!')
os.chdir(new_dir)
pwd = os.getcwd()
print(f'you are now at {pwd}')
new_file = input('please input file name:')
f = open(fr"{pwd}\{new_file}",'a+')
f.write('nihao')
print(f'you just have create a new file {new_file} and add something to it!!')
nf = f.read()

print(nf)