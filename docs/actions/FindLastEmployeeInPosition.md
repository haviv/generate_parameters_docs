Action Name: FindLastEmployeeInPosition

**Category:** User Management

**Description:** 

The `FindLastEmployeeInPosition` action is designed to identify the most recent employee who held a specific position within the company, looking back over a specified timeframe. This action searches through the company's employee records, comparing position titles and employment dates to find the relevant individual. If an employee who matches the criteria is found, details about this employee are set as the reference user in the workflow instance, facilitating further actions such as access assignments or reviews based on this context.

**Parameters:**

- Basic:
    - Name: PositionTitleTechnicalName
    - Description: Technical name of the position to search for the last employee.
    - Default value: Not applicable
    - Mandatory: Yes

    - Name: EmployeeNumberOfCurrentEmployee
    - Description: Employee number used as a reference point, typically the new or current employee's number.
    - Default value: "##NewEmployeeNumber##"
    - Mandatory: Yes

- Advanced:
    - Name: TimeIntervalTechnicalName
    - Description: Defines the number of months to look back to find the last employee in the given position. Used to limit the search to a relevant timeframe.
    - Default value: 3
    - Mandatory: No

**Business Impact:** 

The ability to efficiently identify the predecessor of a position within specified timeframes enhances the company's internal processes, such as onboarding, transition planning, and access management. By automating this query, Pathlock Cloud ensures that relevant historical access patterns, risks, and compliance requirements associated with a position are readily accessible and can be applied to the new incumbent, thereby maintaining continuity and enforcing security and governance standards.

**Example of Usage:**

An HR manager initiates a workflow to automate the onboarding process for a new employee. As part of the workflow, the `FindLastEmployeeInPosition` action is executed to find the last employee who held the new employee's designated position. This information is then used to review and assign relevant access rights and responsibilities, ensuring a smooth transition and adherence to compliance requirements.

**Prerequisites:** 

The user must have access to the workflow management system and the database where employee records are stored. Additionally, the user executing this action must have permissions to query employee records and update workflow instances.

**Error Handling and Troubleshooting:**

- If an employee matching the criteria cannot be found, the action will set the workflow instance to have no reference user. Ensure the position title and time interval are correctly specified.
- Ensure the database connection is active and accessible; a failed connection could prevent the action from completing successfully.
- If unexpected results are returned (e.g., no employee found when one is expected), review the specified parameters for accuracy and ensure that the database contains up-to-date and comprehensive employee records.
- Monitor the system's logs for any error messages that can provide insight into failures or exceptions that occur during the execution of this action.