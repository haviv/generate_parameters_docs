**Authorization Review Exclude Locked Users By Logons**

**Technical Name:** AuthorizationReviewExcludeLockedUsersByLogons

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter controls whether locked users are excluded based on their logon activities during the authorization review process in Pathlock Cloud GRC platform.

**Business Impact:** Enabling this feature can streamline the authorization review process by focusing only on active users, thereby reducing the workload and potential oversight on user accounts that are not currently of concern due to their locked status.

**Technical Impact when configured:** When enabled, this setting filters out locked user accounts from the authorization review process based on their logon activities. This can lead to a more efficient review process, focusing resources on user accounts that are active and potentially pose a security risk.

**Examples Scenario:** If an organization is conducting monthly authorization reviews to ensure compliance with access control policies and there are a significant number of user accounts that have been locked due to prolonged inactivity or security concerns, activating this setting would automatically exclude these accounts from the review process. This can save the reviewers considerable time by not having to manually sift through accounts that are not currently active or pose a risk, allowing them to concentrate on active accounts with potential access compliance issues.

**Related Settings:** N/A

**Best Practices:** Configure when undertaking large-scale authorization reviews to enhance efficiency and focus on active user accounts. Avoid when comprehensive reviews of both active and locked user accounts are necessary for audit or compliance purposes.