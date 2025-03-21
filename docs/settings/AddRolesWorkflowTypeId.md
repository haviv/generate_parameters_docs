# Workflow Type to Add Roles to User

**Technical Name:** AddRolesWorkflowTypeId

**Category:** User Management

**Default Value:** Not specified

**Impact Level:** High

**Description:**

This parameter is used within the Pathlock Cloud GRC platform to determine the specific workflow type responsible for managing the process of adding roles to users. It ensures that roles are provisioned in a controlled and auditable manner, aligning with compliance and governance requirements.

**Business Impact:**

Utilizing the correct workflow type when adding roles to users directly influences the organization's ability to enforce access control and adhere to security policies. It ensures that only authorized users gain access to specific functions and data, thus minimizing the risk of unauthorized access and potential security breaches.

**Technical Impact when configured:**

When properly configured, this parameter ensures seamless integration with the system's user management processes, enforcing consistency and accountability in how roles are assigned. It empowers administrators to maintain an accurate and compliant access control environment.

**Examples Scenario:**

- **Enhancing Security Posture:** An organization needs to update access privileges for a group of users to restrict access to sensitive financial records. By using the `AddRolesWorkflowTypeId`, they can ensure these changes are managed through a predefined, secure workflow, providing an auditable trail of who was granted access, when, and by whom.

- **Compliance Requirements:** To meet GDPR compliance, a company must ensure that access to personal data is tightly controlled and monitored. By employing the specified parameter for role addition workflows, the company can demonstrate adherence to strict access control policies, reducing the risk of compliance violations.

**Related Settings:**

- `ProfileTailorContext.Context.SystemCode` - This setting might be indirectly related as it specifies the system code used in the context of adding roles, potentially affecting the overall workflow process.

**Best Practices:** 

- **Configure when:** Setting up or revising user access control policies, especially when introducing new roles or adjusting existing access rights as part of compliance or security enhancement initiatives.
  
- **Avoid when:** If the process does not require auditability or when using ad-hoc, manual processes for user role assignment outside of the regulatory or compliance scope.