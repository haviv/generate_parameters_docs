# Request Declined

**Technical Name:** RequestDeclined

**Category:** Workflow

**Default Value:** Not applicable

**Impact Level:** Medium

**Description:** The parameter is used to trigger specific actions or behaviors within workflow processes when a request within the Pathlock GRC platform has been declined.

**Business Impact:** Helps in managing and tracking the workflow of authorization requests, ensuring that any declined requests are properly noted and acted upon, maintaining the integrity and efficiency of security and compliance processes within the organization.

**Technical Impact when configured:** Proper configuration ensures that notifications, audits, and other related processes are triggered when a request is declined, facilitating better management of compliance and security measures.

**Example Scenario:** Suppose an employee requests access to a sensitive financial system. If the request is reviewed but ultimately declined, the RequestDeclined parameter triggers a workflow that could notify the requester, log the decision for auditing purposes, and potentially initiate a review process to understand why the access was not granted.

**Related Settings:**
- NotifyUserOnRequestStart
- EnableChooseRequestType

**Best Practices:** Configure the RequestDeclined parameter to ensure that all declined requests are processed according to your organization's security, risk management, and compliance policies. Avoid inconsistent configuration that may lead to untracked or poorly managed declined requests, which can pose security risks or compliance issues.