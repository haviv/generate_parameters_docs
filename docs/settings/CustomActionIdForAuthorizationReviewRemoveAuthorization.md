# Custom Action Id For Authorization Review Remove Authorization

**Technical Name:** CustomActionIdForAuthorizationReviewRemoveAuthorization

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**

The CustomActionIdForAuthorizationReviewRemoveAuthorization parameter is designed to define a specific action identifier used during the authorization review process. It plays a critical role in the Pathlock Cloud GRC platform by enabling administrators to specify custom actions that are to be deployed for removing authorizations from users as part of their compliance and risk management workflows.

**Business Impact:**

Configuring this parameter with the correct action ID directly impacts the organization's ability to manage user authorizations effectively, ensuring that only appropriate users have access to critical systems and data. It helps in tightening security measures and maintaining compliance with various regulatory standards by automating the removal of obsolete or unauthorized access rights.

**Technical Impact when configured:**

Upon configuration, this parameter interacts with the authorization certification business object (`AuthoirizationCertificationBO`) to trigger specific workflows aimed at reviewing and, if necessary, revoking user authorizations. This automated process ensures timely action on access rights adjustments, reduces manual overhead, and minimizes the risk of security breaches or compliance issues.

**Examples Scenario:**

- **A user gets promoted or changes departments:** Their previous authorizations need to be reviewed and potentially removed to prevent unnecessary access. Configuring the CustomActionIdForAuthorizationReviewRemoveAuthorization guides the system in executing the proper workflow for removing those authorizations.
  
- **An employee leaves the organization:** To ensure that all access rights held by the individual are revoked, the configured custom action ID ensures that any authorization tied to the user is evaluated and appropriately removed, securing the system against unauthorized access.

**Related Settings:**

- `ImportManagersToWFIgnoreDepartmentTypes`: While configuring authorizations, this setting helps in filtering out certain department types, ensuring that the authorization review process stays focused on relevant user groups.

**Applicable Workflows Actions:**
- AuthoirizationCertificationBO

**Best Practices:** 

- **Configure when:**
  - Establishing or updating an authorization review process.
  - Implementing role-based access controls that necessitate periodic review and adjustment.
  - Compliance standards require strict monitoring and control over user access.

- **Avoid when:**
  - The organization lacks a clear process for authorization review and management.
  - Custom actions have not been clearly defined or documented.
