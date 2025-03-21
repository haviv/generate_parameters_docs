# Get Employee Data From Active Directory

**Technical Name:** GetEmployeeDataFromActiveDirectory

**Category:** User Management

**Default Value:** 

**Impact Level:** High

**Description:** 

Enables automated user profile management by fetching relevant employee data from Active Directory (AD). This parameter, when enabled, facilitates the synchronization of user data into the Pathlock Cloud GRC platform for various aspects such as user creation, authorization management, and automated workflow triggering.

**Business Impact:**

By automating user data retrieval from Active Directory, organizations can streamline user account management processes, ensure timely updates to user permissions, and maintain compliance with regulatory requirements. It reduces manual intervention, minimizing errors and increasing operational efficiency.

**Technical Impact when configured:** 

1. Automates the process of creating new user profiles within Pathlock Cloud GRC by pulling employee information directly from Active Directory.
2. Helps in applying accurate authorization settings and permissions for users based on their current role and status in AD.
3. Ensures that user management actions like user creation, and authorization adjustments are informed by the most current data available in Active Directory.

**Examples Scenario:**

- **User Onboarding:** Automatically creates a user profile in Pathlock Cloud GRC when a new employee is added to Active Directory, ensuring immediate access to necessary applications and systems based on predefined roles and permissions.
- **Role Change Management:** Dynamically adjusts user permissions and access rights when an employee’s role changes within the organization, as reflected in Active Directory, ensuring compliance and preventing unauthorized access.

**Related Settings:** 

- Workflow Action Parameters for UserCreationManagement, CreateNewUser, and ApplyAuthorizationAction.

**Applicable Workflows Actions:** 

- ApplyAuthorizationAction
- CreateNewUser
- UserCreationManagement

**Best Practices:** 

- **Configure when:** you are looking to automate user management and ensure that user permissions across your GRC platform are always in sync with Active Directory.
  
- **Avoid when:** your organization does not use Active Directory for employee management or when manual oversight of user permissions is required.