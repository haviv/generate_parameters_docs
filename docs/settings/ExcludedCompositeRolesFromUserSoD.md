**Excluded Composite Roles From User SoD**

**Technical Name:** ExcludedCompositeRolesFromUserSoD

**Category:** SOD (Segregation of Duties)

**Default Value:**

**Impact Level:** Medium

**Description:**
This configuration parameter allows for specific composite roles to be excluded from the Segregation of Duties (SoD) checks within the Pathlock Cloud GRC platform. A composite role is considered a grouping of individual roles that a user can be assigned. Excluding certain composite roles from SoD checks can be necessary for roles that inherently require cross-functional access, which might otherwise be flagged as a violation.

**Business Impact:**
Using this parameter helps in fine-tuning the SoD controls by excluding roles that are designed to span across multiple domains or functionalities which are essential for certain users or group of users to perform their job effectively. This ensures that security checks are aligned with business needs without compromising on compliance and governance standards.

**Technical Impact when configured:**
When composite roles are excluded from the user SoD checks, the system will not flag any potential segregation of duties conflict arising from these roles. It accelerates the user access review process by reducing the number of false positives, thus focusing on the real SoD violations that need remediation.

**Examples Scenario:**
- A role designed for system administrators that includes access to both system configuration settings and user account management might be excluded to prevent unnecessary flags for SoD conflicts, given the nature of administrative duties.
  
**Related Settings:**
- WorkflowMailIncludeChildRequestsInApprovalFlow: This setting impacts how child requests are included in the approval flow for workflow mails, which could interplay with how SoD checks are communicated or enforced in workflows involving role assignments.

**Best Practices:** configure when roles are specifically designed with cross-functional access necessary for job roles, avoid when the exclusion of roles can compromise the integrity of segregation of duties control.