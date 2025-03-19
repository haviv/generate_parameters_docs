# StartAuthorizationReviewBasedOnFileAttachment

**Category:** Workflow

**Description:** This action initiates an authorization review process based on file attachments. It leverages information from specified file attachments to populate and start the authorization review. Key elements include identifying the workflow type, generating a review with a title, and utilizing an email template for notifications related to the review. The core flow involves reading an attached file (e.g., an Excel sheet defined by 'FileSheetName'), extracting relevant data, and using this data to initiate the authorization review process.

**Parameters:**

- Basic:
    - Name: Workflow Type name
        - Description: Specifies the type of workflow to be initiated for the authorization review.
        - Default value: N/A
        - Mandatory: yes

    - Name: Title
        - Description: The title for the authorization review process, used for identification and notification purposes.
        - Default value: N/A
        - Mandatory: yes

    - Name: Mail Template
        - Description: Defines the email template used for notifications within the authorization review process.
        - Default value: N/A
        - Mandatory: yes

- Advanced:
    - Name: FileSheetName
        - Description: The name of the sheet within the file to be used for extracting data necessary for the review process.
        - Default value: N/A
        - Mandatory: no

**Business impact:** By automating the initiation of authorization reviews based on file attachments, this action streamlines access and compliance processes within the organization. It helps ensure that user access rights are regularly reviewed and updated according to current needs and compliance requirements, enhancing overall security and governance.

**Example of usage:** In a scenario where regular authorization reviews are required to maintain compliance with internal policies and regulations, this action can be triggered after a compliance report is uploaded as a file attachment. The workflow automatically reads the attachment, extracts the necessary information, and initiates a review process without manual intervention, thereby saving time and reducing errors.

**Prerequisites:** Before executing this action, the user must ensure that the workflow type, title, and email template are correctly defined in the system. The file to be attached should be properly formatted according to the expected structure, especially if the 'FileSheetName' parameter is used.

**Error Handling and Troubleshooting:**
- Common error scenario: Workflow type not found.
    - Probable cause: The specified workflow type name does not exist.
    - Solution: Verify that the workflow type name is correctly defined in the system.

- Common error scenario: Email template not found.
    - Probable cause: The specified email template does not exist.
    - Solution: Ensure the email template is correctly defined and named in the system.

- Common error scenario: File attachment not readable.
    - Probable cause: The attachment is improperly formatted or corrupted.
    - Solution: Check the file format and ensure it complies with the expected structure. Verify that the file is not corrupted before attachment.