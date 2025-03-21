**Technical Name:** TechnicalNameForEmployeeLastNameHebrew

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used to define and manage the Hebrew version of employee last names within the Pathlock Cloud GRC platform. It helps ensure accurate and consistent recording of last names in Hebrew script across various parts of the system, particularly in workflows related to user creation and authorization.

**Business Impact:**

Proper configuration of this parameter ensures that user profiles, especially for Hebrew-speaking users, are correctly managed and identified. This is crucial for organizations operating in or with Hebrew-speaking regions, facilitating better compliance, reporting, and user management.

**Technical Impact when configured:**

When correctly configured, this parameter aids in the accurate application of user roles and access permissions, especially in workflows that require precise identification of users, such as ApplyAuthorizationAction and CreateNewUser. This precise identification is critical for security, audit trails, and compliance purposes.

**Examples Scenario:**

- **Scenario 1:** In an organization with Hebrew-speaking employees, the HR department inputs the employee's last name in Hebrew during the creation of their user profile. By properly configuring the *TechnicalNameForEmployeeLastNameHebrew*, the system accurately associates the user with specific roles and permissions without any anomalies due to script differences.

**Related Settings:**

- TechnicalNameForEmergencyAccessDuration

**Applicable Workflows Actions:**

- ApplyAuthorizationAction
- CreateNewUser

**Best Practices:** 

- **Configure when:** the organization operates in a Hebrew-speaking environment or when Hebrew-speaking employees are onboarded in the system.
  
- **Avoid when:** the organization does not require handling of different scripts for user information, or when there is no business need to incorporate multilingual support for employee last names.