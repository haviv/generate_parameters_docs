**Authorization Review System Details Link Text**

**Technical Name:** AuthorizationReviewSystemDetailsLinkText

**Category:** Audit

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

This parameter controls the display text for links related to system details within the context of authorization reviews, facilitating users to navigate and review authorization details more intuitively.

**Business Impact:**

Having a clear and descriptive link text directly affects the user's ability to efficiently navigate and understand the authorization context, thereby impacting the overall effectiveness and timeliness of the authorization review process. This can ultimately influence the organization's compliance posture and its ability to mitigate internal risks.

**Technical Impact when configured:**

Configuring this parameter to include specific, descriptive text can improve the usability of the Pathlock GRC platform, especially during detailed audits and reviews. It enhances clarity and accessibility, making it easier for users to identify and interact with the relevant system details necessary for thorough authorization reviews.

**Examples Scenario:**

A user is conducting an audit within the platform and encounters a link labeled with generic text such as "Details." If the `AuthorizationReviewSystemDetailsLinkText` parameter is configured to display "View Detailed Authorization History," the user is more likely to understand what information will be displayed upon clicking the link, thus improving the user's navigation and efficiency during the audit process.

**Related Settings:**

- AuthorizationReviewShowPartialApprovalIcon

**Best Practices:** 

- **Configure when:** There is a need to enhance clarity and reduce ambiguity in authorization review processes, particularly for users who may not be familiar with the platform.
  
- **Avoid when:** Detailed customization of link texts could introduce inconsistencies in the UI, potentially confusing users if not done thoughtfully. Ensure changes are communicated effectively to all platform users.