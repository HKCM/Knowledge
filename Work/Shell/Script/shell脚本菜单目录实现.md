

### 一个简单shell菜单实现


```shell
#!/bin/bash
clear
cat << EOF
********please enter your choice:(1-6)****
(1) List you selected directory
(2) Change to you selected directory
(3) Create a new file
(4) Edit you selected file
(5) Remove you selected file.
(6) Exit Menu.
EOF
read -p "Now select the top option to: " input
case $input in 
1) ls;;
2) echo "Enter target directory:"
read dir
cd $dir;;
3) echo "Enter a file name:"
read file
touch $file;;
4) echo "Enter a file name:"
read file
vi $file;;
5) echo "Enter a file name:"
read file
rm $file;;
6) echo "Bye"
exit 0;;
*) echo "Invalid input,bye"
exit 1;;
esac
```
也可以通过`while ture` 循环菜单
```shell
while true
do
  cat << EOF
  ********please enter your choice:(1-6)****

  (1) List you selected directory
  (2) Change to you selected directory
  (3) Create a new file
  (4) Edit you selected file
  (5) Remove you selected file.
  (6) Exit Menu.
  EOF
  read -p "Now select the top option to: " input
  case $input in 
  1) ls;;
  2) echo "Enter target directory:"
  read dir
  cd $dir;;
  3) echo "Enter a file name:"
  read file
  touch $file;;
  4) echo "Enter a file name:"
  read file
  vi $file;;
  5) echo "Enter a file name:"
  read file
  rm $file;;
  6) echo "Bye"
  exit 0;;
  *) echo "Invalid input,bye"
  exit 1;;
done
```

#### 菜单函数
```shell
function diskspace {
  clear
  df -k
}

function whoseon {
  clear
  who
}

function memusage {
  clear
  cat /proc/meminfo
}

function menu {
  clear
  echo
  echo -e "\t\t\tSys Admin Menu\n"
  echo -e "\t1. Display disk space"
  echo -e "\t2. Display logged on users" 
  echo -e "\t3. Display memory usage" 
  echo -e "\t0. Exit program\n\n"
  echo -en "\t\tEnter option: "
  read -n 1 option
}

while true; do
  menu
  case $option in
  0) break ;;
  1) diskspace ;;
  2) whoseon ;;
  3) memusage ;;
  *) 
      clear
      echo "Sorry, wrong selection" ;;
  esac
  echo -en "\n\n\t\t\tHit any key to continue"
  read -n 1 line
done
clear
```

### select实现菜单
```shell
#!/bin/bash
function diskspace {
  clear
  df -k
}

function whoseon {
  clear
  who
}

function memusage {
  clear
  cat /proc/meminfo
}

PS3="Enter option: "
# select语句中的所有内容必须作为一行出现
select option in "Display disk space" "Display logged on users" "Display memory usage" "Exit program"

# 存储在变量中的结果值是整个文本字符串而不是跟菜单选项 相关联的数字
# 文本字符串值才是要在case语句中进行比较的内容
do
  case $option in
  "Exit program")
    break ;;
  "Display disk space")
    diskspace ;;
  "Display logged on users")
    whoseon ;;
  "Display memory usage")
    memusage ;;
  *)
    clear
    echo "Sorry, wrong selection" ;;
  esac
done
clear
```

