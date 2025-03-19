Action Name: FillWorkflowFromExternalQuery

**Category:** Workflow

**Description:** The `FillWorkflowFromExternalQuery` action is designed to populate a workflow form with data retrieved from a specified external data source via a stored procedure. Initially, it establishes the execution context based on the system ID provided by the parameters. It then compiles a list of parameters from the workflow instance and the current settings, excluding any that relate to passwords for security reasons. These parameters are then utilized to query the specified data source. The resultant data is used to fill the form related to the current workflow instance. Following the successful data retrieval and form population, the action marks itself as completed and commits the changes to the database.

**Parameters:**

*Basic:*

    Name: datasourceName
    Description: The name identifier of the datasource from which data is to be queried. This parameter is crucial for specifying which external data source should be queried to retrieve necessary data for form population.
    Default value: None
    Mandatory: yes

*Advanced:*

    No advanced parameters defined for this action.

**Business impact:** The `FillWorkflowFromExternalQuery` action automates the process of fetching and populating forms with data from an external source, significantly streamlining workflows that require external data. This is particularly useful for workflows involving dynamic data retrieval for forms like user access requests, risk calculation forms, or policy compliance checks, where up-to-date information from external databases is critical. Automating this task reduces manual data entry errors, speeds up process completion, and ensures consistency across the workflow processes.

**Example of usage:** 

A common application of this action would be during a user access request workflow where user details and required access levels need to be fetched from an HR management system. By specifying the `datasourceName` as the HR system's database, the action can retrieve the necessary data to populate the access request form, making the approval process more efficient and reducing the risk of manual errors.

**Prerequisites:** 

- The specified datasource must be accessible and correctly configured in the system.
- The user executing this action must have the necessary permissions to access both the workflow system and the external datasource.
- The stored procedure or query defined must exist in the datasource and be accessible.

**Error Handling and Troubleshooting:** 

- If the action fails to retrieve data, ensure that the `datasourceName` parameter is correctly specified and matches an existing and accessible data source.
- Verify that the necessary permissions are in place for the workflow system to access the data source.
- Check logs for any errors related to data query execution; issues may relate to the structure of the query or the availability of the specified data source.
- Errors regarding data not populating correctly in the form may require a review of the data mapping and form field configurations to ensure they match the structure of the data being retrieved.