# Authorization Review By Roles Show Number Of Activities

**Technical Name:** AuthorizationReviewByRolesShowNumberOfActivities

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the display of the total number of activities associated with roles during authorization reviews within the Pathlock Cloud GRC platform. This parameter allows for a detailed and quantitative analysis of roles based on their activity volumes, aiding in the identification of highly active roles which may require additional scrutiny or attestations.

**Business Impact:**

Understanding the number of activities tied to specific roles is crucial for organizations to ensure proper role management and segregation of duties. High activity volumes may indicate roles with extensive permissions that could pose security risks. Thorough review and certification of these roles help in minimizing unauthorized access and enhancing overall compliance posture.

**Technical Impact when configured:**

When enabled, this setting provides visibility into the role-based activities during authorization reviews, enriching the decision-making process for certifications, audits, and compliance activities. It aids administrators and auditors in identifying roles with significant influence on systems and data, thereby facilitating targeted reviews and adjustments.

**Examples Scenario:**

- During periodic access reviews, an auditor can identify roles with an unusually high number of activities and prioritize these roles for a more thorough review to ensure all users assigned to these roles require the associated permissions.

**Related Settings:**

- AuthorizationReviewByRolesShowRoleDescription

**Best Practices:** 

- **Configure when:** Conducting detailed authorization reviews and needing to assess the impact of roles based on their activity levels. Especially useful in complex environments where roles are granted numerous activities.
  
- **Avoid when:** The number of activities per role is not relevant to your security or compliance posture, or if such detailed analysis may overwhelm the review process without adding value.