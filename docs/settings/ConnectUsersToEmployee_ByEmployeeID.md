# Connect Users To Employee By Employee ID

**Technical Name:** ConnectUsersToEmployee_ByEmployeeID

**Category:** User Management

**Default Value:** True

**Impact Level:** High

**Description:**

The parameter `ConnectUsersToEmployee_ByEmployeeID` determines whether users within the Pathlock GRC platform are automatically connected to employee records based on their Employee ID. This connection is attempted through a sequence of checks, starting with a direct Employee ID match, followed by cross-referencing users in other systems, and finally, attempting to match by email if no direct match is found.

**Business Impact:**

Ensuring accurate mapping between users and employee records is critical for effective governance, risk, and compliance (GRC) management. This setting directly impacts the integrity of audit trails, access controls, and compliance reporting by ensuring that actions and permissions within the system are correctly attributed to the specific employees.

**Technical Impact when configured:**

When enabled, this feature automates the process of associating users to their respective employee records within the Pathlock platform, reducing manual overhead and potential for error. If a user’s Employee ID cannot be located within the system, the mechanism proceeds to look for a match in other systems or by matching email addresses, enhancing the likelihood of accurate user to employee connections.

**Examples Scenario:**

For instance, in the scenario where a user's Employee ID does not directly match any existing record within the primary HR system integrated with Pathlock GRC, this feature, if enabled, would initiate a search across other systems or attempt to connect the user based on their email address. This ensures that even in cases of incomplete or inconsistent data entry, efforts are made to maintain accurate user-employee mappings, crucial for audit and compliance purposes.

**Related Settings:** ConnectUsersToEmployee_By_HR_system

**Best Practices:** configure when the organization has up-to-date and consistent Employee IDs across integrated systems to ensure seamless user-employee mapping. Avoid when Employee IDs are inconsistently used or when most user mapping would result in matches by email, as it might reduce the precision of the automatic connection process.