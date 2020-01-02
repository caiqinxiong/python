import os
from git.repo import Repo

# 克隆代码
# download_path = os.path.join('code', 'fuck')
# Repo.clone_from('https://gitee.com/wupeiqi/fuck.git', to_path=download_path, branch='master')


import os
from git.repo import Repo

local_path = os.path.join('code', 'fuck')
repo = Repo(local_path)
commit_log = repo.git.log('--pretty={"commit":"%h" ,"author":"%an","%s","date":"%cd"}',date='format:%Y-%m-%d %H:%M')

print(commit_log)

# commit_log = repo.git.log('--pretty={"commit":"%h","author":"%an","summary":"%s","date":"%cd"}', max_count=50,
#                           date='format:%Y-%m-%d %H:%M')
# log_list = commit_log.split("\n")
# real_log_list = [eval(item) for item in log_list]
# print(real_log_list)