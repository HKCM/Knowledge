

### 描述: shell脚本中提示用户确认操作

#### 例1：确认提示（一次）
这个示例代码将为确认提示一次，如果你给输入错误，程序会以状态1退出。这个例子将只接受Y或N或YES或NO（不区分大小写）。
```Shell
#!/bin/bash

read -r -p "Are You Sure? [Y/n] " input

case $input in
    [yY][eE][sS]|[yY])
		echo "Yes"
		;;

    [nN][oO]|[nN])
		echo "No"
       	;;

    *)
		echo "Invalid input..."
		exit 1
		;;
esac
```

#### 例2：提示进行确认（输入正常退出，输入错误则需重新输入）
```Shell
#!/bin/bash

while true
do
	read -r -p "Are You Sure? [Y/n] " input

	case $input in
	    [yY][eE][sS]|[yY])
			echo "Yes"
			exit 1
			;;

	    [nN][oO]|[nN])
			echo "No"
			exit 1	       	
			;;

	    *)
			echo "Invalid input..."
			;;
	esac
done
```

