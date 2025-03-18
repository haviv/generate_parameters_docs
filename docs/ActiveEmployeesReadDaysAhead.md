# Active Employees Read Days Ahead

**Technical Name:** ActiveEmployeesReadDaysAhead

**Category:** User Management

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

This parameter defines the number of days ahead of the current date that the system should consider when reading active employee data from an ERP system, specifically for the purpose of preparing or updating organizational structure within the Pathlock Cloud GRC platform.

**Business Impact:**

Configuring this parameter helps organizations to proactively manage their employee data by including soon-to-be active employees into the organizational structure. This can significantly improve planning for user access rights, compliance checks, and risk assessments, ensuring no gaps as employees transition into their roles.

**Technical Impact when configured:**

When configured, this parameter allows the Pathlock Cloud GRC platform to fetch and prepare data for employees who are marked as active within the specified days ahead of the current date in ERP systems like SAP HCM. This preemptive data fetch helps in smooth transitions and maintenance of accurate, real-time organizational data, enhancing the system’s effectiveness in managing security, risk, and compliance.

**Examples Scenario:**

An organization has a policy to prepare user access and compliance checks 10 days before an employee starts. By setting the `ActiveEmployeesReadDaysAhead` parameter to 10, the Pathlock Cloud GRC platform begins processing this data ahead of time, ensuring the system is prepared for the new employee's start date.

**Related Settings:** Not provided

**Best Practices:** 
- **Configure when:** There's a clear understanding of the organization's onboarding process length and upcoming employment start dates are known ahead of time.
- **Avoid when:** The organization does not have a fixed onboarding schedule or if employee data is frequently subject to last-minute changes.