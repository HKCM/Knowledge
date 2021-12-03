

## 描述: shell脚本的执行时间


```shell
START_TIME=`date '+%F %T'`
# code......
DONE_TIME=`date '+%F %T'`

# Consuming Time Calculate
TOTAL_TIME=$((`date -d "$DONE_TIME" +%s`-`date -d "$START_TIME" +%s`))

function Time_convert(){
  Seconds=$(($1%60))
  Mins=$(( $1/60 ))
  echo "$2 : $Mins min(s) $Seconds s"
}
echo ""
Time_convert $TOTAL_TIME "Prepare Time "
echo ""
```


另外一种
```shell
START_TIME=$(date +%s)
# code......
DONE_TIME=$(date +%s)
# Consuming Time Calculate
TOTAL_TIME=$(($DONE_TIME-$START_TIME))

function Time_convert(){
    Seconds=$(($1%60))
    Mins=$(( $1/60 ))
    write_log "$2 : $Mins min(s) $Seconds s"
}

Time_convert $TOTAL_TIME "Deployment Time "
```

