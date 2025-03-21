# Data Exceptions Batch Size

**Technical Name:** DataExceptionsBatchSize

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter defines the size of the batch when processing data exceptions in the Pathlock Cloud GRC platform. It determines how many data exceptions can be processed in a single batch, optimizing performance and resource utilization during the data monitoring and exception handling processes.

**Business Impact:**

Setting an appropriate batch size for data exceptions is crucial for maintaining system performance and ensuring timely and efficient handling of exceptions. Too large a batch size may result in prolonged processing times and increased system load, potentially delaying actions on critical exceptions. Conversely, too small a batch size could lead to underutilization of system resources, making the exception handling process less efficient.

**Technical Impact when configured:**

Proper configuration of the `DataExceptionsBatchSize` parameter can significantly enhance system performance by balancing the load and optimizing the processing time of data exceptions. It ensures that the system can handle large volumes of exceptions without compromising on processing speed or resource utilization.

**Examples Scenario:**

Consider a scenario where the Pathlock Cloud GRC platform is monitoring transaction data for exceptions that might indicate potential compliance issues. If the `DataExceptionsBatchSize` is set to a high value, the system can quickly process a large volume of transactions, identifying and reporting exceptions without significant delays, thus aiding timely compliance intervention.

**Related Settings:**

- Custom_Sql_Query_For_Rest_API_HR_DataSource_Secondary

**Best Practices:** configure when the system is expected to process a high volume of exceptions to optimize performance and resource utilization, avoid when the system is under heavy load to prevent potential performance degradation.