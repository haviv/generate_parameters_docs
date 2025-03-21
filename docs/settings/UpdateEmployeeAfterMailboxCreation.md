# Update Employee After Mailbox Creation

**Technical Name:** UpdateEmployeeAfterMailboxCreation

**Category:** User Management

**Default Value:** N/A

**Impact Level:** High

**Description:**

This setting controls the process of updating employee records in the Pathlock platform following the successful creation of a mailbox in Microsoft Exchange. This ensures that employee profiles are kept current with their latest contact information and access rights.

**Business Impact:**

Ensuring employee records are immediately updated after mailbox creation helps maintain efficient communication channels within the organization. It also ensures that access rights and security settings align with current employee roles and responsibilities, supporting compliance and security management.

**Technical Impact when configured:**

When enabled, this feature interacts with Microsoft Exchange Server to verify mailbox creation before updating the corresponding employee profile in the Pathlock platform. It attempts to update employee records multiple times (as defined in ExchangeUserCreationAttempts) to accommodate any delays or issues in mailbox provisioning.

**Examples Scenario:**

- An employee is newly onboarded, and their user account is created in Active Directory. Subsequently, a mailbox is provisioned for the employee. Enabling this setting ensures that once the mailbox is successfully created, the employee's profile in Pathlock is immediately updated to include their new email address.
  
- An existing employee changes departments, necessitating an email change. Once their mailbox is updated or recreated, this setting ensures their Pathlock profile is automatically updated to reflect these changes.

**Related Settings:**

- ExchangeUserCreationAttempts

**Best Practices:** configure when 

- Setting up automatic synchronization between employee email provisioning and their security profiles.
  
avoid when 

- Mailbox provisioning does not impact user management or access controls within Pathlock platform.