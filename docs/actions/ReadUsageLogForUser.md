# ReadUsageLogForUser

**Category:** Reporting

**Description:**  
The `ReadUsageLogForUser` action is designed to automate the retrieval of user access logs within a specified date range, catering to auditing and security monitoring needs. The key functionality involves parsing start and end dates from the input, validating these times, and then retrieving the user's access logs for review. If specific dates are not provided or are invalid, the action attempts to calculate a fallback range based on additional parameters, allowing for flexibility in report generation. The action encapsulates a critical component of the identity and GRC platform by simplifying the access review process and enabling better oversight of user activities.

**Parameters:**

*Basic*:

- Name: ReadUsageLogForUser_StartDate
    - Description: Defines the start date for the log retrieval range.
    - Default value: None
    - Mandatory: No

- Name: ReadUsageLogForUser_EndDate
    - Description: Specifies the end date for the access log search.
    - Default value: None
    - Mandatory: No

- Name: ReadUsageLogForUser_Username
    - Description: The username for which the access log will be retrieved. If left blank, the system will attempt to use a contextually relevant username.
    - Default value: None
    - Mandatory: No

*Advanced*:

- Name: ReadUsageLogForUser_DateFormat
    - Description: Specifies the date format to be used for parsing provided start and end dates, enhancing flexibility in date representation.
    - Default value: None
    - Mandatory: No

- Name: ReadUsageLogForUser_TimeTypeDefinition
    - Description: Allows specifying a unit (Days, Hours, Minutes) to dynamically determine the date range based on the current date and provided amount, facilitating relative date range queries.
    - Default value: None
    - Mandatory: No

- Name: ReadUsageLogForUser_Amount
    - Description: Specifies the amount to adjust the current date by, according to the Time Type Definition, for calculating dynamic date ranges.
    - Default value: None
    - Mandatory: No

**Business impact:**  
This action significantly enhances the security posture by providing detailed insights into user activities, enabling timely audits and reviews. It supports compliance by automating the retrieval of necessary logs that can prove adherence to various regulations and internal policies. Efficient log access assists in rapid analysis and decision-making regarding user access and activities, contributing to the overall risk management framework.

**Example of usage:**  
To generate a report for a user's activity in the last 30 days:

```csharp
var parameters = new WorkflowActionParameters
{
    { "ReadUsageLogForUser_TimeTypeDefinition", "Days" },
    { "ReadUsageLogForUser_Amount", "30" },
    { "ReadUsageLogForUser_Username", "jdoe" }
};
var readUsageLogAction = new ReadUsageLogForUser();
readUsageLogAction.Perform(parameters);
```

**Prerequisites:**  
- Proper system access rights to execute log retrieval actions.
- Understanding of the available parameters and their formats.

**Error Handling and Troubleshooting:**  
- **Issue**: Logs not retrieved for the specified time range.  
  **Cause**: Incorrect date format or unparseable dates provided.  
  **Solution**: Verify the date format parameter and the correctness of the start and end date values.

- **Issue**: `Missing Dates data` exception.  
  **Cause**: Neither specific dates nor time type definitions provided.  
  **Solution**: Ensure either the specific start and end dates are provided or a valid time type definition and amount are given.

- **Issue**: `Amount should be a number` exception.  
  **Cause**: Non-numeric value passed to the "Amount" parameter.  
  **Solution**: Confirm the amount is a valid number corresponding to the time type definition.

