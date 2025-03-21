**Authorization Review Take Full Name From User Record**

**Technical Name:** AuthorizationReviewTakeFullNameFromUserRecord

**Category:** User Management

**Default Value:** True

**Impact Level:** Medium

**Description:**
This parameter controls whether the Pathlock Cloud GRC platform should use the full name from the user's record during authorization reviews. When enabled, it ensures that the full name of the user, instead of just a username or an identifier, is displayed, enhancing clarity and personalization in reports and reviews.

**Business Impact:**
Using the full name from the user record can significantly improve the readability of reports and make it easier for administrators and auditors to identify users during authorization reviews. It enhances the accuracy of audits and compliance reports by ensuring personnel names are correctly matched to their corresponding user actions and permissions.

**Technical Impact when configured:**
When enabled, the system will fetch and display the user's full name, as stored in the user management system, in authorization reviews and related reports. This may slightly increase the time taken to generate reports due to the additional lookup required to retrieve the full name from the user record.

**Examples Scenario:**
- During an authorization review, instead of displaying user identifiers such as user123, the platform will display the full name, e.g., John Doe, making the review process more intuitive and user-friendly.
- Reports generated for compliance purposes will list full names, enhancing the documentation's formal quality and ease of understanding for external auditors.

**Related Settings:**
- `CompareSoDRisksBasedOnCausingRoles`

**Best Practices:** 
- Configure when: You are conducting authorization reviews within an environment where clarity of user identity is crucial, especially in large organizations where user identifiers may be less recognizable.
- Avoid when: There is a specific need to use anonymized data or identifiers for users during the review processes, or when system performance is a critical concern and the additional lookup time cannot be tolerated.