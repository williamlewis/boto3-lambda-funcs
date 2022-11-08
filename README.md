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
            <td width="20%"><a href="">file name (hyperlink to gh page)</a></td>
            <td width="60%">regular text description</td>
            <td width="20%"><code>classes used (code snippet)</code></td>
        </tr>
        <tr>
            <td width="20%" ><a href="">find_and_email_unused_eips.py</a></td>
            <td width="60%">Find unused Elastic IPs and send alert email using SES and Lambda environmental variables</td>
            <td width="20%"><code>EC2.Client</code>, <code>SES.Client</code></td>
        </tr>
        <tr>
            <td width="20%"><a href="">s3_csv_to_dynamodb.py</a></td>
            <td width="60%">Persist CSV data to DynamoDB when file is uploaded to an S3 bucket</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="">s3_json_to_dynamodb.py</a></td>
            <td width="60%">Persist JSON data to DynamoDB when file upload triggers a CloudWatch log event</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="">slack_alert.py</a></td>
            <td width="60%">Send Slack message via webhook to alert when an instance has stopped</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href="">unused_volumes.py</a></td>
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
            <td width="20%"><a href=""></a></td>
            <td width="60%"></td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href=""></a></td>
            <td width="60%"></td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href=""></a></td>
            <td width="60%"></td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href=""></a></td>
            <td width="60%"></td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href=""></a></td>
            <td width="60%"></td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href=""></a></td>
            <td width="60%"></td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href=""></a></td>
            <td width="60%"></td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href=""></a></td>
            <td width="60%"></td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href=""></a></td>
            <td width="60%">Deregister unused custom AMIs</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href=""></a></td>
            <td width="60%">Query contents of CSV file stored in S3</td>
            <td width="20%"><code></code></td>
        </tr>
        <tr>
            <td width="20%"><a href=""></a></td>
            <td width="60%">Start, stop, & terminate instances based in Id</td>
            <td width="20%"><code></code></td>
        </tr>
    </tbody>
</table>






- Create AMI & copy to another region
- Describe instances from resource collection
- Batch write data to DynamoDB table
- Delete data from DynamoDB table
- Email list of EBS Snapshots base on tags
- Get instances from filtered resource collections
- Launch new intances based on AMI & instance type
- Delete EBS snapshots older than x days
- 
- 
- 

















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




