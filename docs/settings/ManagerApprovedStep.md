# Manager Approved Step

**Technical Name:** ManagerApprovedStep

**Category:** Workflow

**Default Value:** None

**Impact Level:** High

**Description:** The ManagerApprovedStep parameter is used to configure and manage the approval steps in workflow processes specifically related to email communication for approvals. 

**Business Impact:** Proper configuration of this parameter ensures that workflow processes involving manager approvals are streamlined and communicated effectively via email. It impacts how quickly and accurately approval requests are processed, directly affecting operational efficiency and compliance.

**Technical Impact when configured:** When configured, this parameter activates specific workflow mail listeners that are responsible for detecting and acting on manager approval keywords within email communications. This automation significantly reduces manual oversight and speeds up the approval process.

**Examples Scenario:** In a scenario where an employee requests access to sensitive financial records, the ManagerApprovedStep parameter ensures that an automated email is sent to the employee's manager for approval. Only upon receiving an approval response will the workflow proceed to grant access, ensuring security and compliance with internal policies.

**Related Settings:** WorkflowStatus

**Best Practices:** 
- **Configure when** you have a well-defined workflow that involves managerial approvals via email.
- **Avoid when** your approval processes do not rely on email communication or when automated approval handling might bypass necessary manual oversight.