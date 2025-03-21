# Disable SoD Approval By Same User

**Technical Name:** DisableSoDApprovalBySameUser

**Category:** SOD

**Default Value:** Not specified

**Impact Level:** High

**Description:**

The parameter 'DisableSoDApprovalBySameUser' is designed to prevent users from approving their own Segregation of Duties (SoD) mitigations. This setting ensures that the approval process for SoD mitigations involves a second party, promoting internal controls and regulatory compliance.

**Business Impact:**

Enabling this parameter strengthens the internal control environment by ensuring that mitigations for potential SoD violations are reviewed and approved by a separate individual other than the one who requests the mitigation. This reduces the risk of fraudulent activities and enhances the organization's compliance with audit and governance standards.

**Technical Impact when configured:**

When this parameter is set, the system will restrict the same user from both initiating and approving SoD mitigation requests. This enforces a dual control mechanism, where a different user must approve the mitigations, thus increasing the integrity of the segregation of duties process within the system.

**Examples Scenario:**

- An employee in the finance department requests a mitigation for an SoD conflict they have identified. If 'DisableSoDApprovalBySameUser' is enabled, the employee cannot also approve their own request. Instead, the approval must come from another authorized individual, ensuring an unbiased review process.

**Related Settings:**

- SystemsWithoutLastLogon: While not directly related, understanding settings that deal with user management and security protocols can complement the configuration of 'DisableSoDApprovalBySameUser.'

**Best Practices:** configure when an organization's SoD policy requires independent verification and approval of mitigations to prevent potential conflict of interest and reduce fraud risk. Avoid when the organization is small and such controls could hinder operational efficiency due to the limited number of users.