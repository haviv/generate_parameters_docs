# Authorization Review By Roles Show Activities In Role Details Link

**Technical Name:** AuthorizationReviewByRolesShowActivitiesInRoleDetailsLink

**Category:** Audit

**Default Value:** False

**Impact Level:** High

**Description:** This parameter controls the visibility of activities within role details in authorization review processes. When enabled, users can view specific activities linked to roles during the review.

**Business Impact:** Enhancing the transparency and granularity of authorization reviews by allowing auditors and compliance managers to see not just roles but the specific activities those roles entail. This can significantly contribute to a more efficient risk assessment and compliance process by identifying and addressing inappropriate role assignments or excessive permissions at a granular level.

**Technical Impact when configured:** Enables the display of associated activities for each role within the authorization review screens. This aids in deeper analysis and understanding of the permissions and access levels granted by each role, facilitating better governance and compliance posture.

**Examples Scenario:** An organization must comply with strict regulatory standards requiring detailed oversight of user permissions and roles. By enabling this parameter, during an authorization review, the compliance team can identify roles with potentially excessive permissions by reviewing the detailed activities each role encompasses. This level of detail allows for finer control over permissions and helps identify roles that may need to be adjusted to align with the principle of least privilege.

**Best Practices:** Configure when detailed activity-level review is necessary for compliance or audit purposes. Avoid when unnecessary to limit information overload and simplify the authorization review process.