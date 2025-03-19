Action Name: Fill Workflow Form By Employee Record

**Category:** Workflow

**Description:**

This action automates the process of filling out a form within a workflow based on the record of an employee. When executed, it retrieves an employee's record using a specified field identifier, extracts relevant information, and automatically populates a form with this information. The action supports workflows that require up-to-date employee information to proceed, such as access requests, risk assessments, or any process that involves employee details. It ensures that the form is filled with accurate and current data by pulling this information directly from the employee’s record in the company database.

**Parameters:**

- Basic Parameters:
    - Name: employeeField
    - Description: The field identifier used to specify which employee's record should be retrieved for the form. It is used to locate the employee's record in the company's database and extract necessary information. In the context of this action, this parameter is critical for identifying the correct employee and is used as a key to fetch employee-related data.
    - Default value: N/A
    - Mandatory: Yes

- Advanced Parameters: None in this example

**Business impact:**

Implementing this action streamlines workflows that require employee-specific information. It eliminates manual data entry, reducing both time spent on form completion and the potential for errors. This automation supports compliance with internal policies and external regulations by ensuring that the information used in processes such as Provisioning Access Management (PAM), risk calculation, or access reviews is accurate and up-to-date. Enhanced accuracy and efficiency in these processes directly contribute to the robustness of an organization’s identity and GRC (Governance, Risk Management, and Compliance) strategies.

**Example of usage:**

In a new employee onboarding scenario, this action could be used within a workflow to automatically fill out an access request form with the employee's details, such as department, role, and contact information. This would ensure that the new employee receives the right access permissions quickly and accurately, improving their onboarding experience and operational efficiency.

**Prerequisites:**

- The user executing this action must have the necessary permissions to access employee records in the company database.
- An employee identification field must be defined and passed as a parameter to accurately fetch the correct employee record.

**Error Handling and Troubleshooting:**

- Error: Employee record not found
    - Cause: The specified employeeField may be incorrect or does not exist in the database.
    - Solution: Verify that the employeeField parameter is correctly set and matches an existing employee identifier in the database.

- Error: Form not filled
    - Cause: The extracted employee data may not contain the required fields or technical names to match the form’s fields.
    - Solution: Review the form configuration and the data fields available in the employee records to ensure a match. Adjust the form or the workflow action’s logic as needed to align the data fields.

This documentation aims to provide a clear understanding of how to configure and utilize the "Fill Workflow Form By Employee Record" action within the Pathlock Cloud platform, facilitating efficient and accurate form filling in workflow processes based on employee records.