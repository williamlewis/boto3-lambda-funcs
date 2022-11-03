# Mastering Boto3 and Lambda Functions Using Python
Hands-on projects using Boto3 Python SDK for AWS


Instructor:  Hari Kammana

Platform:  Udemy


--



- Managing EC2 Instances, EBS Volumes, & AMIs + Notifications with SNS
- Using Lambda Functions with S3, DynamoDB, CloudWatch, EC2, AMIs, & SNS


Project
- services used
- action taken using xyz methods



|SERVICES|S3|CLOUDWATCH|LAMBDA|DYNAMODB
|---:|---|---|---|---|
|VIA CONSOLE|uploaded sample CSV file|created event for CSV uploads into bucket|created function|created sample table|
|VIA BOTO3|created bucket w/ xyz() method|got bucket & object details from event log response|read & converted file data|wrote data to table|

---

## Course Outline

- Managing EC2 Services & EBS Snapshots
    - Launching EC2 Instances

    - Operations on EC2

    - Filtering & Describing EC2 Instances

    - Boto3 Collections
    
    - Taking EBS Snapshots & Sending Email Notifications

    - Deleting EBS Snapshots Older than X Days

    - **Migrating AMIs to Different Regions Using Boto3 Waiters








- AWS Lambda - Develop Real-Time Use Cases
- Boto3 & DynamoDB
- Operations on S3
- Cost Optimization


<br/>
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



<table>
    <thead>
        <tr>
            <th>Column 1 Header</th>
            <th>Column 2 Header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1 - Column 1</td>
            <td>Row 1 - Column 2</td>
        </tr>
        <tr>
            <td colspan=2, style="text-align: center">Row 2 - Columns 1 - 2</td>
        </tr>
    </tbody>
</table>



**test text here**

