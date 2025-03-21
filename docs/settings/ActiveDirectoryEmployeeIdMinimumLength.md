# Active Directory Employee Id Minimum Length

**Technical Name:** ActiveDirectoryEmployeeIdMinimumLength

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The ActiveDirectoryEmployeeIdMinimumLength parameter specifies the minimum number of characters required for an employee ID within the Active Directory integration context. This setting ensures that employee IDs adhere to organizational policies for length, contributing to consistent identity management practices. 

**Business Impact:**

Setting an appropriate minimum length for employee IDs can enhance security by preventing the use of overly simplistic or easily guessable IDs. It also supports compliance with internal and external regulations that may dictate specific requirements for identification length. 

**Technical Impact when configured:**

When configured, this parameter enforces the validation of employee ID length during user account synchronization or creation processes within the Active Directory. If an employee ID does not meet the specified minimum length, the related action (e.g., user account creation) may be rejected or flagged for review.

**Examples Scenario:**

- **Compliance Requirement:** If an organization operates under regulations requiring specific standards for identification numbers, configuring the ActiveDirectoryEmployeeIdMinimumLength ensures that all employee IDs within the AD conform to these standards, thus avoiding non-compliance penalties.
- **Security Policy:** To strengthen security measures, an organization decides that all identification numbers, including employee IDs, must be at least 8 characters long to reduce the risk of ID-related security breaches.

**Related Settings:**

- OrganizationStructureProviderType
- ReadActiveDirectoryEmployeeId

**Best Practices:** 

- **Configure when:** Establishing initial integration with Active Directory or when updating ID management policies to align with new security, compliance, or organizational standards.
- **Avoid when:** Employee ID length does not correlate with security or compliance requirements, or when such enforcement may disrupt established workflows or legacy systems incompatible with the change.