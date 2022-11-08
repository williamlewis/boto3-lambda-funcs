# Mastering Boto3 and Lambda Functions Using Python
Hands-on projects using Boto3 Python SDK for AWS

Instructor:  Hari Kammana

Platform:  Udemy


---


## Part 1:  Boto3 for Lambda Functions
Using Boto3 within Lambda Functions to manage S3, DynamoDB, CloudWatch, EC2, AMIs, SNS, & SES







- Find unused Elastic IPs and send alert email using SES and Lambda environmental variables
- Persist CSV data to DynamoDB when file is uploaded to an S3 bucket
- Persist JSON data to DynamoDB when file upload triggers a CloudWatch log event
- Send Slack message via webhook to alert when an instance has stopped
- Check for unattached (unused) EBS volumes and send alert email using SNS



---

## Part 2:  Boto3 Terminal Scripts
Using Boto3 Terminal Scripts to manage EC2 Instances, EBS Volumes, & AMIs


- Create AMI & copy to another region
- Describe instances from resource collection
- Batch write data to DynamoDB table
- Delete data from DynamoDB table
- Email list of EBS Snapshots base on tags
- Get instances from filtered resource collections
- Launch new intances based on AMI & instance type
- Delete EBS snapshots older than x days
- Deregister unused custom AMIs
- Query contents of CSV file stored in S3
- Start, stop, & terminate instances based in Id

















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




