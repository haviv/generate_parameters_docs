# Workflow Type to Lock User Accounts

**Technical Name:** LockUserWorkflowTypeId

**Category:** User Management

**Default Value:** N/A

**Impact Level:** High

**Description:**

The `LockUserWorkflowTypeId` parameter is used to identify and configure the specific workflow type within the Pathlock Cloud GRC platform that is responsible for automatically locking user accounts under certain conditions. This parameter is integral for enhancing security measures and ensuring compliance by preventing unauthorized access to sensitive information and systems.

**Business Impact:**

Misconfiguration or incorrect usage of this parameter can lead to unauthorized access to critical systems or unintentional lockout of legitimate users, potentially interrupting business operations and impacting productivity. Proper configuration helps maintain the integrity and security of user data while assisting in regulatory compliance and mitigating the risk of data breaches.

**Technical Impact when configured:**

- Ensures targeted and automatic locking of user accounts considered risky or having violated specific compliance rules.
- Supports adherence to security policies and regulatory requirements.
- Helps in preemptively mitigating potential threats by swiftly revoking access rights when suspicious activity is detected.

**Examples Scenario:**

For example, if an employee’s role in the financial department grants them access to sensitive financial records, the `LockUserWorkflowTypeId` can be configured to automatically lock their account if anomalous behaviors suggesting a potential security threat (e.g., failed login attempts or accessing data at unusual hours) are detected. This immediate reaction helps prevent unauthorized data exposure.

**Related Settings:**

N/A

**Best Practices:** 

- **Configure when:** Implementing a proactive security measure for automatically managing user account access based on predefined risk triggers or compliance violations.
- **Avoid when:** Insufficient data or understanding of the operational impact might lead to unnecessary business interruptions due to the unwarranted locking of user accounts.