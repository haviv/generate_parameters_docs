# Skip Is User Exists Check In Sap

**Technical Name:** SkipIsUserExistsCheckInSAP

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter allows the Pathlock Cloud GRC platform to skip the check for existing users during SAP connector operations. When enabled, this setting bypasses the standard verification process to determine if a user already exists within the SAP system, potentially speeding up batch operations or integrations.

**Business Impact:**

Enabling this parameter can significantly reduce the time required for mass user operations, such as role assignments or updates, by eliminating the need to check if each user exists in the system. However, it may also increase the risk of duplicating user entries or missing errors related to user existence, which could impact system security and integrity.

**Technical Impact: when configured**

When configured, operations involving user data in SAP will proceed without verifying user existence. This can lead to faster processing times for batch updates, user role assignments, and other mass user management activities. It is particularly useful in environments where user existence is managed or verified through external systems or pre-validated lists.

**Examples Scenario:**

A company is undergoing a massive reorganization, requiring the update of SAP user roles for thousands of users. The IT department knows these users already exist in SAP and have been pre-validated through HR systems. By enabling SkipIsUserExistsCheckInSAP, the IT team can upload the entire batch without SAP checking the existence of each user, saving considerable time and resources.

**Related Settings:**

- FieldsToIncludeFromUpdate

**Best Practices:** 

- Configure when performing large scale user updates or integrations where user existence is assured through external validations or pre-checks.
- Avoid when user updates are performed ad-hoc or when there is no other mechanism ensuring the accuracy of user existence data.