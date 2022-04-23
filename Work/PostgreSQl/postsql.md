#### 查询数据库大小

```sql
SELECT pg_size_pretty(pg_database_size('rcdb'));
```