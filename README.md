
#### Resources

- REVIEW - THE MOST IMPORTANT CHAPETERS AS EC2, MIGRATING - SNOWFLAKE APPLICATIONS, ETC.
- 
AWS provides a vast array of resources through services like EC2 for scalable computing power, S3 for storage, and RDS for managed databases. These services allow businesses to deploy, manage, and scale their applications seamlessly, offering both flexibility and reliability.

#### Networking
AWS offers advanced networking capabilities through services like Amazon VPC, which allows users to create isolated networks, AWS Direct Connect for dedicated network connections, and Route 53 for scalable DNS and domain management. These services ensure secure, scalable, and efficient network configurations.

#### Security
AWS emphasizes security with services such as AWS Identity and Access Management (IAM) for user access control, AWS Key Management Service (KMS) for encryption, and AWS Shield for DDoS protection. These tools help safeguard data and ensure compliance with security standards.

#### IaaS and PaaS
AWS provides Infrastructure as a Service (IaaS) with offerings like EC2, which allows users to rent virtual servers and other infrastructure. For Platform as a Service (PaaS), AWS offers services like AWS Elastic Beanstalk, which simplifies application deployment and management by handling the underlying infrastructure automatically.


**AWS - Amazon Web Services Overview**
- **Global Reach**: AWS is the most comprehensive and broadly adopted cloud platform worldwide, offering over 200 fully featured services from 32 launched regions and 102 availability zones, ensuring high availability and performance.
- **Innovation Leader**: Recognized as a market leader in cloud computing, AWS continues to pioneer innovations in cloud technology, setting industry standards.
- **Wide Adoption**: Trusted by millions to power diverse requirements from infrastructure to machine learning.

**AWS Core Service Domains**
- **Compute, Storage, Database, and Networking**: Fundamental to most cloud services, these domains form the bedrock of AWS.
  - **Compute**: Like the head chef, it’s where processing and operations happen.
  - **Storage**: Acts as the pantry, providing space for data.
  - **Database**: Functions as the recipe book, structuring and retrieving data.
  - **Networking**: Ensures smooth data flow and connectivity with external systems, such as payment processors.

**AWS Compute Services**
- **Amazon EC2**: Offers scalable computing capacity in the AWS cloud allowing users to use virtual servers (instances).
- **AWS Lambda**: Serverless computing service, running code in response to events, suitable for applications like real-time file processing and data transformation.

**Storage Solutions**
- **Active Storage (Amazon S3)**: Scalable storage for data backup, archival, and analytics.
- **Archival Storage (AWS Glacier)**: Cost-effective for data archiving with infrequent access.
- **Elastic Block Store (EBS)**, **Elastic File System (EFS)**, and **FSx**: Provide block and file storage solutions for diverse needs.

**Database Services**
- **Amazon RDS**: Supports relational databases for structured data with clear relations, suitable for traditional applications such as financial systems.
- **Amazon DynamoDB**: A NoSQL database that supports key-value and document data structures, ideal for mobile apps, IoT, and gaming.

**AWS Networking**
- **VPC (Virtual Private Cloud)**: Provides a private network to deploy AWS resources, enhancing security and control.
- **Edge Locations**: Facilitates content delivery with reduced latency, enhancing user experience globally.

**Serverless and Server-based Computing Models**
- **Traditional vs. Serverless**: EC2 provides continuous availability and customization; Lambda offers cost-effective, event-driven computing without server management.

**AWS Cost and Capacity Management**
- **Savings Plan and Compute Optimizer**: Tools to optimize costs and compute capacity.
- **Elastic Beanstalk and Image Builder**: Simplify application deployment and management.
- **Load Balancing**: Distributes incoming application traffic across multiple targets, enhancing availability.

**Common Use-Cases for AWS Lambda**
- **Data Processing**: ETL jobs and real-time file processing.
- **APIs**: Serverless REST or GraphQL APIs via AWS API Gateway.
- **Automation**: Tasks like backups or notifications.
- **Analytics**: Streaming analytics from sources like Kinesis.
- **Interactivity**: Powering chatbots for customer service.

**Why AWS Lambda is Well-Suited for These Scenarios**
- **Scalability**: Automatically adjusts to the required workload.
- **Cost-Effectiveness**: Only charges for the compute time used.
- **Low Latency**: Executes functions rapidly.
- **Event-Driven**: Integrates seamlessly with other AWS services.
- **Simplicity**: Eliminates the need to manage servers, focusing on code development.

AWS - Amazon Web Services
- Most comprehensive and broadly adopted cloud platform
- It is like having a super computer
- Market leader in cloud computing
- Trusted by millions of customers
- Over 200 fully featured services
- Pioneering inovation in Cloud technology and its setting industries standards

AWS Core service domains
- Compute
- Storage
- Database
- Networking
    -  ensures smooth communication  and data flow ( external systems like payment processors)

AWS geographical vastness
- 32 launched regions
    - Data centres in each region ( used to organise, process , store , disseminate large amounts of data) ensuring security, reliability and brisk performance (high speed)
- 102 AZ - redundancy high availability for operational robustness
* Edge Locations are individual points of presence located in major cities, often used for content distribution. They are larger than individual Data Centers but smaller than Availability Zones


Compute, storage and database
- Essential concepts to grasp, as they form the bedrock of  most cloud services
- Analogy
    - Compute - The head chef
    - Storage - The pantry, fridge
    - Databases - recipe books

