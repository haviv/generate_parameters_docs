Action Name: MassUploadVerifyWorkflowAction

**Category:** Workflow

**Description:** The `MassUploadVerifyWorkflowAction` is designed to automate the verification process of mass-uploaded data against specified system parameters. It extends the capabilities of `MassUploadWorkflowAction`, focusing on verifying the integrity and compliance of the uploaded data. Once invoked, this action first executes a mass upload operation using the provided file name, system name, original sheet name, and line format. Following this, it proceeds to handle the uploaded sheet by validating each data line against predefined business rules and system-specific constraints, efficiently identifying and reporting any discrepancies or non-compliant records. This action ensures that all uploaded data adheres to the necessary quality and compliance standards before successful integration into the system.

**Parameters:**

- Basic:
    - Name: fileName
    - Description: The name of the file to be uploaded. It is utilized in the initial upload phase to locate and process the specified file for subsequent verification steps.
    - Default value: N/A
    - Mandatory: yes

    - Name: systemName
    - Description: Identifies the target system for which the data is being uploaded. It is crucial for determining the specific validation rules and import logic applicable to the data.
    - Default value: N/A
    - Mandatory: yes

    - Name: originalSheetName
    - Description: Specifies the sheet within the file that contains the data to be verified. It directs the action to the correct dataset for processing and validation.
    - Default value: N/A
    - Mandatory: yes

    - Name: lineFormat
    - Description: Defines the expected format of each data line in the upload. It guides the parsing and validation logic in identifying and reporting format discrepancies.
    - Default value: N/A
    - Mandatory: yes

- Advanced:
    - Parameters within this action are foundational and equally mandatory, leaving none classified as advanced under its current implementation. 

**Business impact:** Implementation of the `MassUploadVerifyWorkflowAction` significantly enhances data integrity and system compliance within Pathlock Cloud. By automating the verification process, it not only optimizes the efficacy and speed at which mass data uploads are conducted but also reduces the risk of errors and non-compliance issues. This action directly supports critical aspects of identity, access management, and governance, risk, and compliance (GRC) strategies by ensuring only valid, compliant data is processed and utilized within the system.

**Example of usage:** An administrator needs to upload a large volume of user access data into the Pathlock Cloud system. They choose the `MassUploadVerifyWorkflowAction` to ensure this bulk upload not only completes successfully but also meets all compliance and format criteria specific to their system setup. 

**Prerequisites:** Users must have appropriate permissions to execute mass uploads and access the specified file path. Additionally, the target file must conform to the accepted structure and format requirements for the action to process correctly.

**Error Handling and Troubleshooting:** 

- Common error scenario: The system outputs "File not found" or "Invalid file path."
    - Probable cause: The `fileName` parameter is incorrect or points to an inaccessible location.
    - Solution: Verify the file name and path are correct and that the executing user has appropriate access permissions.

- Common error scenario: "Sheet validation failed" or "Invalid data format" errors.
    - Probable cause: The uploaded sheet or the data format within it doesn't align with expected standards or system-specific requirements.
    - Solution: Ensure the original sheet name and line format parameters correctly match the structure and format rules defined for the targeted system. Review the uploaded file for any data inconsistencies or format deviations.

By addressing these issues promptly, users can minimize disruptions and ensure smooth operation of the data upload and verification processes within the Pathlock Cloud platform.