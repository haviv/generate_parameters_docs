# Enable Apply Changes To Derived Role

**Technical Name:** EnableApplyChangesToDerivedRole

**Category:** Configuration

**Default Value:** Not Provided

**Impact Level:** High

**Description:**

The `EnableApplyChangesToDerivedRole` parameter plays a crucial role in the governance, risk, and compliance (GRC) operations within the Pathlock Cloud GRC platform. This setting determines whether changes applied to a parent role automatically propagate to all derived (or child) roles within the system. It ensures that role-based access control (RBAC) policies remain consistent and up-to-date across an organization's IT environment.

**Business Impact:**

Enabling this feature streamlines the process of updating access permissions, significantly reducing the administrative overhead associated with manually applying changes to each derived role. It contributes to maintaining a robust security posture, ensuring that only authorized users have access to sensitive information and critical systems, thereby mitigating potential security risks.

**Technical Impact when configured:**

When enabled, any modifications made to a parent role are automatically applied to its derived roles, ensuring quick and consistent updates across the organization's roles hierarchy. This automatism is crucial for maintaining compliance with internal and external security policies and regulations.

**Examples Scenario:**

Consider an organization that utilizes a hierarchical role model within its IT systems. Suppose there is a need to revoke access to a specific resource from a parent role due to a changed regulatory requirement. By enabling `EnableApplyChangesToDerivedRole`, this access revocation is automatically mirrored in all derived roles, ensuring the organization stays compliant without the need for individual role adjustments.

**Related Settings:** WorkflowMailIncludeChildRequestsInApprovalFlow

**Best Practices:** 

- **Configure when:** You have a complex role hierarchy and need to ensure consistent permission updates across all derived roles efficiently.
- **Avoid when:** Each derived role requires customized access control that should not be automatically overwritten by changes in parent roles.