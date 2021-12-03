[toc]

## 常见问题

### Please login as the user "ec2-user" rather than the user "root".

```shell
[ec2-user@ip-10-4-7-51 ~]$ sudo cat /root/.ssh/authorized_keys
no-port-forwarding,no-agent-forwarding,no-X11-forwarding,command="echo 'Please login as the user \"ec2-user\" rather than the user \"root\".';echo;sleep 10" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDFw38SgXXnz+/2AEXS3Iyl04Sq55ersJfmDoor7gdqDVLV5yZ5YGHaSiu/kP/pHHBU7jMhjm6JpjR9xJ9iFp57tNl2eW8Sym02j8z/DI1qUrvpT9I1/sWGWlB80O0c6zfnLq9jEMNCj/0oNtqKluqYD28gD9o56staaj15VWxT9lPI/cjNL/eWoHOh++9DJwBmjtkOutMjjiTeHuM275n8rQkMDTaIfnXitnLGlqvHiQqpyt/6CTxPJLS5Or3HrLkyf3YgPVmhqCdzoBp+KStBnFmGk2aejuKwposPsOR6299CZgQdG8oBHHClQFFRo5IIXJWeKHGkeeDbBahQ7HiB myselfkey
```

解决方法:

```shell
[ec2-user@ip-10-4-7-51 ~]$ sudo cp .ssh/authorized_keys /root/.ssh/authorized_keys
```



