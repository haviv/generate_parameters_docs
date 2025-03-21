# Custom Action Template For Authorization Review Remove Authorization

**Technical Name:** CustomActionTemplateForAuthorizationReviewRemoveAuthorization

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter defines a custom action template utilized during the authorization review process, specifically designed for removing an authorization. It enables the specification of tailored actions in the review process for removing access rights from users or roles within the Pathlock Cloud GRC platform.

**Business Impact:**

Utilizing a custom action template for removing authorization can significantly streamline the review process, enhancing compliance and security within the organization. It ensures that unauthorized access is promptly identified and revoked, thereby minimizing potential security risks and compliance violations.

**Technical Impact when configured:**

When configured, this parameter influences the authorization review workflow by introducing customized steps or checks tailored to the organization's specific requirements for removing access rights. This customization can lead to more efficient authorization reviews, targeted removal actions, and improved compliance with security policies.

**Examples Scenario:**

In a scenario where an organization needs to revoke access rights from users who no longer require them, or who have changed roles, the custom action template for removing authorization can provide a streamlined process for identifying such cases and executing the revocation actions as part of the authorization review process.

**Related Settings:**

- `CUAPrefixForRfcDestinations`
- `ShowOrganizationUnitTypeInTree`

**Best Practices:** configure when you need specific, tailored actions during the authorization review process to remove access rights, enhancing security and compliance. Avoid when the default authorization review process meets the organization's needs without additional customization.