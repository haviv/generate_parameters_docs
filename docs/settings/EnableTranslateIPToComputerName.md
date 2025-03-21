**Enable Translate IP To Computer Name**

**Technical Name:** EnableTranslateIPToComputerName

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether the Pathlock Cloud GRC platform attempts to resolve IP addresses to their corresponding computer names within the network. Enabling this feature enhances the visibility and readability of log and activity records by replacing numeric IP addresses with more recognizable computer names.

**Business Impact:**

Turning on IP to computer name translation can significantly improve the understanding of activity logs for security and audit purposes. It allows security teams to quickly identify which machines are involved in certain actions or behaviors without the need to cross-reference IP addresses manually. This can speed up incident response times and simplify the audit trail review process.

**Technical Impact when configured:**

When enabled, this setting affects how activity records are displayed in system logs, particularly in environments where transaction codes (TCode) and user activities are monitored, such as in SAP systems. It enhances the detail available in the logs by providing the computer names alongside other transaction details, making it easier for administrators and security teams to pinpoint the source of activity.

**Examples Scenario:**

A security team is investigating unauthorized access to sensitive data. With the `EnableTranslateIPToComputerName` parameter enabled, the logs show that the access attempt came from a computer named "FinanceDeptPC" instead of just displaying an IP address. This immediate context allows the security team to quickly identify the potential origin of the threat within the organization.

**Related Settings:**

- EnableSM20LogRead

**Best Practices:** 

- **Configure when:** You have a clear naming convention for computers within the network that can add meaningful context to security and audit logs.
  
- **Avoid when:** Your network uses dynamically assigned IP addresses without a clear and consistent naming convention for devices, as this might not add meaningful value and could lead to confusion.

