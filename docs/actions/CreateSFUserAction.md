Action Name: CreateSFUserAction

**Category:** User Management

**Description:** 

The CreateSFUserAction class is designed to automate the creation of users within SAP's SuccessFactors (SF) by extending the IWorkflowAction interface and implementing the Perform method. The action initializes the Security Protocol to TLS 1.2, establishes a connection using SAP credentials, and leverages SuccessFactors REST APIs for data manipulation. It dynamically builds JSON payloads for creating or updating different SF entities (e.g., User, PerPerson, EmpEmployment) based on the provided parameters, translating field values using picklists where necessary. The action supports both creating new users with auto-generated IDs and updating existing users, handling boolean, date fields, and custom entity processing with extensive error logging for troubleshooting.

**Parameters:**

Basic:

- Name: sfBaseUrl
  - Description: The base URL for the SuccessFactors API. This parameter overrides the default base URL to allow for custom API endpoints.
  - Default value: "https://api10.successfactors.com/odata/v2/"
  - Mandatory: No

- Name: FieldTranslations
  - Description: Semi-colon separated string pairs for field translation, e.g., "fieldKey:fieldEntity". Translates field values based on SuccessFactors picklists to ensure data integrity.
  - Default value: N/A
  - Mandatory: No

Advanced:

- Name: sfBooleanFields
  - Description: Comma-separated list of field names that should be treated as Boolean. These fields are converted to true/false in the JSON payload based on their content.
  - Default value: N/A
  - Mandatory: No

- Name: sfDateFields
  - Description: Comma-separated list of field names that should be treated as Date objects. These fields are converted to the appropriate date format for JSON payload.
  - Default value: N/A
  - Mandatory: No

- Name: SF_Entities
  - Description: Additional custom SuccessFactors entities to be created or updated as part of the workflow. Specified as comma-separated values, indicating the entity name and metadata.
  - Default value: N/A
  - Mandatory: No

- Name: disableAutoUserId
  - Description: Flag to disable automatic generation of user and person external IDs, allowing for manual specification.
  - Default value: false
  - Mandatory: No

**Business impact:**

The CreateSFUserAction simplifies and streamlines the management of user identities in SuccessFactors, facilitating efficient onboarding, offboarding, and updates to user information. By automating these processes, it reduces manual errors, ensures data consistency, and improves security compliance. It supports both granular and bulk user operations, enhancing the overall effectiveness of identity and access management strategies within the organization.

**Example of usage:**

An organization needs to bulk import new employees from an HR system into SuccessFactors. The CreateSFUserAction can be configured with the necessary parameters, such as sfBaseURL, FieldTranslations, and entity-specific fields. The workflow action then automatically creates or updates user records in SuccessFactors, translating and mapping data as required, potentially triggering additional workflows for access provisioning based on the roles and permissions defined.

**Prerequisites:**

- Valid SuccessFactors API credentials (username and password) must be configured in the Pathlock platform for authentication.
- Knowledge of the required SuccessFactors entities and fields for user creation or update.
- Appropriate network access permissions to reach the SuccessFactors API endpoints from Pathlock Cloud.
  
**Error Handling and Troubleshooting:**

Common error scenarios include:

- Invalid API credentials: Ensure the SAPUserName and SAPPassword are correctly specified in ProfileTailorContext.
- Incorrect or unreachable sfBaseUrl: Verify the base URL is accessible and correct.
- Translation errors due to incorrect FieldTranslations setup: Check the format and values specified for field translations.
- API rate limits or timeouts: Implement retry logic or increase the timeout duration.

For each type of error, consult the Pathlock Cloud log files for detailed exception information. Common.Logger functionality is utilized throughout the creation process for detailed error logging and tracing.