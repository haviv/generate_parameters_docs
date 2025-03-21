# Update Cache Period

**Technical Name:** UpdateCachePeriod

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Update Cache Period parameter is utilized to define the frequency at which the system cache is refreshed. This ensures that the data users interact with is up-to-date and accurate, reflecting the latest changes within the Pathlock GRC platform.

**Business Impact:**

Setting an appropriate cache update period is critical for ensuring that business processes reliant on current compliance, risk, and security data operate effectively. A well-configured cache update interval supports timely decision-making and helps in maintaining the integrity of the GRC environment by providing users with the most recent data.

**Technical Impact when configured:**

- Enhanced system performance by reducing the load on servers for constantly retrieving the most recent data.
- Improved user experience as a result of quicker access to updated information.
- Optimization of data consistency across the GRC platform, helping in accurate reporting and analysis.

**Examples Scenario:**

In a scenario where a company undergoes frequent changes in compliance regulations, setting a shorter cache update period would ensure that users always have access to the latest compliance guidelines, thus aiding in maintaining high compliance standards.

**Related Settings:**

- TransactionAttribute4ColumnHeader
- TransactionCodeMaxLength

**Best Practices:** 

- Configure to a shorter period when immediate data update is essential for compliance and decision-making.
- Avoid setting too short of an update period for large datasets to prevent potential system performance issues.