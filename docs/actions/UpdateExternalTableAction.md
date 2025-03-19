# UpdateExternalTableAction

**Category:** Configuration

**Description:** The `UpdateExternalTableAction` is designed to manipulate records within an external table by performing operations such as create, update, insert, or delete based on the specified parameters. Upon execution, it determines the action to take (update, insert, delete) and applies the necessary changes to the external table. This process includes validating if the specified action is achievable and logging the changes or failures accordingly. This action allows for dynamic interaction with database tables, useful for managing data external to the core system but integral to its operation and reporting.

**Parameters:**

_Basic Parameters:_

- Name: ExternalTableName
  - Description: Specifies the name of the external table to be manipulated.
  - Default value: N/A
  - Mandatory: Yes

- Name: ExternalTableKeyColumns
  - Description: Defines the key column(s) in the external table that are used to identify the record for the update or delete operation.
  - Default value: N/A
  - Mandatory: Yes

- Name: ActionOperation
  - Description: Determines the type of operation to be performed (Create, Update, Update or Insert, Delete) on the external table.
  - Default value: Empty (No operation)
  - Mandatory: Yes

_Advanced Parameters:_ (none specified)

**Business impact:** Streamlining operations such as updating, deleting, or inserting records into external tables directly impacts the efficiency of data management within Pathlock Cloud. This has implications for access control, risk assessment, and compliance reporting by ensuring that external data representations are accurate and current. For instance, modifying access permissions in an external table can reflect immediate changes in user access management without manual intervention, reinforcing security and compliance posture.

**Example of usage:** Suppose an organization needs to update the access level of a user in an external table named `AccessControl`. They can perform an "Update" action specifying the table name (`AccessControl`), key columns (e.g., `UserID`), and operation (`Update`) along with the new access level details. Similarly, if a new risk assessment model necessitates adding records to an external risk calculation table, the Create action can be utilized.

**Prerequisites:** Users must have appropriate permissions to access and perform operations on the external tables. Additionally, knowledge of the external table schema (i.e., table name and key columns) is necessary to define operations accurately.

**Error Handling and Troubleshooting:**

- **RowNotInTableException:** If the action is `UpdateOrInsert` and the target row does not exist, the system attempts to insert the new record. If insertion fails, check for incorrect table name or key columns, and validate that all required data for insertion is provided.
- **Update or Delete with No Changes:** If an update or delete operation reports “No changes affected,” verify the accuracy of key columns and that the specified data changes or deletion criteria match existing records.
- **General Failure Messages**: For failures like "No update was done," confirm the table exists, the key columns are correctly identified, and the operation parameters are compatible with the table schema.