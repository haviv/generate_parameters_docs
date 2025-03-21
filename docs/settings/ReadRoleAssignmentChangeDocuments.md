# Read Role Assignment Change Documents

**Technical Name:** ReadRoleAssignmentChangeDocuments

**Category:** Audit 

**Default Value:**

**Impact Level:** Medium

**Description:**

The `ReadRoleAssignmentChangeDocuments` parameter is intended for use within the Pathlock Cloud GRC platform, facilitating the retrieval and examination of documents related to changes in role assignments within a given organizational context. Through leveraging this parameter, compliance and auditing teams can streamline the process of auditing role assignments, ensuring adherence to both internal policies and regulatory standards.

**Business Impact:**

Effective use of the `ReadRoleAssignmentChangeDocuments` parameter can significantly enhance an organization's ability to maintain strict compliance with security policies and regulatory requirements. By enabling a detailed review of role assignment changes, organizations are better positioned to identify unauthorized or erroneous modifications, thereby mitigating potential security risks and ensuring that only authorized personnel have access to sensitive information or systems.

**Technical Impact when configured:**

When configured, this parameter allows for the systematic collection and analysis of role assignment change documents. This aids in identifying discrepancies or deviations from established security policies, enabling timely corrective actions. Furthermore, it assists in maintaining an audit trail that is critical for internal audits or compliance reviews, enhancing transparency and accountability within the role management process.

**Examples Scenario:**

An organization needs to comply with strict financial regulations requiring detailed audit trails for access to financial systems. By employing the `ReadRoleAssignmentChangeDocuments` parameter, they can automatically gather and review documents evidencing any changes made to roles granting access to these systems. This ensures that any adjustments are properly authorized and documented, facilitating compliance with regulations such as SOX (Sarbanes-Oxley Act).

**Related Settings:** 

- `DisableSystemSelectionNarrowByUserGroups`

**Best Practices:** 

- **Configure when:** Establishing or updating audit trails is necessary for compliance or security policy enforcement. This is crucial for organizations with stringent regulatory requirements regarding role and access management.
  
- **Avoid when:** If the organization operates under less strict compliance requirements, or if the potential performance impact of tracking every role assignment change outweighs the benefits in security or compliance terms.