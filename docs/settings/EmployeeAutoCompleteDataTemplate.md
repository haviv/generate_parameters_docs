# Employee Auto Complete Data Template

**Technical Name:** EmployeeAutoCompleteDataTemplate

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The Employee Auto Complete Data Template parameter is designed to enhance the user experience within the Pathlock Cloud GRC platform by facilitating the auto-completion of employee data fields. This functionality utilizes a combination of employee IDs, names, and descriptions to assist users in quickly and accurately filling out forms or data fields related to employee information.

**Business Impact:**

Improves the efficiency of data entry and reduces the risk of errors when users are inputting or searching for employee-related information within the system. It streamlines processes that require the selection of employee-specific data, such as assigning roles, permissions, or tasks, ultimately aiding in better data management and operational workflows.

**Technical Impact when configured:**

When enabled and properly configured, the EmployeeAutoCompleteDataTemplate can significantly reduce the time required for filling out employee-related information by suggesting the most relevant information based on the initial input. This not only speeds up administrative tasks but also ensures data consistency and reliability across the platform.

**Examples Scenario:**

- When assigning a user to a new project, the system will suggest employee names and IDs as the project manager begins to type, allowing for quick selection and assignment.
- During audits or compliance checks, auditors can easily find and select employee names or IDs involved in specific processes, reducing the time spent searching through records.

**Related Settings:**

- `CommonSettings.Default.SearchUsingContainsInsteadOfStartsWith`
- `EmployeeReadDirectManagerForPositions`

**Best Practices:** 

- **Configure when:** Setting up the platform for initial use or updating employee information to ensure quick access and selection of employee data in system-wide forms and fields.
- **Avoid when:** Complete accuracy of manual entry is required without the influence of auto-suggestions to prevent the possibility of selecting incorrect auto-complete suggestions.