描述: 修改MAC默认截图地址

1. 创建截图存放位置
   
   ```
   mkdir ~/Desktop/Snapshot
   ```

2. 修改存储位置
   
   ```
   defaults write com.apple.screencapture location ~/Desktop/Snapshot
   ```

3. 修改截图格式(可选)
   
   ```
   # png gif pdf jpg
   defaults write com.apple.screencapture type jpg 
   ```

4. 重启UI
   
   ```
   killall SystemUIServer
   ```
