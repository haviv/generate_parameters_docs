# Enable user recognition by email address in workflow requests

**Technical Name:** RecognizeUserNameOfCurrentUserByEmail

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter configures the Pathlock Cloud GRC platform to recognize user accounts by their email addresses during workflow requests. This feature enhances the handling of user identities, making it easier to link workflow requests to specific users based on their email addresses rather than their usernames or other identifiers.

**Business Impact:**

Adopting this feature can significantly streamline workflow processes related to security, risk, and compliance management. By enabling user recognition by email, organizations can improve accuracy in user identification, reduce the risk of errors in manual user searches, and accelerate the approval processes for compliance and access requests. This leads to better efficiency and reliability in managing user access and permissions within the organization.

**Technical Impact when configured:**

- Workflow requests can automatically identify and authenticate users based on their email addresses.
- Reduces the potential for errors in user identity verification.
- Enhances the integration capabilities with systems where email addresses are primary user identifiers.
- Improves the user experience by simplifying the workflow requests process.

**Examples Scenario:**

- When a user requests emergency access to sensitive resources, the system can automatically link the request to the user's profile using their email address. This ensures that the access rights are granted to the correct individual without manual cross-referencing of user information.

**Related Settings:**

- ProfileTailorUserManagmentFromActiveDirectory

**Best Practices:**

- **Configure when:**
  - The organization uses email addresses as the primary identifier for users across its systems.
  - There is a need for improved accuracy and efficiency in user recognition during workflow processes.
- **Avoid when:**
  - Email addresses are not uniformly used or frequently change, which might lead to inconsistencies in user recognition.