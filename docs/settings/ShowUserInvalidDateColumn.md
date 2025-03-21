# Show User Invalid Date Column

**Technical Name:** ShowUserInvalidDateColumn

**Category:** Reporting

**Default Value:** False

**Impact Level:** Low

**Description:**

This parameter controls the visibility of the "User Invalid Date" column in various reporting views within the Pathlock Cloud GRC platform. When enabled, it allows for the display of dates that are considered invalid for user-related events or attributes.

**Business Impact:**

Enabling this feature can help organizations identify and investigate discrepancies in user date-related data quickly. It is particularly useful for audit and compliance purposes, where understanding the timeline of user activities and attributes (such as account creation or last login dates) is critical.

**Technical Impact when configured:**

When this parameter is configured to true, the system will include a separate column in the reports generated that showcases invalid date data related to users. This can aid in the detailed analysis of user behavior and attribute integrity over time.

**Examples Scenario:**

A company undergoes a security audit, and auditors request information on accounts with incorrect or suspicious last logon dates. By enabling this parameter, the audit team can quickly generate reports that include the "User Invalid Date" column, facilitating the identification of potential security issues.

**Related Settings:** 

- DisableEmployeeHRDataCollection

**Best Practices:** configure when performing audits or investigating user data integrity issues, avoid when such detailed analysis is unnecessary as it may clutter reports with additional data.