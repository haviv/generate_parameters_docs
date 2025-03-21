# User Multi User Max Number Of Users Per Computer

**Technical Name:** UserMultiUserMaxNumberOfUsersPerComputer

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter defines the maximum number of users allowed to use a single computer within an organization's network as identified in the Pathlock Cloud GRC platform. It is utilized in the context of generating reports to ensure compliance and manage user access effectively.

**Business Impact:**

Setting an appropriate value for this parameter helps in enforcing security policies regarding shared computer usage within an organization. It prevents excessive shared use of a single device, which can lead to security risks like unauthorized access or data leakage. Moreover, it assists in license management by ensuring the optimal use of software resources.

**Technical Impact when configured:**

When configured, this parameter directly influences the generation of user access reports by including data on the number of users per computer. It helps in identifying deviations from the set security policies by reporting computers that exceed the configured maximum user limit.

**Examples Scenario:**

- **Compliance Monitoring:** In a scenario where a company's policy restricts the number of users on a single workstation to 5 for security reasons, this parameter will help in identifying any workstation with user access exceeding this limit. It aids in maintaining compliance with internal security policies.
  
- **License Optimization:** For organizations that have software licenses based on the number of users per device, configuring this parameter helps in identifying instances where additional licenses may be required or where licenses can be optimized to reduce costs.

**Related Settings:**

- `ActiveDirectoryProviderWithExternalDataEmployeeLinkadgeField`
- `SapUserRoleBackTraceRoleFromGeneratedProfile`

**Best Practices:** 

- **Configure when:** There is a need to enforce security policies regarding shared computer usage, or to optimize software licenses based on the number of users per computer.
- **Avoid when:** If the organization does not utilize shared computers or if the management of user access does not rely on the number of users per device.