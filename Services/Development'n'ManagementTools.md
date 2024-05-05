### AWS Development and Management Tools

#### **AWS CodeBuild**
- **Function**: A fully managed continuous integration service that compiles source code, runs tests, and produces software packages.
- **Key Point**: It retrieves code dependencies but doesn't store them.

#### **AWS CodeArtifact**
- **Function**: A managed artifact repository service that stores, publishes, and shares software packages.
- **Key Point**: Enhances security and collaboration in software development.

#### **AWS CodePipeline**
- **Function**: A continuous delivery service that automates release pipelines for quick and reliable updates of applications and infrastructure.
- **Key Point**: Streamlines the deployment process across your development and production environments.

#### **AWS CodeStar**
- **Function**: Provides a unified user interface to develop, build, and deploy applications on AWS quickly.
- **Key Point**: Integrates with other AWS services for a seamless CI/CD experience.

### AWS Infrastructure Management

#### **AWS CloudFormation**
- **Function**: Uses JSON or YAML templates to declare the set of AWS resources that make up a stack.
- **Key Point**: Automates and simplifies the provisioning and management of AWS resources.

#### **AWS Elastic Beanstalk**
- **Function**: An easy-to-use service for deploying applications which automatically handles the details of capacity provisioning, load balancing, scaling, and monitoring.
- **Key Point**: Ideal for developers unfamiliar with managing the infrastructure that runs their applications.

### Database Services

#### **Amazon RDS (Relational Database Service)**
- **Function**: Simplifies setting up, operating, and scaling a relational database in the cloud.
- **Key Points**: 
  - Offers cost-efficient and resizable capacity.
  - Automates time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups.
  - Suitable for Online Transaction Processing (OLTP).

#### **Amazon Aurora**
- **Function**: A MySQL and PostgreSQL-compatible relational database with a blend of speed and reliability.
- **Key Points**:
  - Combines the performance of high-end databases with the cost-effectiveness of open-source databases.
  - Not necessarily serverless but offers high scalability and durability.

#### **AWS Database Migration Service (DMS)**
- **Function**: Facilitates the migration of databases to AWS securely and with minimal downtime.
- **Key Point**: The source database remains operational during the migration, which minimizes disruption.

### Analytics and Big Data

#### **AWS Glue**
- **Function**: A managed ETL (extract, transform, load) service that prepares and loads data for analytics.
- **Key Point**: Integrates with the AWS Glue Data Catalog, offering a persistent metadata store for your data assets.

#### **Amazon QuickSight**
- **Function**: A business intelligence service that provides quick and easy insights for your organization.
- **Key Point**: Allows creation and publication of interactive dashboards.

#### **Amazon Athena**
- **Function**: Enables easy analysis of data in Amazon S3 using standard SQL in a serverless fashion.
- **Key Point**: Pay-for-query model, which means paying only for the queries executed.

#### **Amazon EMR (Elastic MapReduce)**
- **Function**: Facilitates processing large amounts of data using Hadoop framework alongside other big data frameworks.
- **Key Point**: Suitable for data transformation, preprocessing, and analysis.

### Caching and Performance

#### **Amazon DynamoDB Accelerator (DAX)**
- **Function**: Provides an in-memory cache for DynamoDB, significantly improving read performance.
- **Key Point**: Delivers up to a 10x performance improvement.

#### **Amazon ElastiCache**
- **Function**: Supports caching strategies using either Memcached or Redis to enhance the performance of web applications by retrieving data from fast, managed, in-memory caches.
- **Key Point**: Helps reduce database load and increases application performance.
