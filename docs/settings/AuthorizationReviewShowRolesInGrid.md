**Authorization Review Show Roles In Grid**

**Technical Name:** AuthorizationReviewShowRolesInGrid

**Category:** Audit

**Default Value:** Not provided in the code references.

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of user roles within grid views in Authorization Certifications details pages. When enabled, it allows for a more granular view of user permissions and roles directly from the grid interface, enhancing the audit and review process within Pathlock's GRC platform.

**Business Impact:**

Enabling the display of roles in grid views significantly streamlines the process of reviewing user authorizations. It provides auditors and administrators with a quick, comprehensive overview of user roles and permissions, facilitating faster decision-making during audits and compliance reviews. This can lead to improved security posture and compliance with regulatory requirements by ensuring only the necessary permissions are granted.

**Technical Impact when configured:**

Once configured, the 'Authorization Review Show Roles In Grid' feature impacts the UI rendering of authorization certification details pages. It modifies how information is presented to the user, potentially loading additional data into the grid. This ensures that users can see roles associated with each account or user without navigating away from the audit trail, improving efficiency in user authorization reviews.

**Examples Scenario:**

- **Audit Preparation:** Preparing for an internal or external audit, an administrator enables this feature to quickly review and confirm the accuracy of user roles and permissions, ensuring they adhere to the principle of least privilege.
  
- **Compliance Review:** During routine compliance checks, this parameter is enabled to facilitate the verification of user access rights, making it easier to demonstrate compliance with regulations such as GDPR, SOX, or HIPAA.

**Related Settings:** WorkflowExportIncludeApprovalGroups

**Best Practices:** 

- **Configure when:** Preparing for audits or compliance reviews to streamline the review process.
- **Avoid when:** The additional information might overwhelm users or when the system performance is a concern due to large datasets being loaded on the grid.