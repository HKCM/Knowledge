## Restoring a Table to a Point in Time (Console)

The following example demonstrates how to use the DynamoDB console to restore an existing table named Music to a point in time.

*Note*
This procedure assumes that you have enabled point-in-time recovery. To enable it for the Music table, on the Overview tab, in the Table details section, choose Enable for Point-in-time recovery.

To restore a table to a point in time

1. Sign in to the AWS Management Console and open the DynamoDB console at https://console.aws.amazon.com/dynamodb/.

2. In the navigation pane on the left side of the console, choose Tables.

3. In the list of tables, choose the Music table.

4. On the Backups tab of the Music table, in the Point-in-time recovery section, choose Restore to point-in-time.

5. For the new table name, enter MusicMinutesAgo.

*Note*
You can restore the table to the same AWS Region or to a different Region from where the source table resides. You can also exclude secondary indexes from being created on the restored table. In addition, you can specify a different encryption mode.

6. To confirm the restorable time, set the Restore date and time to the Latest restore date. Then choose Restore table to start the restore process.

*Note*
You can restore to any point in time within Earliest restore date and Latest restore date. DynamoDB restores your table data to the state based on the selected date and time (day:hour:minute:second).

The table that is being restored is shown with the status Restoring. After the restore process is finished, the status of the Music table changes to Active.



## Restoring a Table from a Backup (Console)
The following procedure shows how to restore the Music table by using the MusicBackup file that is created in the Backing Up a DynamoDB Table tutorial.

*Note*
This procedure assumes that the Music table no longer exists before restoring it using the MusicBackup file.

To restore a table from a backup

1. Sign in to the AWS Management Console and open the DynamoDB console at https://console.aws.amazon.com/dynamodb/.

2. In the navigation pane on the left side of the console, choose Backups.

3. In the list of backups, choose MusicBackup.

4. Choose Restore backup.

5. Enter Music as the new table name. Confirm the backup name and other backup details. Then choose Restore table to start the restore process.

*Note*
You can restore the table to the same AWS Region or to a different Region from where the backup resides. You can also exclude secondary indexes from being created on the new restored table. In addition, you can specify a different encryption mode.

The table that is being restored is shown with the status Creating. After the restore process is finished, the status of the Music table changes to Active.

## Restoring a Table from a Backup (AWS CLI)

Follow these steps to use the AWS CLI to restore the Music table using the MusicBackup that is created in the Backing Up a DynamoDB Table tutorial.

To restore a table from a backup

Confirm the backup that you want to restore by using the list-backups command. This example uses MusicBackup.
```
aws dynamodb list-backups
```
To get additional details for the backup, use the describe-backup command. You can get the input backup-arn from the previous step.

```
aws dynamodb describe-backup \
--backup-arn arn:aws:dynamodb:us-east-1:123456789012:table/Music/backup/01489173575360-b308cd7d 
```

Restore the table from the backup. In this case, the MusicBackup restores the Music table to the same AWS Region.
```
aws dynamodb restore-table-from-backup \
--target-table-name Music \
--backup-arn arn:aws:dynamodb:us-east-1:123456789012:table/Music/backup/01489173575360-b308cd7d 
```

Restore the table from the backup with custom table settings. In this case, the MusicBackup restores the Music table and specifies an encryption mode for the restored table.

*Note*

The sse-specification-override parameter takes the same values as the sse-specification-override parameter used in the CreateTable command. To learn more, see Managing Encrypted Tables.

```
aws dynamodb restore-table-from-backup \
--target-table-name Music \
--backup-arn arn:aws:dynamodb:us-east-1:123456789012:table/Music/backup/01581080476474-e177ebe2 \
--sse-specification-override Enabled=true,SSEType=KMS,KMSMasterKeyId=abcd1234-abcd-1234-a123-ab1234a1b234
```

You can restore the table to a different AWS Region from where the backup resides.

*Note*

The sse-specification-override parameter is mandatory for cross-Region restores but optional for restores in the same Region as the source table.

When performing a cross-Region restore from the command line, you must set the default AWS Region to the desired destination Region. To learn more, see Command Line Options in the AWS Command Line Interface User Guide.
```
aws dynamodb restore-table-from-backup \
--target-table-name Music \
--backup-arn arn:aws:dynamodb:us-east-1:123456789012:table/Music/backup/01581080476474-e177ebe2 \
--sse-specification-override Enabled=true,SSEType=KMS
```

You can override the billing mode and the provisioned throughput for the restored table.

```
aws dynamodb restore-table-from-backup \
--target-table-name Music \
--backup-arn arn:aws:dynamodb:us-east-1:123456789012:table/Music/backup/01489173575360-b308cd7d \
--billing-mode-override PAY_PER_REQUEST
```

You can exclude some or all secondary indexes from being created on the restored table.

*Note*
Restores can be faster and more cost-efficient if you exclude some or all secondary indexes from being created on the restored table.

```
aws dynamodb restore-table-from-backup \
--target-table-name Music \
--backup-arn arn:aws:dynamodb:us-east-1:123456789012:table/Music/backup/01581081403719-db9c1f91 \
--global-secondary-index-override '[]' \
--sse-specification-override Enabled=true,SSEType=KMS
```

*Note*
The secondary indexes provided should match existing indexes. You cannot create new indexes at the time of restore.

You can use a combination of different overrides. For example, you can use a single global secondary index and change provisioned throughput at the same time, as follows.

```
aws dynamodb restore-table-from-backup \
--target-table-name Music \
--backup-arn arn:aws:dynamodb:eu-west-1:123456789012:table/Music/backup/01581082594992-303b6239 \
--billing-mode-override PROVISIONED \
--provisioned-throughput-override ReadCapacityUnits=100,WriteCapacityUnits=100 \
--global-secondary-index-override IndexName=singers-index,KeySchema=["{AttributeName=SingerName,KeyType=HASH}"],Projection="{ProjectionType=KEYS_ONLY}",ProvisionedThroughput="{ReadCapacityUnits=5,WriteCapacityUnits=5}" \
--sse-specification-override Enabled=true,SSEType=KMS
```

To verify the restore, use the describe-table command to describe the Music table.
```
aws dynamodb describe-table --table-name Music 
```
The table that is being restored from the backup is shown with the status Creating. After the restore process is finished, the status of the Music table changes to Active.

#### Important

While a restore is in progress, don't modify or delete your IAM role policy; otherwise, unexpected behavior can result. For example, suppose that you removed write permissions for a table while that table is being restored. In this case, the underlying RestoreTableFromBackup operation would not be able to write any of the restored data to the table. *Note* that IAM policies involving source IP restrictions for accessing the target restore table might similarly cause issues.

After the restore operation is complete, you can modify or delete your IAM role policy.

If your backup is encrypted with an AWS managed CMK or a customer managed CMK, don't disable or delete the key while a restore is in progress, or the restore will fail.

After the restore operation is complete, you can change the encryption key for the restored table and disable or delete the old key.