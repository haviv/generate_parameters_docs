# Enable Active Directory Activity Modes Matrix Compact Mode

**Technical Name:** EnableActiveDirectoryActivityModesMatrixCompactMode

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:** 

This parameter controls whether the Active Directory Activity Modes Matrix is displayed in a compact mode. Enabling this setting reduces the amount of screen space used by the matrix, making it easier to view large amounts of data at once.

**Business Impact:** 

Enabling this mode streamlines the display of user roles and permissions within the Active Directory, facilitating quicker decision-making regarding access rights and security policies. It is particularly beneficial for organizations with extensive Active Directory structures, where space optimization can significantly improve usability and oversight.

**Technical Impact when configured:** 

When this parameter is set to true, the Active Directory Activity Modes Matrix adopts a more condensed layout, minimizing the need for horizontal scrolling and allowing administrators to assess security settings more efficiently.

**Examples Scenario:** 

- **Before Configuration:** An IT security auditor needs to review hundreds of roles within the Active Directory. The default, expansive view of the Activity Modes Matrix requires excessive scrolling, making it difficult to compare roles and permissions side by side.
  
- **After Configuration:** The auditor enables Compact Mode for the Activity Modes Matrix. The streamlined view now allows for a more effective comparison of the roles and permissions within the same screen real estate, enhancing the auditor's ability to identify discrepancies and areas requiring attention.

**Related Settings:** 

- `DailyEmailIncludeUsernameField`

**Best Practices:** 

- **Configure when:** Reviewing or auditing large Active Directory environments to improve data visibility and ease the comparison of permissions and roles.
- **Avoid when:** Detailed, individual entry review is necessary, and screen real estate is ample, as the compact mode may omit some details for the sake of space.