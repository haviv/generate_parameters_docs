# Authorization Review Link To Portal Visible

**Technical Name:** AuthorizationReviewLinkToPortalVisible

**Category:** Workflow

**Default Value:** (The default value is not provided in the code references)

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of a link to the Pathlock Cloud GRC platform within authorization review communications or interfaces. When enabled, it allows users to directly access relevant authorization review materials or tasks within the platform.

**Business Impact:**

Enabling this link enhances user experience by providing immediate access to necessary authorization reviews, streamlining the process of reviewing and approving access rights and roles. This can lead to more timely and efficient compliance activities, reducing the risk associated with delayed or inefficient authorization review processes.

**Technical Impact when configured:**

- Enhanced navigation and user experience within authorization review processes.
- Potential increase in compliance efficiency by minimizing delays in review processes.
- Direct access to the Pathlock Cloud GRC platform, facilitating immediate action on authorization reviews.

**Examples Scenario:**

An organization implements the AuthorizationReviewLinkToPortalVisible parameter to simplify the process for managers when conducting quarterly access reviews. With the link visible, managers can directly click through to the Pathlock Cloud GRC platform from the review notification email, where they can see pending tasks, thus speeding up the review process and enhancing overall compliance workflows.

**Related Settings:**

- `AuthorizationReviewForPositionChangeTemplateId`
- `SAP_HR_RELAT_BetweenPositionAndObject`

**Best Practices:** configure when you aim to enhance the user experience and efficiency of authorization review processes; avoid when there is concern about directly linking to the platform from external communications for security reasons.