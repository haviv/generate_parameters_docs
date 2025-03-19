# StartTraceForEmergencyAccess

**Category:** Security

**Description:** 

The `StartTraceForEmergencyAccess` action is designed to initiate a trace for scenarios that require emergency access. This action facilitates enhanced monitoring and auditing by marking the start of a trace period tied to a specific user and session. The trace monitors user activities within the system for a defined period, ensuring any actions taken during emergency access are logged and auditable. This action is vital for security purposes, ensuring compliance with internal and external audit requirements. 

**Parameters:** 

- Basic:
    - **Name:** Until Date
    - **Description:** Defines the end date until which the trace for emergency access is active. It is used in conjunction with the `DateFormat` parameter to accurately parse the date provided by the user.
    - **Default value:** N/A
    - **Mandatory:** yes

    - **Name:** Username
    - **Description:** Specifies the username for whom the emergency access trace is being started. It's essential for identifying the exact user account that requires monitoring during the emergency access period.
    - **Default value:** N/A
    - **Mandatory:** yes

    - **Name:** Session Identifier
    - **Description:** A unique identifier for the session during which the trace is to be activated. This ensures that the trace is accurately associated with the correct session and user actions.
    - **Default value:** N/A
    - **Mandatory:** yes

- Advanced:
    - **Name:** Date Format
    - **Description:** Allows specifying the format in which the `Until Date` parameter is provided. This ensures accurate parsing and understanding of the until date, accommodating different date format preferences.
    - **Default value:** N/A (Defaults to system's date parsing capabilities in the absence of this parameter)
    - **Mandatory:** no

**Business impact:** 

Implementing the `StartTraceForEmergencyAccess` action significantly enhances security and compliance processes within an organization. It enables detailed monitoring and logging of all actions performed under emergency access, assisting in audit trails and ensuring actions are traceable. This capability is crucial for meeting strict regulatory requirements, mitigating risks associated with unauthorized access, and ensuring that emergency access privileges are not misused.

**Example of usage:** 

To initiate a trace for user "JohnDoe" in an emergency scenario, until the end of the current month, with the session identifier "XYZ123":

```csharp
Perform("JohnDoe", "XYZ123", new WorkflowActionPramaters {
    { "UntilDate", "2023-12-31" }, 
    { "DateFormat", "yyyy-MM-dd" }
});
```

**Prerequisites:** 

- The user executing this action must have administrative privileges or specific permissions to initiate traces for emergency access.
- The system must be configured to allow tracing and logging of user actions.
- The correct date format must be understood if specified, to ensure the `Until Date` is interpreted correctly.

**Error Handling and Troubleshooting:** 

- **Error:** "Until Date parameter is not a valid date"
    - **Cause:** The provided `Until Date` does not match the specified `Date Format` or is not a recognizable date.
    - **Solution:** Ensure the `Until Date` is correctly formatted as per the provided or default `Date Format`. Review the date format documentation if needed.

- **Common Issue:** Trace not starting
    - **Probable Cause:** Incorrect session identifier or user name.
    - **Solution:** Verify the session identifier and username are correct and retry the action.

Remember to review system logs for any additional error messages or warnings that could provide further insight into issues encountered during the execution of the `StartTraceForEmergencyAccess` action.