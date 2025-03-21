**Technical Name:** ServerDiscrepancyEmailSubject

**Category:** Configuration

**Default Value:** Notify about application servers discrepancy:

**Impact Level:** Medium

**Description:**

Defines the subject line for email notifications sent by the Pathlock Cloud GRC platform when discrepancies between application servers listed in the profile tailor and those actually in use are detected. This setting ensures administrators are promptly informed about mismatches, enabling quick response to potential security, compliance, or operational issues.

**Business Impact:**

Effective monitoring and management of server discrepancies directly impact the organization's security posture and compliance status. Timely alerting via email helps in maintaining the integrity of the IT infrastructure, preventing unauthorized access or changes, and ensuring that all application servers are correctly accounted for in security audits.

**Technical Impact when configured:**

When this parameter is configured, email alerts generated in response to application server discrepancies will use the defined subject line, making them easily identifiable in the administrators' inbox. This facilitates quicker recognition and prioritization of issues related to server mismatches.

**Examples Scenario:**

If the platform detects that there are servers listed in the profile tailor that do not match the application servers currently in use, it triggers an email alert. If the `ServerDiscrepancyEmailSubject` is set to "Critical Server Configuration Alert," the email received by administrators will carry this subject, indicating the urgency and nature of the issue, thereby prompting an immediate review and action.

**Related Settings:** SendMailOnApplicationServerDiscrepancies

**Best Practices:** configure when

- Immediate identification of discrepancy-related emails is required by administrators.
- There's a need to categorize and prioritize discrepancy alerts among other email notifications.

avoid when

- Default subject lines suffice for organization's email alert management practices.