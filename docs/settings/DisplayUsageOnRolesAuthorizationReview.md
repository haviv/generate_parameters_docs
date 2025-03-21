# Display Usage On Roles Authorization Review

**Technical Name:** DisplayUsageOnRolesAuthorizationReview

**Category:** Audit

**Default Value:**

**Impact Level:** High

**Description:**

The DisplayUsageOnRolesAuthorizationReview parameter controls the visibility of specific rows during the authorization review process in Pathlock's GRC platform. This parameter ensures that only relevant data is presented to the user, enhancing the effectiveness and efficiency of the authorization review workflow.

**Business Impact:**

Ensuring that only necessary information is displayed during the review process greatly impacts the organization’s ability to maintain tight security controls and adhere to compliance requirements. It reduces the risk of overlooking critical discrepancies by minimizing information overload.

**Technical Impact when configured:**

- Enhances user interface clarity by hiding irrelevant or empty rows in review screens. 
- Streamlines the review process, making it easier and quicker for users to identify and act on important items.
- Reduces the likelihood of user error by presenting only pertinent information.

**Examples Scenario:**

- During roles authorization reviews, auditors or administrators can focus on roles genuinely requiring attention, ignoring system-generated empty or irrelevant entries that might otherwise clutter the review interface.
  
**Related Settings:**

- `ShowHasChangeFilter`
- `SapReadLogsResponseTimeoutInMinutes`

**Best Practices:** Configure when setting up roles authorization reviews to ensure users are presented with only the necessary information, hence optimizing the review process. Avoid when transparency is required for all entries, including placeholder or system-generated rows.