# Show File Upload Technical Error

**Technical Name:** ShowFileUploadTechnicalError

**Category:** General - UI

**Default Value:**

**Impact Level:** Medium

**Description:**

The Show File Upload Technical Error parameter determines whether technical error messages are displayed to the user during file upload processes within the Pathlock Cloud GRC platform. This setting enhances user understanding of issues encountered during file uploading by providing specific, technical feedback.

**Business Impact:**

Enabling detailed technical error messages for file uploads can help users troubleshoot issues more efficiently, reducing downtime and support requests. However, it may also expose sensitive system information if not managed properly. Appropriate use of this setting balances operational transparency with security considerations.

**Technical Impact when configured:**

When enabled, users encounter clear, technical descriptions of errors during the file upload process, allowing for self-resolution or more informed support requests. This can lead to improved user experience and reduced burden on support teams. Conversely, if not adequately controlled, there could be unintended disclosure of system details through error messages.

**Examples Scenario:**

A user tries to upload a file containing characters not allowed by the system's configuration. Instead of a generic "Upload Failed" message, the system specifies the reason, e.g., "File cannot be uploaded due to the presence of restricted characters in the file name."

**Related Settings:**

- AllowedUploadFileTypes
- NotAllowedChractersUploadFile

**Best Practices:** 
- Configure when a detailed technical analysis of upload errors is needed to empower users to self-serve problem resolution.
- Avoid when the user base is not technically inclined or if there is a risk of exposing sensitive system information through error messages.