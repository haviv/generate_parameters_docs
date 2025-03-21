# Event For Employee Changed Enable For Employee Without Users

**Technical Name:** EventForEmployeeChangedEnableForEmployeeWithoutUsers

**Category:** User Management

**Default Value:** True

**Impact Level:** Medium

**Description:**

This parameter enables the tracking and handling of events related to employees who do not have associated user accounts within the system. It is designed to ensure that employee-related changes are captured and processed accurately, even if the employee does not have a direct user account in the Pathlock Cloud GRC platform.

**Business Impact:**

Enabling this feature allows organizations to maintain comprehensive oversight of all employee changes, enhancing the integrity of audit trails and supporting compliance with internal policies and regulatory requirements. It ensures that actions related to employees, including those without system user accounts, are monitored and recorded, aiding in governance and risk management efforts.

**Technical Impact: when configured**

When configured, this setting initiates additional checks and processes within the system to capture and process events for employees without user accounts. It modifies the event handling logic to consider these scenarios, ensuring that relevant data is collected and available for audit or compliance purposes.

**Examples Scenario:**

An organization has employees who are not assigned user accounts in the Pathlock GRC platform but still undergo changes in their employment status or other personnel-related updates. With this parameter enabled, any changes to these employees' records are tracked and processed, ensuring they are included in compliance reports and audit trails, thus maintaining the integrity of the governance, risk, and compliance data. 

**Related Settings:** 

- SwitchBackToOriginalUserAfterEmergencyAccess

**Best Practices:** 

- **Configure when:** You have employees within your organization who do not have user accounts in the Pathlock Cloud GRC platform but for whom you need to track changes for compliance, audit, and governance purposes.
  
- **Avoid when:** All employees in your organization have user accounts, or there is no requirement to track changes for employees without user accounts, to reduce unnecessary system processing and overhead.