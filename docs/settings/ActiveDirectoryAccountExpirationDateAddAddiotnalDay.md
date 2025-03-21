# Active Directory Account Expiration Date Add Additional Day

**Technical Name:** ActiveDirectoryAccountExpirationDateAddAddiotnalDay

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter allows for the addition of an extra day to the expiration date of an Active Directory account. It is designed to provide a buffer period for administrative tasks related to account expiration, ensuring uninterrupted access for users.

**Business Impact:**

Adding an additional day to account expiration dates can prevent premature account lockouts, reducing the risk of disrupting critical business processes. It assists in compliance with internal policies regarding account management and ensures that users have continuous access to necessary resources.

**Technical Impact when configured:**

When configured, this parameter extends the expiration date of Active Directory accounts by one day beyond the originally set expiration date. This extension can be crucial for ensuring that automated processes or user activities are not unexpectedly interrupted due to account expiration.

**Examples Scenario:**

- A user's account is set to expire on a Friday, potentially leaving them without access over the weekend when IT support may be limited. By adding an additional day, the account remains active through the weekend, allowing access until IT can address the expiration on the next business day.

**Related Settings:**

- RoleReDesginMode
- SoDSimulateForHighRiskRoles

**Best Practices:** 

- Configure when accounts are critical to business operation and cannot afford even a brief period of disruption.
- Avoid when strict account expiration policies are in place, and any deviation could violate compliance requirements.