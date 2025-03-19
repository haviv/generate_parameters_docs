# ClearWorkflowFormAction

**Category:** Workflow

**Description:** The ClearWorkflowFormAction is designed to manipulate XML data within a workflow instance by selectively removing XML elements based on their technical names. This action plays a critical role in dynamic form management and data sanitization within workflow processes by allowing conditional removal of form fields and data sections. The action reads a parameter specifying the technical names of the XML elements to remove, iterates over the XML structure of the workflow instance's request data, and selectively removes specified elements. This process effectively allows for dynamic adjustments to the data structure carried through the workflow, tailoring the data payload for downstream processing or compliance needs.

**Parameters:**

- Basic Parameters:
    - Name: technicalNamesToRemove
    - Description: A comma-separated list of the technical names of the XML elements to be removed from the workflow instance's request data. This action splits the input string and iterates over the request data XML, removing elements matching any of the specified technical names.
    - Default value: (none)
    - Mandatory: no

**Business impact:** This action directly impacts the integrity and relevance of the data passing through a workflow, ensuring only pertinent form fields and data are retained for processing. It supports compliance and data minimization strategies by allowing unnecessary or sensitive data to be removed in accordance with business rules or regulatory requirements. By facilitating dynamic form modifications, it enhances the flexibility and user experience of self-service portals, where users can submit requests that are automatically adjusted for relevancy and compliance.

**Example of usage:** In a scenario where a workflow form includes fields for optional data collection - such as "temporaryAccessEndDate" or "additionalNotes" - that are not always relevant for every process or decision path, the ClearWorkflowFormAction can be used to remove these fields based on the workflow context or user input, simplifying the data structure for subsequent approval or processing stages.

**Prerequisites:** To use this action, a workflow instance must be active with request data structured as expected by the action (i.e., in XML format with identifiable 'technicalNames' attributes for elements). The user or system account invoking the action must have permissions to modify workflow instances and their associated data.

**Error Handling and Troubleshooting:**

- **Error:** Workflow instance's request data is null or does not conform to the expected XML structure.
    - **Cause:** This could occur if the workflow is misconfigured, or if prior actions in the workflow sequence failed to initialize the request data properly.
    - **Solution:** Ensure that the workflow is correctly configured and that all preceding actions are successfully initializing and manipulating the request data as expected. Verify XML structure integrity before invoking this action.

- **Error:** Changes not reflected in the workflow instance.
    - **Cause:** This may be due to a failure in committing changes to the database after element removal.
    - **Solution:** Check database connectivity and permissions. Ensuring that the `WorkflowManager.Instance.db.SubmitChanges();` operation completes successfully is crucial for reflecting changes made by this action.

This documentation covers how to use the ClearWorkflowFormAction within the Pathlock cloud platform, emphasizing its role in managing data structure and integrity throughout workflow processes.