# Add Reference Information To User Owner Review

**Technical Name:** AddReferenceInformationToUserOwnerReview

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `AddReferenceInformationToUserOwnerReview` parameter is designed to enhance the authorization review process by adding additional, custom reference information fields. This feature enables user owners to have more context during the review process, thereby facilitating informed decision-making regarding user access and rights within the Pathlock Cloud GRC platform.

**Business Impact:**

Incorporating reference information into user owner reviews potentially reduces the risk of inappropriate access permissions being granted. It enables a more thorough review process by providing user owners with additional data points and context, which is crucial in tightly regulated or high-security environments.

**Technical Impact when configured:**

When enabled, this parameter allows the inclusion of bespoke fields in authorization review forms. These fields can be populated with data relevant to the review, such as the department, role criticality, or specific compliance requirements associated with the user being reviewed. This customization ensures that reviewers have all necessary information at hand without needing to consult external records.

**Example Scenario:**

A financial institution utilizes the `AddReferenceInformationToUserOwnerReview` parameter to add custom fields displaying the last audit date of user roles and whether any discrepancies were noted. This additional information aids the review process by highlighting potential risk areas, ensuring that user access is aligned with the institution's internal control standards and regulatory requirements.

**Related Settings:** 

- `UseCustomCountUsersForLicense`: Indicates if a custom method is being used to count users for licensing purposes. This setting, though not directly related, reflects the platform's general capability for customization to meet specific organizational needs.

**Best Practices:** 

- **Configure when:** there's a need for detailed reviews of user access, especially in environments with strict compliance requirements or when managing access to sensitive systems.
  
- **Avoid when:** additional information may overload reviewers or when the default review information suffices for decision-making processes.