# Custom Sql Query For Rest API HR Data Source Secondary

**Technical Name:** Custom_Sql_Query_For_Rest_API_HR_DataSource_Secondary

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** 

Enables the customization of SQL queries used for interacting with secondary HR data sources via REST API. This parameter allows for the fine-tuning of data queries to match specific business requirements and optimize performance.

**Business Impact:**

Customizing SQL queries for secondary HR data sources can lead to more efficient data retrieval, better alignment with organizational reporting needs, and improved decision-making processes. By tailoring queries, businesses can ensure that the data extracted is relevant, leading to enhanced analytics and insights.

**Technical Impact when configured:**

When configured, this parameter directly affects how data is queried and retrieved from secondary HR data sources. It enables the extraction of specific datasets that are most relevant to the organization's needs, potentially enhancing the performance of HR-related reports and analytics.

**Examples Scenario:**

A company uses a generic SQL query for all its HR data sources. However, for a secondary HR system that stores data in a unique format, the generic query does not capture critical data efficiently. By customizing the SQL query using this parameter, the company can ensure that data extraction from the secondary system is optimized, accurate, and relevant to their specific reporting needs.

**Related Settings:**

- **AuthorizationReviewMaxThreadCount**: While not directly related to SQL queries, tuning this setting may help manage the system's performance when executing customized SQL queries, especially when dealing with large datasets.

**Applicable Workflows Actions:**

**Best Practices:** 

- **Configure when:** You need to optimize data retrieval from secondary HR data sources or when the default query does not meet your specific data requirements.
- **Avoid when:** The default SQL query configuration meets your organizational needs, or if you do not have the expertise to customize SQL queries safely and efficiently. Misconfiguration can lead to data retrieval issues, impacting system performance and accuracy.