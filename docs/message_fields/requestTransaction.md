**Field Name:** requestTransaction

**Description:** The `requestTransaction` field represents a formatted description of the transaction involved in a workflow process. This field provides context and details regarding the transaction for which the approval or other actions are being requested in the workflow. It is used to inform recipients of the specific transaction details that are under review or action in the email templates.

**Usage Context:** The `requestTransaction` field is typically used in email templates associated with the workflow process to notify users about a transaction that requires approval or has been initiated. It is included in emails as part of the necessary information to give recipients insight into what transaction is being referred to without requiring them to access the workflow system directly. It is particularly relevant when transactions are related to specific requests, roles, or SAP activities processed within Pathlock Cloud workflows.

**Example:** 

    Transaction Details: $$requestTransaction$$

    After rendering:

    Transaction Details: Travel Expense Approval for Q3 2023