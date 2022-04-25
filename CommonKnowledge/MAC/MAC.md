# MAC
- [MAC](#mac)
  - [检查MAC](#检查mac)
    - [鉴别序列号和配置](#鉴别序列号和配置)
    - [检测屏幕](#检测屏幕)
    - [**声音功能**](#声音功能)
    - [检查电池循环](#检查电池循环)
    - [检测摄像头](#检测摄像头)
    - [硬盘检测](#硬盘检测)
  - [常用软件安装](#常用软件安装)
    - [Rosetta 2](#rosetta-2)
    - [Homebrew](#homebrew)
    - [IINA](#iina)
    - [PopClip](#popclip)
    - [iShot](#ishot)
    - [eul](#eul)
    - [bob](#bob)
    - [vscode](#vscode)
    - [Docker](#docker)
    - [AWSCLI](#awscli)
    - [IDEA](#idea)
    - [JDK](#jdk)
    - [VSCode插件](#vscode插件)
## 检查MAC

### 鉴别序列号和配置

1.   MacBook上点击关于本机—系统报告—找到型号标识符（11，1）；

2.   在Apple官网搜索 >> **[识别MacBook air机型](https://support.apple.com/zh-cn/HT201862)** >> 找到对应的型号，核对标识符是否一致。

### 检测屏幕

屏幕测试网站:https://screen.bmcx.com/#welcome

### **声音功能**

播放一段音频听音质，这远远不够；在系统偏好设置—声音—输出，左右拖动平衡，测试左右声道功能是否都正常

### 检查电池循环

在左上角点苹果标志—关于本机—系统报告—电源

### 检测摄像头

在DOCK栏启动Face Time，打开摄像头，显示人像就行

### 硬盘检测

在左上角点苹果标志—关于本机-储存空间显示为闪存为原装硬盘，非原装硬盘显示固态“SATA”驱动器。


## 常用软件安装

### Rosetta 2

```shell
softwareupdate --install-rosetta
```

### Homebrew

[homebrew官网](https://brew.sh/index_zh-cn)

简单的使用文档: [Homebrew](./Homebrew.md)

### IINA

官网: https://iina.io

### PopClip

据说很好用 APP store 98
### iShot

截图应用,默认存放在下载目录
[iShout官网](https://www.better365.cn/ishot.html)
快捷键: 
- Option + A: 截图
- Option + S: 固定截图到屏幕
- Option + W: 开始/停止录制

### eul
用于显示CPU 内存 网络等状态
[eul官网](https://github.com/gao-sun/eul)

```shell
brew install --cask eul
```

### bob

使用说明: https://ripperhe.gitee.io/bob/#/

```bash
brew install --cask bob
```
### vscode

官网: https://code.visualstudio.com/Download

### Docker

[Docker官网](https://docs.docker.com/desktop/mac/apple-silicon/)

### AWSCLI

[AWSCLI官网](https://aws.amazon.com/cn/cli/)

```bash
brew install awscli
# 或
pip install awscli
```

### IDEA

官网: https://www.jetbrains.com/zh-cn/idea/download/

### JDK

旧版:
https://www.azul.com/downloads/?version=java-11-lts&os=macos&architecture=arm-64-bit&package=jdk#download-openjdk

新版:
https://www.oracle.com/java/technologies/downloads/

### VSCode插件
- Markdown All in one
- Chinese
- Python
- Markdown Preview Enhanced
- Code Spell Checker
- Gitlens
- Drawio
- MongoDB for VS Code
- MySQL
- LeetCode




