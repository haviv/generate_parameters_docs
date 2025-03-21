# Campaigns Review Details Tab UAR Usage

**Technical Name:** CampaignsReviewDetailsTabUARUsage

**Category:** User Management

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

The Campaigns Review Details Tab UAR Usage parameter is used to control the automatic refreshing of user information during emergency access review steps within the Pathlock Cloud GRC platform. It ensures that user access reviews (UAR) are conducted with the most up-to-date information, enhancing the effectiveness of emergency access management.

**Business Impact:**

By enabling this setting, organizations can improve their security posture by ensuring that decisions made during the emergency access review process are based on current user data. This reduces the risk associated with stale or outdated information potentially leading to inappropriate access being granted or maintained.

**Technical Impact when configured:**

When this parameter is enabled, the system automatically refreshes the user information at the beginning of the emergency access step in campaigns. This ensures that reviewers have access to the latest user data, thus making more informed decisions about user access rights during emergency situations.

**Examples Scenario:**

Imagine a scenario where a user’s role has changed just before an emergency access review is conducted. If the Campaigns Review Details Tab UAR Usage parameter is enabled, the system will refresh the user's information, ensuring the review reflects their current access privileges, roles, and responsibilities. This mitigates the risk of the user retaining access rights that are no longer appropriate for their new role.

**Related Settings:** 

- EnableModernStyleChartInReportDesigner
- ContentSecurityHeaderDefaultSrcDirectiveAllowedDomains

**Best Practices:** 

- Configure when: Emergency access needs to be frequently reviewed, and user data changes are common.
- Avoid when: User information is stable, and emergency access reviews are conducted infrequently, to minimize system load.