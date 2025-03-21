# Custom Report Wasn't Found Error Message

**Technical Name:** CustomReportWasntFoundErrorMessage

**Category:** Reporting

**Default Value:** 

**Impact Level:** High

**Description:**

This parameter defines the error message displayed when a custom report cannot be found or loaded within the Pathlock Cloud GRC platform. It is crucial for guiding users when there's an issue accessing or locating specified reports.

**Business Impact:**

Having a clear and informative error message prevents user frustration and helps in diagnosing issues with report accessibility or existence. It ensures users are not left in the dark about what went wrong, enabling them to quickly understand the problem and take corrective actions or seek help.

**Technical Impact when configured:**

Proper configuration of this parameter can significantly reduce support tickets related to report accessibility issues. It enables a self-service troubleshooting approach for users by providing immediate, context-relevant feedback.

**Examples Scenario:**

A user attempts to access a custom report by ID or title that has either been deleted, moved, or renamed. Instead of a generic error or no feedback, the system displays the configured error message, informing the user that the specific report could not be found.

**Related Settings:**

- `CopySystem_SameSourceAndDest`
- `ResourceManager.GetString`
- `CustomQueryColumnsGeneratorWithCopy`

**Best Practices:** configure when, avoid when 

- Configure this parameter with a clear, non-technical message that guides the user to possible next steps or actions they can take.
- Avoid using technical jargon or codes that may not be easily understood by the end user.