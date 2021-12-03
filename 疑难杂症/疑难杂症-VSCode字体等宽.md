

描述: 用VSCode写markdown时,原生字体在中英文字体下不等宽,导致写table时强迫症很难受


解决方案:
1. 下载字体

https://github.com/be5invis/Sarasa-Gothic/releases

分为ttc和ttf:

下载`ttc`格式则安装`ttcsarasa-regular.ttc`

下载`ttf`格式则安装`sarasa-mono-sc-regular.ttf`

2. VSCode设置

因为我只希望markdown使用该字体,所以在当前工作区添加`.vscode/settings.json`文件
![](1.png)

以我的git路径为例

```
vim ~/git/.vscode/settings.json

{
    "[markdown]": {
        "editor.fontFamily": "Sarasa Mono SC"
    }
}
```

3. 重启或重载VSCode

`Command + shift + P` 查找 `Reload Window`

