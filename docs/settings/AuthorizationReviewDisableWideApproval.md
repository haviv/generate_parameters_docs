# Authorization Review Disable Wide Approval

**Technical Name:** AuthorizationReviewDisableWideApproval

**Category:** Workflow UI

**Default Value:**

**Impact Level:**

**Description:**

This parameter controls the functionality related to the approval process within the authorization review workflows on the Pathlock Cloud GRC platform. When enabled, it restricts the ability to perform wide approvals, making the approval process more granular and specific.

**Business Impact:**

Enabling this parameter has significant implications for security and compliance processes within an organization. It ensures that approvals for access changes, permissions, and other sensitive operations are conducted more meticulously, thereby increasing accountability and reducing the risk of unauthorized access or compliance violations.

**Technical Impact when configured:**

- Limits bulk approval actions, requiring approvers to assess each request individually.
- Enhances the safeguarding of sensitive operations by adding an extra layer of scrutiny.
- Supports compliance by aligning with principles of least privilege and separation of duties.

**Examples Scenario:**

An organization must comply with strict regulatory standards requiring detailed scrutiny of user access and permissions. By enabling the AuthorizationReviewDisableWideApproval parameter, the company can enforce a process where each access request or change must be individually reviewed and approved, ensuring compliance with regulatory requirements and mitigating the risk of unauthorized access.

**Related Settings:**

**Applicable Workflows Actions:** 

**Best Practices:** 

- **Configure when:** Tight control and detailed oversight of the approval processes are required, especially in highly regulated industries or for sensitive operations.
- **Avoid when:** Speed and efficiency in the approval process are prioritized over detailed control, and the risk level associated with the operations is low.