# Custom User Group Id For Change Documents Sync

**Technical Name:** CustomUserGroupIdForChangeDocumentsSync

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The CustomUserGroupIdForChangeDocumentsSync parameter is used to specify a custom user group ID that synchronizes change documents. This setting allows for targeted synchronization of documents based on user group, facilitating more efficient data management and security protocols within the Pathlock Cloud GRC platform.

**Business Impact:**

Setting a specific user group ID for change document synchronization helps in streamlining the process of document management and ensures that only relevant changes are synchronized with the specified user group. This can lead to improved operational efficiency and better compliance with internal security and governance policies.

**Technical Impact when configured:**

When configured, this parameter ensures that change documents are only synchronized with the system for the specified user group ID. This targeted synchronization can help in reducing system load, avoiding unnecessary data processing, and enhancing the security by limiting access to sensitive documents.

**Examples Scenario:**

For instance, if there are multiple user groups within an organization, and only one group is responsible for compliance documentation, setting the CustomUserGroupIdForChangeDocumentsSync parameter to this specific group's ID ensures that only members within this group receive updates and changes to compliance-related documents. This mechanism prevents data overload and avoids exposing sensitive information to unauthorized groups.

**Related Settings:**

- CustomerStatistics_EnableSend

**Best Practices:** Configure the CustomUserGroupIdForChangeDocumentsSync parameter when there is a need to segregate document synchronization processes among different user groups. Avoid using this setting if all user groups require access to the same set of change documents to ensure comprehensive data availability.