# Authorization Review For Position Change Title

**Technical Name:** AuthorizationReviewForPositionChangeTitle

**Category:** Compliance

**Default Value:** Not Provided

**Impact Level:** High

**Description:**

The Authorization Review For Position Change Title is a critical parameter within the Pathlock Cloud GRC platform, designed to trigger a review process whenever there is a change in an employee's position. This review ensures that the change aligns with organizational compliance and security policies.

**Business Impact:**

Utilizing this parameter helps in maintaining strong internal control systems by preventing unauthorized access and ensuring that the right individuals have access to sensitive information and systems. This is pivotal in mitigating risks associated with fraud, data breaches, and non-compliance with regulations.

**Technical Impact when configured:**

When this parameter is enabled, it automatically initiates a comprehensive authorization review process for any position change within the organization. This includes validating the change against predefined security and compliance policies to ensure the new position alignment does not introduce any compliance risks.

**Examples Scenario:**

For instance, when an employee is promoted from a non-sensitive position to a sensitive one that requires access to financial data, the Authorization Review For Position Change Title parameter would trigger a review process to confirm the employee's eligibility and adherence to compliance standards for the new role.

**Related Settings:**

- AuthorizationReviewForPositionChangeEnable
- AuthorizationReviewForPositionChangeTemplateId

**Best Practices:** configure when an organization wants to enhance its control over position-based access rights. Avoid when the process may cause unnecessary delays in routine position changes where compliance risks are already mitigated through other controls.