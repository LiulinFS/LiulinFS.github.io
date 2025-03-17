import os
import git

# 设置本地仓库路径
local_repo_path = "E:/MyBlog"

# GitHub 仓库地址
remote_repo_url = "https://github.com/LiulinFS/LiulinFS.github.io.git"

# 确保本地目录是一个 Git 仓库
if not os.path.exists(os.path.join(local_repo_path, ".git")):
    print("初始化 Git 仓库...")
    repo = git.Repo.init(local_repo_path)
    repo.create_remote("origin", remote_repo_url)
else:
    repo = git.Repo(local_repo_path)

# 添加所有文件
print("添加所有文件到 Git...")
repo.git.add(all=True)

# 提交更改
print("提交更改...")
repo.index.commit("Updated website")

# 设置 main 分支（如果没有的话）
if "main" not in repo.heads:
    repo.create_head("main")

repo.heads.main.checkout()

# 推送到 GitHub
print("推送到 GitHub...")
repo.remote("origin").push(refspec="main:main")

print("🎉 代码已成功上传到 GitHub！")
