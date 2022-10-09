# Mastering Boto3 and Lambda Functions Using Python
Hands-on projects using Boto3 Python SDK for AWS


Instructor:  Hari Kammana

Platform:  Udemy


--

## Course Outline

- Managing EC2 Services & EBS Snapshots
    - **Launching EC2 Instances**
        - create and launch new EC2 instances using `EC2.Client` class and `.run_instances()` method
        - provided inputs:  AMI ImageId, Min. / Max. number of instances

    - **Operations on EC2**
        - start, stop, and terminate existing EC2 isntances using `EC2.Client` class and `.start_instances()`, `.stop_instances()`, and `.terminate_instances()` methods
        - provided inputs:  InstanceId (list of Ids if multiple)

    - **Filtering & Describing EC2 Instances**
        - filter instances and display selected attributes using `EC2.Client` class and `.describe_instances()` method
        - provided inputs:  instance tag key/value pairs, attributes to describe

    - **Boto3 Collections**
        - find and stop instances in a "running" state using `EC2.ServiceResource` class and `.stop()` method
        - provided inputs:  current instance state
    
    - **Taking EBS Snapshots & Sending Email Notifications**
        - take a snapshot for all EBS volumes attached to a filtered selection of EC2 instances, using `EC2.ServiceResource` class
        - publish an email message noting all Snapshot Ids using `SNS.Client` class and `.publish()` method
        - provided inputs:  instance tag key/value pairs, snapshot description, SNS message, SNS TopicArn, SNS email subject

    - **Deleting EBS Snapshots Older than X Days**
        - delete EC2 snapshots started more than 15 days ago by self using `EC2.ServiceResource` class and `.snapshots.filter()` and `.delete()` methods
        - provided inputs:  snapshot OwnerIds
        - python modules:  `datetime`

    - **Migrating AMIs to Different Regions Using Boto3 Waiters**
        - create AMI from filtered selection of EC2 instances using `EC2.ServiceResource` class and `.create_image()` method
        - wait for newly created AMI to become available using `EC2.Client` and `EC2.Waiter.ImageAvailable` classes and `.get_waiter()` and `.wait()` methods
        - copy AMI image from a source region to a separate destination region using `EC2.Client` class and `.copy_image()` method








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



