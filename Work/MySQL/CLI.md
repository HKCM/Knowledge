查看数据库编码：

show variables like '%char%'; 

| column0    | column1                                                                               |
|------------|---------------------------------------------------------------------------------------|
| client     | 为客户端使用的字符集。                                                                    |
| connection | 为连接数据库的字符集设置类型，如果程序没有指明连接数据库使用的字符集类型则按照服务器端默认的字符集设置。 |
| database   | 为数据库服务器中某个库使用的字符集设定，如果建库时没有指明，将使用服务器安装时指定的字符集设置。        |
| results    | 为数据库给客户端返回时使用的字符集设定，如果没有指明，使用服务器默认的字符集。                       |
| server     | 为服务器安装时指定的默认字符集设定。                                                        |
| system     | 为数据库系统使用的字符集设定。                                                             |