Cloud Computing
 - servers - physical vs VMs
- Full control and customisation
- Ex. Webhosting,  data analytics 

- Serverless - managed by the provider (AWS f.e.)
    - No need to manage server infrastructure
    - Runs code in response to events 
    - Examples image processing, real time data updates
    - Ex. Image processing, real time data updates

Storage
- Ensures availability, durability, swift retrieval times

Databases
- The nerve systems of our digital landscapes (digitální porstředí)
- Beyond Storage - organising and retrieving data
- Like a library in the digital world
    -  Categorizes, arranges and provides a system to easily retrieve books.
- Offer structured systems to efficiently access and modify data
- Relacni (data stored in tables, SQL queries) a nerelacni database ( flexible data models, often schema less)

disseminate - spread (something, especially information) widely.

AWS Compute Services
- EC2
- Lambda
- Compute services as the ability to provide computing power on demand.
    - Importance : scalability, flexibility, and cost-efficiency 
- Meeting the demand with AWS
    - Server based 
        - Continuous availability 
        - Dedicated resources
        - More control
        - Customization (like owning a car)
    - Serverless
        - On-demand execution
        - No server management
        - Event Driven
        - Cost effective
        - Its like using a taxi service, its there when you need it, and gone when you don’t
        - 
- EC2 - Server based solution
        - Sandbox where you can build whatever you want, no just a box of sand but a playground, with different zones for various activities.
        - Virtual server in the cloud
        - Customisable configurations (OS, Storage, location)
        - Focus on customisation and control
- Lambda
    - Serverless computing platform
    - Name comes from Lambda Calculus
    - Event-driven architecture (file uploads, database changes)
        - Meaning it can automatically run code in response to a variety of events 
        - Fe. It can process a new file the moment it’s uploaded to a website, or update a database entry when record is added.

In real life:
- EC2 
    - Hosting websites
    - Scalability and customisation
- Lambda 
    - Real time image processing, or automated backups
    - Event driven tasks


AWS - Cost and capacity management 
- Savings plan
- Compute Optimiser
- Elastic Beanstalk
- Image builder
- Load balancing

AWS Instance
- AMazon EC2
- EC2 Spot
- EC2 autoscaling
- Lightsail
- Batch



What are some common use-cases for AWS Lambda, and why is it well-suited for those scenarios?

Common Use-Cases for AWS Lambda:
* Data Processing: Handle large-scale data transformations like ETL jobs.
* APIs: Build serverless REST or GraphQL APIs via AWS API Gateway.
* Automation: Automate repetitive tasks like backups or notifications.
* Real-Time File Processing: Process files as they are uploaded to AWS S3.
* Streaming Analytics: Analyze real-time data streams from services like Kinesis.
* Chatbots: Power conversational interfaces for customer service.
Why It's Well-Suited:
* Scalability: Automatically scales to handle the workload.
* Cost-Effectiveness: Pay only for the time your code runs.
* Low Latency: Quick to start and execute functions.
* Event-Driven: Easily integrates with other AWS services for event-based triggers.
* Simplicity: No need to manage servers, so you can focus on code.
* AWS Lambda is ideal for these scenarios because it's designed for quick, event-driven tasks that can scale automatically and cost-effectively.

Can you explain what AWS Lambda is and how it differs from traditional server-based computing models?

Certainly! AWS Lambda is a serverless computing service that lets you run code without managing servers. It is event-driven, scales automatically, and you only pay for the time your code runs.
Key Differences from Traditional Servers:
* No Server Management: Lambda handles it for you.
* Automatic Scaling: Lambda scales with the number of events.
* Pay-as-You-Go: Only pay for the compute time you use.
* Stateless: Each function execution is independent.
* Short-lived: Functions have a time limit per execution.
* Traditional servers, on the other hand, require you to manage the server, handle scaling manually, and pay for server uptime, whether or not you are using it. They are generally stateful and long-lived.


AWS Storage options 

Active Storage (Direct Storage)
- Like your recent emails, readily accesible
- Ideal for day to day storage
- Amazon S3 - designed for ease of access and management
    - Simple Storage Service
    - Highly scalable, durable and secure
    - Wide variety of use cases like website hosting, data backup, and content distribution 
    - Or Real-time big data analytics 
    - S3 design aims at maximising benefits of scale and passing those benefits to customers
    - Object storage service
    - Used for storing and retrieving any amount data, anytime, from anywhere
    - Can get pricey

Archival Storage
- Like old emails, accessed infrequently
- Ideal for long term data retention
- AWS Glacier - cost effective for long-term storage
    - Used for data archiving and long term backup
    - Long-term, low cost, and secure cloud storage service
    - Cost effective  solution for data archiving and backup

AWS Storage Services
- Amazon S3
- AWS Elastic Block Storage
- Elastic File System
- Am. Storage Gateway
- FSx (Shared File Storage)


Understanding database types

- Relational Databas (RDS)
    - Like a well organised bookshelf
    - Structured data with clear relations
    - Ideal for traditional applications 
    - AWS RDS the sturdy bookshelf of the digital world
    - Ex. Financial systems, e-commerce platforms 

- NoSQL Databases (DynamoDB)
    - Like a dynamic magazine rack
    - Flexible schema for unstructured data
    - Ideal for mobile apps, IoT, gaming
    - AWS DynamoDB : adaptable and ready for every changing content
        - Uses a key-value model
        - A key maps to a value
    - Ex. Real time bidding systems, leaderboards for gaming

---
