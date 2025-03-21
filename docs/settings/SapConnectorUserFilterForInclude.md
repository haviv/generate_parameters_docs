# Sap Connector User Filter For Include

**Technical Name:** SapConnectorUserFilterForInclude

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter specifies a user-defined filter for including specific user groups in SAP connector operations. It allows for a more granular control over which user data is processed and synchronized by Pathlock’s GRC solutions.

**Business Impact:**

Applying this filter ensures that only relevant user groups are included in GRC monitoring and management tasks, which optimizes system performance, improves the accuracy of compliance reporting, and enhances security by focusing on specified user segments.

**Technical Impact when configured:**

Once configured, the parameter influences how the SAP connector aggregates user data, directly affecting the scope of GRC activities such as risk analysis, compliance checks, and audit reporting within the Pathlock platform. It enables targeted data processing, reducing overhead and refining compliance and security outcomes.

**Examples Scenario:**

A company wishes to exclude all users except for those in specific administrative and financial roles from their GRC monitoring processes to streamline compliance checks and risk assessments. By setting the `SapConnectorUserFilterForInclude` parameter to include only the relevant SAP user groups, the company can ensure that their GRC activities are both efficient and focused.

**Related Settings:**

- `SapConnectorUserGroupForExclude`

**Best Practices:** 

- **Configure when:** There is a clear requirement to include specific user groups for GRC processes, enabling targeted monitoring and management.
- **Avoid when:** No specific user groups need to be isolated for GRC processes, to maintain broad and comprehensive security and compliance oversight.