# Disable Init Last Use Of Activity

**Technical Name:** DisableInitLastUseOfActivity

**Category:** Configuration

**Default Value:** (No default value provided in the code references)

**Impact Level:** Low

**Description:**

The "Disable Init Last Use Of Activity" parameter controls whether the initialization of activities' last use tracking is enabled or disabled within the Pathlock Cloud GRC platform. It affects how user transactions and activities are logged and processed, particularly concerning their first and last usage timestamps.

**Business Impact:**

Disabling the initialization for last use of activity can impact auditing and monitoring capabilities. It might hinder the organization's ability to track the precise usage of various activities within applications, which can be crucial for compliance auditing, suspicious activity detection, and understanding user behavior.

**Technical Impact when configured:**

When this parameter is configured to disable the initialization, the system will not record or update the last use timestamps for activities. This may lead to a lack of data regarding when specific activities were last utilized, potentially affecting security audits and compliance reporting.

**Examples Scenario:**

An organization might wish to disable this feature to improve system performance if tracking the last use of activities is not a compliance requirement or if it's determined that the performance impact of logging this information outweighs the benefits.

**Related Settings:**

- `SapConnectorUserFilterForInclude`

**Best Practices:** Configure this parameter to disable initialization only when necessary, such as when performance issues are observed and tracking the last use of activities is not a critical requirement. Otherwise, keeping this feature enabled is advised to ensure comprehensive activity tracking for security and compliance purposes.