# Employee Number Length

**Technical Name:** EmployeeNumberLength

**Category:** User Management

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:**

Specifies the accepted length for employee numbers within the organization. This setting is crucial for ensuring consistency in employee records, particularly during synchronization processes where employee identifiers might change (e.g., from a username to a more identifiable format like firstname.lastname).

**Business Impact:**

A properly set Employee Number Length ensures that all employee records are correctly identified and tracked across the system. It prevents errors in employee data management, which can affect access rights, compliance reporting, and overall organizational security.

**Technical Impact when configured:**

- Ensures uniformity in the length of employee numbers, simplifying user management and reporting.
- Facilitates accurate synchronization of employee records across organizational structures, especially when identifiers are altered.
- Aids in the prevention of duplicate or incomplete records resulting from identifier changes.

**Examples Scenario:**

Consider an organization undergoing a restructuring process where employee usernames are transitioned to a more standardized format (firstname.lastname). If an employee originally identified as "johns" is now recognized as "john.smith" within the system, configuring the Employee Number Length correctly will help ensure that "john.smith" is accurately linked to the existing records associated with "johns," provided the length criteria are met. This maintains data integrity and continuity for access and audit purposes.

**Related Settings:**

- EmailMesssageLogEnablePasswordProtection
- DisplayHighRiskActivitiesOnRolesAuthorizationReview

**Best Practices:** Configure when establishing or modifying the organizational structure to ensure consistent employee identification across the platform. Avoid when there is no clear standardization of employee number formats across the organization, as this could lead to inconsistencies and record mismatches.