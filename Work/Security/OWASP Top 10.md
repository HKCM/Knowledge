# OWASP Top 10


http://www.owasp.org.cn/OWASP-CHINA/owasp-project/
https://www.cnblogs.com/pengdai/p/12169534.html

## 注入

注入攻击试图欺骗应用程序，将恶意用户提供的数据发送到应用程序内的解释器中。解释器（或分析器）通常接受某种字符串命令作为输入。**解释器和命令字符串的例子包括：**
	* 数据库查询（SQL 语句）。\
	* LDAP（LDAP 查询）
	* 操作系统 shell 命令（基于字符串的命令）
	* XML 分析器（XML、DTD、XPath 查询）

## SQL 注入

SQL 注入攻击包括通过用户输入数据，将 SQL 数据库查询片段插入或“注入”到您的应用程序中。此类被污染的输入通过传统 Web 客户端或 API 调用发送给应用程序。

危害
	* 阅读来自数据库的敏感数据
	* 对数据库数据执行操作
	* 对数据库执行管理操作（例如关闭 DBMS）
	* 恢复 DBMS 文件系统上给定文件的内容
	* 向操作系统发出命令（在某些情况下）

[OWASP SQL 注入预防备忘表](http://synopsys.support/OWASP2l1) 
[各语言安全代码示例的扩展列表](https://bobby-tables.com/)

## 命令注入

命令注入是一种漏洞，该漏洞允许在托管应用程序的操作系统上执行任意命令。当应用程序将用户提供的不安全数据（例如 Cookie、以 POST 方式提交的数据或 HTTP 标头等）传递给系统 shell 命令时，可能会发生此类攻击。恶意命令通常使用与主机上运行的应用程序相同的权限运行。

## 身份认证
 [OWASP 会话管理备忘表](http://synopsys.support/OWASP3l2) 
 [OWASP 忘记密码备忘表](http://synopsys.support/OWASP3l4) 
 [OWASP 密码存储备忘表](http://synopsys.support/OWASP3l5) 

##  敏感数据泄露
 [OWASP 加密存储备忘表](http://synopsys.support/OWASP7l2) 
## XML外部实体
## 失效的访问控制
## 安全配置错误
## 跨脚本（XSS）
 [OWASP 跨站点脚本防御备忘录](http://synopsys.support/OWASP4l11) 





