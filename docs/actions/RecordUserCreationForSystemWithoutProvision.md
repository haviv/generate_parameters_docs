Action Name: RecordUserCreationForSystemWithoutProvision

**Category:** User Management

**Description:** This action is designed to log the creation of new users in systems that do not support direct provisioning. It checks if a new username is specified; if not, it defaults to the user's SAP username. Additionally, it supports mapping between UI components and systems, allowing for conditional logging based on these mappings. The action is useful in environments where manual provisioning is the norm, and there's a need to ensure that new user creations are recorded consistently across different systems.

**Parameters:**

*Basic:*

- Name: NewUsername
  - Description: This optional parameter specifies the username of the newly created user. If it is not provided, the workflow will default to using the requesting user's SAP username.
  - Default value: (The requesting user's SAP username)
  - Mandatory: No

*Advanced:*

- Name: SystemToUIMapping
  - Description: This parameter provides a semi-colon delimited string mapping UI component technical names to system names in the format [system name]=[technical name]. It's used to conditionally execute user creation records based on whether the mapped UI component's condition is true.
  - Default value: (None)
  - Mandatory: No

**Business impact:** This action facilitates the automated logging of user account creations in systems not directly covered by automated provisioning solutions, thereby helping maintain compliance with organizational IT security policies. It ensures a reliable audit trail for user creations across different systems, which is crucial for access control and security audits.

**Example of usage:** To record a new user creation in a system without direct provisioning, set the `NewUsername` to the newly created user's username. If you want to conditionally log this event based on specific UI components being true, use the `SystemToUIMapping` to define these conditions. For example, setting `SystemToUIMapping` to "SystemA=ComponentA;SystemB=ComponentB" will only log the creation in SystemA and SystemB if ComponentA and ComponentB conditions are met, respectively.

**Prerequisites:** Before performing this action, ensure that the user running it has appropriate permissions to log user creations in the target system(s). Additionally, ensure that any system names used in the `SystemToUIMapping` parameter are correctly registered in the database with their corresponding technical names.

**Error Handling and Troubleshooting:**

- **Error:** No system found for provided mappings
  - **Cause:** The `SystemToUIMapping` parameter contains a system name that does not exist in the database.
  - **Solution:** Verify the system names provided in the `SystemToUIMapping` parameter against the database entries to ensure accuracy.

- **Error:** NewUsername parameter not set and unable to retrieve SAP username
  - **Cause:** The action cannot default to the requesting user's SAP username because it is not available.
  - **Solution:** Ensure that the `NewUsername` parameter is explicitly provided when the requesting user's SAP username is not available.

