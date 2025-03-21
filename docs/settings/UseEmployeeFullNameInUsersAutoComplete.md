# Use Employee Full Name In Users Auto Complete

**Technical Name:** UseEmployeeFullNameInUsersAutoComplete

**Category:** User Management

**Default Value:** None

**Impact Level:** Medium

**Description:**

This parameter controls whether the full name of an employee is used in auto-complete fields within user-related forms or actions. When enabled, it leverages the employee's full name for a more intuitive user experience, particularly in scenarios involving authorization requests or user searches.

**Business Impact:**

Enabling this feature can significantly enhance user experience by making it easier for administrators or users to find and select the correct user accounts, especially in large organizations with many similarly named users. It can lead to more accurate user identification, reducing errors in user selection during authorization processes or while assigning roles and permissions.

**Technical Impact when configured:**

When configured, system forms and functionalities that include user auto-complete fields will display the full name of employees alongside their user identifiers (e.g., usernames or user IDs). This alteration aids in distinguishing between users more effectively, especially in systems like SAP where user IDs might not be self-explanatory.

**Example Scenario:**

In an authorization request form, an approver is attempting to grant access to a user named John Smith. There are multiple users with the name "John Smith" in the organization. Enabling this parameter ensures that the full names of the employees are utilized, along with additional identifiable information (such as their department or position if available), making it straightforward for the approver to select the correct John Smith from the list.

**Related Settings:**

- CustomFieldTechncalNameForUserBuildingData

**Best Practices:** 

- Configure when: Your organization has a large user base with potential for similar names, requiring precision in user identification for authorization and access management processes.
- Avoid when: Usernames or user IDs in your organization are unique and descriptive enough to make user identification straightforward without needing full names.