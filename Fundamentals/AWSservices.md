

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
- 


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


Hosting a dynamic website - meaning ?
