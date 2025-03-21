# Authorization Review For Position Change Run For All Online Systems

**Technical Name:** AuthorizationReviewForPositionChangeRunForAllOnlineSystems

**Category:** Compliance

**Default Value:** False

**Impact Level:** High

**Description:**

This parameter controls whether the authorization review process should be executed for all online systems during a position change within the organization. It ensures that the access rights and authorizations of individuals are evaluated and approved as part of the internal compliance process.

**Business Impact:**

When enabled, this parameter ensures that employee access rights are appropriately aligned with their new position, minimizing the risk of unauthorized access and maintaining compliance with security policies. It supports regulatory compliance by enforcing a thorough review of access permissions whenever there are personnel changes.

**Technical Impact when configured:**

If set to True, the system will automatically trigger an authorization review process for all associated online systems whenever there is a change in an employee's position. This is critical for preventing privilege escalation and ensuring that the principle of least privilege is maintained.

**Examples Scenario:**

- **Scenario:** A manager is promoted to a senior manager, which entails access to more sensitive systems.
  - **Without the parameter:** The user's access rights might not be reviewed, potentially leaving them without necessary access or allowing access to systems no longer relevant to their role.
  - **With the parameter enabled:** A comprehensive review is initiated, adjusting the individual's access rights to align with their new role, thereby maintaining security and compliance.

**Related Settings:**

- EnableJobFailedRead
- AuthorizationReviewDisableSubmitApproval

**Best Practices:** 

- **Configure when:** Implementing or maintaining strict compliance standards, especially in regulated industries, or when high volumes of position changes occur frequently within the organization.
- **Avoid when:** The organization operates in an environment where position changes are infrequent or the review process for access rights is managed manually or through another system.