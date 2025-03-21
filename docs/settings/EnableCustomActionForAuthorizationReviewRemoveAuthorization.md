# Enable Custom Action For Authorization Review Remove Authorization

**Technical Name:** EnableCustomActionForAuthorizationReviewRemoveAuthorization

**Category:** Workflow

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

This parameter enables a custom action within the Authorization Review process to remove authorizations. It is part of the Pathlock GRC platform's workflow management, specifically within the context of authorization certification.

**Business Impact:**

Enabling this parameter allows organizations to customize their authorization review process, providing flexibility to meet specific compliance and governance requirements. It impacts how authorizations are managed and reviewed, ensuring that only appropriate users have access to critical systems and data, which is essential for maintaining security standards and compliance regulations.

**Technical Impact when configured:**

When configured, this setting allows for the integration of custom actions into the workflow for reviewing and removing authorizations. This can streamline the process of managing user access, making it easier to enforce security policies and compliance requirements.

**Examples Scenario:**

- **Compliance Reviews:** During periodic access reviews, an organization wants to integrate a custom step that automatically removes access for users failing compliance checks. Enabling this parameter allows for such an integration, aligning with internal compliance policies.
- **Security Response:** In response to an identified security threat or breach, a company may need to quickly revoke specific authorizations. With this setting enabled, they can incorporate custom actions into the authorization review process to expedite the removal of access.

**Related Settings:**

- `CustomActionIdForAuthorizationReviewRemoveAuthorization` is directly related and specifies the unique identifier for the custom action to be used.

**Best Practices:** configure when - the organization requires flexible, automated processes to manage user authorizations securely and efficiently. Avoid when - default authorization review processes meet the organization’s requirements, and additional customization is unnecessary or could complicate workflow management.