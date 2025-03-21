# Authorization Review By Roles Show System Name

**Technical Name:** AuthorizationReviewByRolesShowSystemName

**Category:** Configuration

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:**

This parameter controls whether the system name is displayed alongside roles during authorization reviews within the Pathlock Cloud GRC platform. Enabling this setting can enhance visibility and context, making it easier for administrators and reviewers to understand the scope and origin of roles being reviewed.

**Business Impact:**

Displaying the system name with roles can significantly improve the accuracy and efficiency of authorization reviews. It aids in decision-making by providing additional context, which is particularly useful in environments with complex or multiple system integrations. This visibility helps in managing security, risk, and compliance more effectively by ensuring that roles are appropriately assigned and understood in the context of their system of origin.

**Technical Impact: when configured**

When enabled, this parameter ensures that every role presented during authorization reviews includes the system name. This facilitates a more informed review process, as reviewers can quickly identify which system a particular role belongs to, reducing confusion and potential errors in roles management.

**Examples Scenario:**

During a compliance audit, a reviewer uses the authorization review feature to verify that users have appropriate access rights. With `AuthorizationReviewByRolesShowSystemName` enabled, the reviewer can easily differentiate between similarly named roles across different systems, such as "Administrator" roles in both HR and Finance systems, ensuring a precise and effective authorization review.

**Related Settings:**

- CustomAuthenticationProviderAllowFallback

**Best Practices:** configure when the organization uses multiple systems that are integrated within the Pathlock Cloud GRC platform to ensure clarity in role assignments. Avoid when unnecessary to reduce information overload during review processes.