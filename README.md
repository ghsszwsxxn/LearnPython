## git 命令
git init:初始化一个本地git仓库

git status:查看变动文件

git diff \<file name\>:查看某个文件的变动

git add \<file name\>:增加一个变动文件

git commit -m "":保存一次变动，-m ""为变动增加注释

git log:查看当前分支的历史commit

git push origin 分支名称:将本地一个分支推到远端

git checkout -b branch_name:从当前分支，切一个分支名为branch_name的分支

git branch:查看当前仓库所有分支

git fetch origin:将本地仓库与远程同步

git branch -a:查看远程与本地的所有分支

git branch -d branch_name:删除指定分支

git merge branch_name:将当前分支与远端分支合并