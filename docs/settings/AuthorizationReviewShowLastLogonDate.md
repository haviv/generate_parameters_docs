# Authorization Review Show Last Logon Date

**Technical Name:** AuthorizationReviewShowLastLogonDate

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the display of the last logon date for users within the authorization review reports. This feature aids in identifying potentially inactive accounts which might still have access privileges.

**Business Impact:**

Incorporating the last logon date into the review process enhances security by providing visibility into user activity. It helps in determining if there are accounts with access rights that have not been active for a significant period, thereby highlighting potential security risks.

**Technical Impact: when configured**

When enabled, the system includes an additional column within authorization review reports showing the last logon date for each user. This facilitates targeted reviews and informed decisions regarding access rights.

**Examples Scenario:**

- **Reviewing User Activity:** In a scenario where an organization is conducting an internal audit or review of user access rights, integrating the last login information can help ascertain if certain users have not been active for a prolonged duration. For instance, identifying users who have not logged in for over six months could lead to a decision to revoke their access, reducing potential security risks.

**Related Settings:**

- ShowHasChangeFilter

**Best Practices:** 

- **Configure when:** You are conducting authorization reviews and wish to include user activity as a criterion for access rights evaluation.
- **Avoid when:** Every user's access rights are frequently reviewed and updated, making the last logon date less relevant for security considerations.