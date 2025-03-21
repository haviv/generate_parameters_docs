# Employees Not Saved Email Address

**Technical Name:** EmployeesNotSavedEmailAddress

**Category:** HR

**Default Value:**

**Impact Level:** High

**Description:**

The EmployeesNotSavedEmailAddress parameter is used to flag instances where new or existing employees' email addresses are not saved during the synchronization process in the organization's employee directory. It helps in identifying and managing employees without registered email addresses in the system.

**Business Impact:**

Not having an email address saved for employees can significantly impact communication efficiency, emergency contact protocols, and access to digital resources. It can delay the distribution of critical information, hinder workflow processes, and affect compliance with communication policies.

**Technical Impact when configured:**

When configured, this parameter can trigger alerts or workflows designed to update employee records, ensuring that all employees have email addresses recorded. This can facilitate more efficient HR processes, improve communication strategies, and support compliance and security protocols by ensuring all employees are reachable via their corporate email.

**Examples Scenario:**

An HR administrator runs a monthly report to identify any employees who were recently added to the system without an email address. Utilizing the EmployeesNotSavedEmailAddress parameter, they are able to quickly pinpoint these entries and work with department managers to update the necessary information, ensuring all employees have access to internal communications and resources.

**Related Settings:**

- EmergencyAccessReportTemplateId

**Best Practices:** 

- **Configure when:** Setting up or maintaining employee records in the organization's HR system to ensure all employees have email addresses for communication and access purposes.
  
- **Avoid when:** All employee records are guaranteed to have email addresses, or when the organization uses alternative primary communication methods outside of email.