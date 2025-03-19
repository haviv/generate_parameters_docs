Action name: MassUploadWorkflowAction

**Category:** Workflow

**Description:**

The `MassUploadWorkflowAction` class is designed to handle mass upload processes within the identity and GRC (Governance, Risk Management, and Compliance) platform of Pathlock Cloud. This action automates the process of uploading, formatting, and processing large volumes of data based on predefined parameters and system settings. The core functionality revolves around reading data from attachments (specifically focusing on CSV files or formats that require specific handling), validating, and importing this data into the designated system. The action predicates its operation on the existence of a file attachment, system identification, and formatting instructions, culminating in either a successful upload process or error logging for troubleshooting.

**Parameters:**

Basic Parameters:

- Name: UseOverideMethod
- Description: Determines whether the action should use an override method during the data import process. This parameter guides the conditional logic on how data is processed, impacting the manipulation or transformation applied to the data before final upload.
- Default value: not specified (depends on runtime evaluation)
- Mandatory: no

- Name: RunOnSystem
- Description: Specifies the target system name where the upload process should be executed. This is pivotal in identifying the correct system context and executing related operations such as data validation and import according to system-specific constraints.
- Default value: System description from WorkflowInstance.RequestSystemId
- Mandatory: no

- Name: FileName
- Description: The name of the file to be processed. This parameter is critical for locating the file within the system or attached files for processing.
- Default value: The most recently uploaded file’s name, if not explicitly provided.
- Mandatory: no

- Name: OutputFormat
- Description: Specifies the format in which the output, particularly logging of processed data, should be generated. This influences how feedback and summaries of the upload process are presented to the user.
- Default value: "{0} {2}/{1}"
- Mandatory: no

**Business impact:**

The `MassUploadWorkflowAction` plays a vital role in facilitating bulk data management operations within the organization, significantly reducing manual data entry and processing errors. It streamlines the integration and harmonization of data across different systems, enhancing efficiency in identity management, access governance, and compliance reporting. Efficient mass uploads directly contribute to time savings, accuracy, and overall operational resilience.

**Example of usage:**

An HR department needs to update access rights for hundreds of users due to an organizational restructuring. By utilizing the `MassUploadWorkflowAction`, they can compile the necessary updates into a single file, specify the target system, and execute the upload. This process ensures that all changes are reflected accurately and promptly across the necessary platforms with minimal manual intervention.

**Prerequisites:**

- The user must have administrative privileges or the necessary permissions to perform uploads on the target system.
- A valid file (preferably in CSV format for optimal processing) must be attached or specified before the action is initiated.
- System identification (RunOnSystem) must match an existing system configured within the Pathlock Cloud environment.

**Error Handling and Troubleshooting:**

- **Missing File:** If no filename is provided or the file cannot be located, the action will fail with a "Data file is missing" message. Ensure that the file name is correctly specified and that the file has been properly attached.
- **System Identification Failure:** If the specified system cannot be found or initialized, verify that the `RunOnSystem` parameter matches an existing system's description or ID accurately.
- **Data Processing Errors:** Errors during the data upload process, including format mismatches or override method issues, will be logged. Review the output and error messages for specifics and adjust the CSV format or processing parameters accordingly.