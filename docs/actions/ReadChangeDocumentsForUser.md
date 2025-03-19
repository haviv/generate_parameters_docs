Action name: ReadChangeDocumentsForUser

**Category:** Workflow

**Description:**

The ReadChangeDocumentsForUser action is designed to retrieve and store change documents for a specific user within the Pathlock Cloud's Identity and Governance, Risk, and Compliance (GRC) platform. This action automates the process of collecting changes made by or affecting a user's account, focusing on modifications from a specified date or within a specific timeframe. The workflow initiates by determining the relevant user and establishes the context based on the user's system ID. It then evaluates parameters to define the scope of change documents to retrieve - either targeting a specific document, setting a timeframe based on days ago, or specifying a start date. The action supports integration with SAP systems through the BaseSAPWASConnector, allowing for specialized document retrieval in SAP environments. This automation facilitates continuous monitoring and auditing of user-related changes, crucial for compliance, security, and risk management.

**Parameters:**

Basic:
- Name: ReadChangeDocumentsForUser_SpecificChangeDocument
  Description: Specifies a unique identifier for a change document. If provided, the system will only retrieve this document.
  Default value: None
  Mandatory: No
- Name: ReadChangeDocumentsForUser_SpecificDaysAgo
  Description: Defines the number of days before the current date to start retrieving change documents. This parameter recalculates the 'fromDate' to fetch documents from.
  Default value: None
  Mandatory: No

Advanced:
- Name: ReadChangeDocumentsForUser_FromSpecificDate
  Description: Allows setting a specific start date for retrieving change documents, overriding the default behavior of using the workflow instance's open date. This parameter enables precise control over the date range for document retrieval.
  Default value: None
  Mandatory: No

**Business impact:**

Implementing the ReadChangeDocumentsForUser action significantly enhances an organization's ability to monitor, audit, and comply with internal and external regulations regarding user account changes. By automating the retrieval and storage of change documents, companies can ensure they have a comprehensive and easily accessible log of all modifications. This capability supports efforts in risk management by enabling swift analysis and response to unauthorized or suspicious changes, thereby safeguarding against potential security breaches and ensuring compliance with regulatory standards.

**Example of usage:**

An administrator wants to audit changes made to a high-profile user's account within the last week. By utilizing the ReadChangeDocumentsForUser action with the "ReadChangeDocumentsForUser_SpecificDaysAgo" parameter set to 7, the workflow will automatically fetch and store all change documents related to that user's account from the past 7 days, facilitating a thorough audit and review process.

**Prerequisites:**

- The user executing the action must have permissions to access user data and change logs within the system.
- The system ID for the user must be known and valid.

**Error Handling and Troubleshooting:**

- Error: No documents found for the specified criteria.
  Probable Cause: The specified user has no change documents within the given timeframe or the specific document ID does not exist.
  Recommended Solution: Verify the user ID, document ID, and timeframe for accuracy. Adjust the parameters or provide broader search criteria.

- Error: Invalid date format provided.
  Probable Cause: The input for "ReadChangeDocumentsForUser_FromSpecificDate" does not match the expected date format.
  Recommended Solution: Ensure the date input follows the correct format (e.g., YYYY-MM-DD) and retry the action.