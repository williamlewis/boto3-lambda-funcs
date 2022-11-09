# Mastering Boto3 and Lambda Functions Using Python
Hands-on projects using Boto3 Python SDK for AWS

Instructor:  Hari Kammana

Platform:  Udemy

<br/>
<br/>

---


## Part 1:  Boto3 for Lambda Functions
Using Boto3 within Lambda Functions to manage S3, DynamoDB, CloudWatch, EC2, AMIs, SNS, & SES


<table>
    <thead>
        <tr>
            <th width="20%">Name</th>
            <th width="60%">Description</th>
            <th width="20%">Classes Used</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td width="20%" ><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/01%20-%20Boto3%20Lambda%20Functions/find_and_email_unused_eips.py">find_and_email_unused_eips.py</a></td>
            <td width="60%">Find unused Elastic IPs and send alert email using SES and Lambda environmental variables</td>
            <td width="20%"><code>EC2.Client</code>, <code>SES.Client</code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/01%20-%20Boto3%20Lambda%20Functions/s3_csv_to_dynamodb.py">s3_csv_to_dynamodb.py</a></td>
            <td width="60%">Persist CSV data to DynamoDB when file is uploaded to an S3 bucket</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/01%20-%20Boto3%20Lambda%20Functions/s3_json_to_dynamodb.py">s3_json_to_dynamodb.py</a></td>
            <td width="60%">Persist JSON data to DynamoDB when file upload triggers a CloudWatch log event</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/01%20-%20Boto3%20Lambda%20Functions/slack_alert.py">slack_alert.py</a></td>
            <td width="60%">Send Slack message via webhook to alert when an instance has stopped</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/01%20-%20Boto3%20Lambda%20Functions/unused_volumes.py">unused_volumes.py</a></td>
            <td width="60%">Check for unattached (unused) EBS volumes and send alert email using SNS</td>
            <td width="20%"><code></code></td>
        </tr>
    </tbody>
</table>



<br/>
<br/>

---

## Part 2:  Boto3 Terminal Scripts
Using Boto3 Terminal Scripts to manage EC2 Instances, EBS Volumes, & AMIs


<table>
    <thead>
        <tr>
            <th width="20%">Name</th>
            <th width="60%">Description</th>
            <th width="20%">Classes Used</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/create_image_copy_to_diff_region.py">create_image_copy_to_diff_region.py</a></td>
            <td width="60%">Create AMI & copy to another region</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/describe_instances.py">describe_instances.py</a></td>
            <td width="60%">Describe instances from resource collection</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/dynamobd_batch_write.py">dynamobd_batch_write.py</a></td>
            <td width="60%">Batch write data to DynamoDB table</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/dynamobd_get_and_delete.py">dynamobd_get_and_delete.py</a></td>
            <td width="60%">Delete data from DynamoDB table</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/ebs_snapshots_email.py">ebs_snapshots_email.py</a></td>
            <td width="60%">Email list of EBS Snapshots base on tags</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/ec2_collections.py">ec2_collections.py</a></td>
            <td width="60%">Get instances from filtered resource collections</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/launch_ec2.py">launch_ec2.py</a></td>
            <td width="60%">Launch new intances based on AMI & instance type</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/remove_old_ebs_snapshots.py">remove_old_ebs_snapshots.py</a></td>
            <td width="60%">Delete EBS snapshots older than 15 days</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/remove_unused_amis.py">remove_unused_amis.py</a></td>
            <td width="60%">Deregister unused custom AMIs</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/s3_query_csv_select_object_content.py">s3_query_csv_select_object_content.py</a></td>
            <td width="60%">Query contents of CSV file stored in S3</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="https://github.com/williamlewis/boto3-lambda-funcs/blob/main/02%20-%20Boto3%20Terminal%20Scripts/sec_start_stop_terminate.py">sec_start_stop_terminate.py</a></td>
            <td width="60%">Start, stop, & terminate instances based in Id</td>
            <td width="20%"><code></code></td>
        </tr>
    </tbody>
</table>

















Project
- services used
- action taken using xyz methods



|SERVICES|S3|CLOUDWATCH|LAMBDA|DYNAMODB
|---:|---|---|---|---|
|VIA CONSOLE|uploaded sample CSV file|created event for CSV uploads into bucket|created function|created sample table|
|VIA BOTO3|created bucket w/ xyz() method|got bucket & object details from event log response|read & converted file data|wrote data to table|


<br/>
<br/>

---
- TEST Table Format

    |   SECTION (CODE SAMPLE)   |   ACTION  |   CLASSES USED    |   METHODS USED    |
    |---:|---|---|---|
    |**Section 2:**|**Managing EC2 Services & EBS Snapshots**
    |<!-- **Launching EC2 Instances** --> | create and launch new EC2 instances | `EC2.Client` | `.run_instances()` | AMI `ImageId`, Min. & Max. number of instances | None
    |<!-- **Operations on EC2** --> | start, stop, & terminate EC2 instances | `EC2.Client` | `.start_instances()`, `.stop_instances()`, `.terminate_instances()`
    |<!-- **Filtering & Describing EC2 Instances** --> | filter instances & display selected attributes | `EC2.Client` |  `.describe_instances()` 
    |<!-- **Boto3 Collections** --> | find & stop instances in a running state | `EC2.ServiceResource` | `.stop()`
    |<!-- **Taking EBS Snapshots & Sending Email Notifications** --> | take a snapshot of EBS volumes, then publish an email noting Snapshot Ids | `EC2.ServiceResource`, `SNS.Client` | `.publish()`
    |<!-- **Deleting EBS Snapshots Older than X Days** --> | delete EC2 snapshots older than 15 days, using Python `datetime` module | #### `EC2.ServiceResource` | `.snapshots.fitler()`, `.delete()`
    |<!-- **Migrating AMIs to Different Regions Using Boto3 Waiters** --> | create AMI from EC2 instance, wait for AMI to become available, then copy AMI to a different region | `EC2.ServiceResource`, `EC2.Client`, `EC2.Waiter.ImageAvailable` | `.create_image()`, `.get_waiter()`, `.wait()`
    |Section 3 - Lambda Functions & Real-Time Use Cases||||
    |Section 4||||







