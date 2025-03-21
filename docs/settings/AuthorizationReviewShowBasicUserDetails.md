# Authorization Review Show Basic User Details

**Technical Name:** AuthorizationReviewShowBasicUserDetails

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The `AuthorizationReviewShowBasicUserDetails` parameter controls the visibility of basic user details in the authorization review interface within the Pathlock Cloud GRC platform. When enabled, this feature allows additional user columns to be displayed, enhancing the information available during the review process.

**Business Impact:**

Enabling this parameter enhances the ability to perform a thorough and informed audit and review of user authorizations by providing essential user details. This added visibility aids in identifying potential security risks or compliance issues associated with specific user profiles, thereby supporting better decision-making in authorization management.

**Technical Impact when configured:**

When configured, this setting dynamically adds columns to the grid displaying user information in the context of authorization certifications. The additional details can include, but are not limited to, user roles, departments, and other relevant employee fields which are prefixed as specified in the configuration, improving the granularity of data available for review.

**Example Scenario:**

- **Scenario:** As an auditor overseeing compliance within the Pathlock Cloud GRC platform, having detailed information about users during an authorization review can significantly streamline the process. 
    - **Example:** When the `AuthorizationReviewShowBasicUserDetails` parameter is enabled, auditors can view not just the roles assigned to a user but also additional information such as the department and location directly within the review interface. This level of detail can be crucial in identifying unauthorized access or ensuring compliance with segregation of duties policies.

**Related Settings:** 

- `RestApiDrillDownFieldNames` 

**Best Practices:** 
- **Configure when:** A detailed review of user authorizations is required, particularly in complex environments where added user context can influence authorization decisions.
- **Avoid when:** Minimalist information suffices for the authorization review process, or in scenarios where performance considerations outweigh the benefits of additional information display.