Action Name: **StartAuthorizationReviewBasedOnTemplate**

**Category:** Workflow

**Description:** 

This action is designed to initiate an Authorization Review process based on a predefined template. The process involves initializing the workflow context, creating a new authorization review record in the database, notifying approvers (if applicable), and updating workflow parameters with the results. This action automates the process of reviewing user access and rights within an organization, ensuring that only authorized users have access to specific systems or data, in line with compliance and security policies.

**Parameters:** 

_Basic:_

- **Name:** IsNotifyApprovers
    - **Description:** A boolean flag indicating whether approvers should be notified upon the creation of a new authorization review. In the workflow, this parameter dictates whether the notification logic for approvers is executed.
    - **Default value:** None (depends on workflow configuration).
    - **Mandatory:** Yes

_Advanced:_

- **Name:** SystemId
    - **Description:** Represents the unique identifier of the system for which the authorization review is being created. It is used to initialize the context for the review process.
    - **Default value:** None (must be supplied at runtime).
    - **Mandatory:** Yes

**Business impact:** 

Implementing this action in your workflow significantly enhances security and compliance postures by ensuring regular and systematic reviews of user access rights. It supports governance, risk management, and compliance (GRC) initiatives by automating the process of validating that the principle of least privilege is adhered to, thereby reducing unauthorized access risks.

**Example of usage:** 

To use this action in a workflow, define it as part of your sequence when setting up or updating authorization review processes. For instance, as part of a quarterly compliance check, configure the workflow to trigger this action, specifying whether to notify approvers based on the organization’s policies for the current review cycle.

**Prerequisites:** 

Users must have appropriate permissions to initiate authorization reviews and to execute workflow actions. Additionally, a valid system identifier (SystemId) and template for the authorization review process must be pre-defined in the system.

**Error Handling and Troubleshooting:** 

- **Error:** "No review created" 
    - **Cause:** This error may occur if the action is unable to create a new authorization review record in the database.
    - **Solution:** Check the database connectivity and permissions. Ensure that the `SystemId` is correct and refers to an existing system in your organization.

Common issues may involve configuration errors or missing parameters. Review the workflow configuration and ensure all mandatory parameters are correctly set. For connectivity issues, verify the database server status and network configurations.