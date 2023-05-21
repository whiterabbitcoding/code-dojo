What is kinesis firehose?

Kinesis Firehose is a data streaming service provided by Amazon Web Services
(AWS). It allows you to capture, transform, and load large amounts of streaming
data into data stores or analytics tools, such as Amazon S3, Redshift,
Elasticsearch, and Splunk, in near real-time. Kinesis Firehose handles the
complexities of scaling, buffering, and managing the data delivery process,
making it easier to ingest and process streaming data efficiently.

What input sources can kinesis firehose use?

Data astreams Log failes IoT devies - sensors etc Clickstreams - can handle user
interactions

Social Media Feeds - caputure and process realtime social media data so you can
monitor trends etc

What is AWS lambda?

Serverless computing service, allows you to rub code without provisioning or
managing servers.

Executer functions to change data ins s3, https request, apis etc

Supports multiple languages

What are the benefits of aws lambda?

Serverless Execution: You don't have to worry about server management, scaling,
or availability. AWS handles all the underlying infrastructure, allowing you to
focus on writing code and building applications.

Cost Efficiency: With Lambda, you pay only for the actual compute time consumed
by your functions. There are no upfront costs or charges for idle server time,
making it cost-effective for event-driven workloads.

Scalability: Lambda automatically scales your functions in response to incoming
requests. It can handle thousands of concurrent executions, ensuring that your
application can scale seamlessly without manual intervention.

Integration with AWS Services: Lambda seamlessly integrates with various AWS
services, enabling you to build powerful and event-driven architectures. You can
connect Lambda functions with services like S3, DynamoDB, SNS, SQS, and more.

Developer Productivity: AWS Lambda simplifies the deployment and management of
your code. You can update your functions without downtime, and versioning allows
you to keep track of changes and rollbacks.

What is AWS API gateway?

acts as a front door for your backend services, allowing you to expose your APIs
to external clients, such as web or mobile applications.

API Creation and Management: You can define the structure and behavior of your
APIs using API Gateway's intuitive interface or by importing API definitions in
popular formats like OpenAPI (formerly known as Swagger) or RAML. You can
configure authentication, authorization, request/response transformations,
caching, rate limiting, and other API management features.

Integration with Backend Services: API Gateway seamlessly integrates with other
AWS services, as well as external HTTP endpoints, allowing you to connect your
APIs to backend services, such as AWS Lambda functions, Amazon EC2 instances, or
Amazon DynamoDB tables. This enables you to build serverless architectures or
leverage existing resources in your infrastructure.

Security and Authorization: API Gateway provides various mechanisms to secure
your APIs, including token-based authentication, OAuth, and AWS Identity and
Access Management (IAM) integration. You can control access to your APIs at
different levels, such as API key, AWS IAM roles, or custom authorization
mechanisms.

Scalability and High Availability: API Gateway is designed to handle high
traffic and provides built-in scalability and fault tolerance. It automatically
scales to accommodate the incoming requests and can distribute the load across
multiple Availability Zones for increased availability.

Monitoring and Analytics: API Gateway offers robust monitoring capabilities,
including request/response logging, performance metrics, and customizable
logging with Amazon CloudWatch. You can use these insights to track API usage,
troubleshoot issues, and optimize performance.

Developer Portal: API Gateway provides a customizable developer portal where you
can document and showcase your APIs to developers. It allows you to publish API
documentation, provide code samples, and manage developer access and
subscription plans.
