# Create Approval Group For Company Employee Record Query Active Directory For Each Manager

**Technical Name:** CreateApprovalGroupForCompanyEmployeeRecord_QueryActiveDirectoryForEachManager

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**

This parameter configures the creation of an approval group by querying Active Directory for each manager of a company's employee records during a workflow step. It ensures that the approval process is tailored to the organizational structure and that managers relevant to the employee's context are included in the approval chain.

**Business Impact:**

Implementing this parameter streamlines the approval process, making it more efficient and reducing the time taken for approvals. It ensures that only relevant managers are part of the approval process, which is critical for maintaining operational efficiency and enforcing proper controls within the organization's GRC (Governance, Risk Management, and Compliance) practices.

**Technical Impact when configured:**

- Dynamically creates approval groups based on the company's organizational hierarchy.
- Ensures approvals are routed to the correct managers by querying Active Directory, aligning with the company's structured approval chains.
- Enhances security by restricting approval to designated managers, thereby enforcing segregation of duties (SOD).

**Examples Scenario:**

An employee submits a request for access to a sensitive financial reporting tool. With this parameter configured, the system automatically queries Active Directory to identify the employee's direct manager and any higher-level managers required for approvals based on the company's policy. An approval group is then dynamically created, consisting of these managers, ensuring that the request is reviewed by all necessary parties before access is granted or denied.

**Related Settings:**

- `ShowApprovalGroupNameAsStepName`

**Best Practices:** Configure when implementing automated approval workflows where efficiency and compliance with organizational hierarchy are critical. Avoid when manual approval processes are preferred or in smaller organizations where automatic group creation may lead to inefficiencies or unnecessary complexity.