# Add Reference Information To User Owner Review

**Technical Name:** AddReferenceInformationToUserOwnerReview

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter enables the addition of custom reference information to the review process of a user’s authorization by their owner within the Pathlock Cloud GRC platform.

**Business Impact:** Enabling this feature can significantly streamline the user authorization review process by providing user owners with additional context or reference information. This can help in making more informed decisions, potentially reducing the risk of unauthorized access and enhancing security compliance.

**Technical Impact when configured:** When enabled, custom fields or details can be added to the user owner’s review interface, potentially affecting how user authorizations are reviewed and managed. It requires careful configuration to ensure that the additional information provided is relevant and useful for the review process.

**Example Scenario:** Let's imagine an organization requires user owners to review and validate the access rights of their team members regularly. By enabling AddReferenceInformationToUserOwnerReview, the company can add custom fields such as "Last Access Review Date" or "Sensitive Access Types," helping user owners to quickly understand the context and make more informed decisions during the review process.

**Related Settings:** 

- UseCustomCountUsersForLicense

**Applicable Workflow Actions:** 

- Authorization review initiation
- Custom field review in user profiles
- Completing user review

**Best Practices:** 
- **Configure when** you have specific compliance or internal requirements that necessitate additional information during the user owner review process. It's particularly useful if you've identified gaps in the review process that could be mitigated by providing more context.
- **Avoid when** there is no clear use case or requirement for additional information, as it could complicate the review process or overwhelm reviewers with unnecessary details.

**Context:** This parameter is part of the Pathlock Cloud GRC platform's user management and authorization review process, designed to enhance security and compliance by adding context and relevant information for user owners during the review process.