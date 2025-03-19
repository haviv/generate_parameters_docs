# Allow Edit Email In My Profile

**Technical Name:** AllowEditEmailInMyProfile

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether a user can edit their email address within the My Profile section of the Pathlock Cloud GRC platform. By enabling or disabling this feature, organizations can manage how users update their contact information, ensuring communication channels remain secure and verified.

**Business Impact:**

Allowing users to edit their email addresses directly impacts how notifications, alerts, and communications are sent and received within the organization. This feature can affect data integrity and security policies regarding user identification and access management.

**Technical Impact when configured:**

When configured to allow edits, users have the flexibility to update their email addresses as needed, for instance, in the case of a name change or a shift to another department with a different email naming convention. Conversely, disabling this feature requires users to go through an administrative process to change their email, thus adding a layer of oversight but potentially slowing down user updates.

**Examples Scenario:**

- A user gets married and changes their last name. They want to update their email address to reflect the change.
- An employee transitions to a new department and receives a new department-specific email address.
- A user mistakenly entered a wrong email during initial setup and needs to correct it to receive important system notifications.

**Related Settings:**

- `AdditionalColumnsInUserSearch`: While not directly related, this setting also affects user management capabilities, offering customization in how user information is searched and displayed.

**Best Practices:** 

- **Configure when:** A dynamic workplace setting where users commonly undergo name changes, department shifts, or where flexibility in contact information is essential.
- **Avoid when:** Strict control over user contact information is required for security, regulatory compliance, or when email addresses are tied to critical operational processes.