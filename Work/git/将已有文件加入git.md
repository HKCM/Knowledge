已存在的文件夹
```shell
cd existing_folder
git init
git config user.name 'karl'
git config user.email 'None'
git config --list
git remote add origin <giturl>
# git remote remove <name>
# git remote remove origin

git add .
git commit -m "message"
git push -u origin master
```
已存在的 Git 版本库
```
cd existing_repo
git remote rename origin old-origin
git remote add origin http://gitlab.xfyun.cn/jbchen6/cicd.git
git push -u origin --all
git push -u origin --tags
```
