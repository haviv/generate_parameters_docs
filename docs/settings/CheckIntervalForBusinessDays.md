# Check Interval For Business Days

**Technical Name:** CheckIntervalForBusinessDays

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

A parameter utilized within the Pathlock Cloud GRC platform to define the frequency of checks or actions specifically within business days. This setting ensures that workflow activities or security checks are aligned with working days, excluding weekends and possibly holidays, depending on the organization's configuration.

**Business Impact:**

Configuring this parameter enhances the operational efficiency of business workflows by ensuring that automated processes and checks are scheduled during business days. It mitigates the risk of delays in critical compliance or security operations that might otherwise occur over non-business days. This setting is crucial for organizations looking to optimize workflow executions and maintain regular monitoring within their governance, risk, and compliance infrastructure.

**Technical Impact when configured:**

When configured, this parameter instructs the system to execute certain workflow steps or actions only on designated business days. This can include, but is not limited to, the timing of automated reminders, compliance checks, or security audits, thus preventing any scheduled actions from occurring on weekends or non-working days.

**Examples Scenario:**

- **Automated Compliance Reminders:** If a compliance check workflow is due to execute every 5 business days, configuring this parameter ensures the system schedules these checks strictly on business days, avoiding weekends and ensuring compliance tasks are aligned with staff availability.
  
- **Security Audit Schedules:** For organizations that perform regular security audits through the Pathlock platform, setting this parameter ensures that audit-related workflows are initiated on business days, facilitating immediate attention and response from the relevant personnel.

**Related Settings:** 

- `CommonSettings.Default.CheckDeletedUsersByAttributeInWorkflowScheduledActions`: This setting might be related in terms of how workflow actions, including those that consider business days, handle user accounts marked for deletion.

**Best Practices:** configure when

- Implementing workflow actions that necessitate attention or execution during standard business operations.
- Scheduling automated compliance checks or security audits that require immediate personnel intervention.

avoid when

- The workflow or process is not impacted by the day of execution, such as non-time-sensitive data processing tasks.