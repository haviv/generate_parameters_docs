Action Name: OpenServiceNowTicket

**Category:** Workflow

**Description:** 

The `OpenServiceNowTicket` action is designed to automate the process of creating service tickets in ServiceNow via Pathlock's workflow engine. When executed, this action establishes a connection with ServiceNow using predetermined credentials and creates a new ticket based on the parameters provided. Essential details such as the ticket number and ID for API usage are captured from the response and made available to the workflow context. This automation facilitates seamless integration of incident or request management processes within the broader GRC and identity management framework offered by Pathlock Cloud.

**Parameters:** 

*Basic Parameters:*

- Name: ServiceRequestComment
    - Description: A brief comment or note associated with the service request ticket.
    - Default value: None
    - Mandatory: Yes

- Name: ServiceRequestDescription
    - Description: Detailed description of the service request or issue to be addressed via the ServiceNow ticket.
    - Default value: None
    - Mandatory: Yes

*Advanced Parameters:*

(No advanced parameters are defined for this action.)

**Business impact:**

The creation of ServiceNow tickets through this action streamlines the incident and request management processes, ensuring timely and organized response to IT service needs. Automating ticket creation directly from Pathlock Cloud reduces manual intervention, accelerates resolution times, and enhances the user experience for administrators and end users. This ability to automate workflow tasks significantly impacts operational efficiency and service management effectiveness within organizations leveraging Pathlock Cloud alongside ServiceNow.

**Example of usage:** 

An example scenario involves an automated workflow triggered by a specific event or user request within Pathlock Cloud, such as a detected access violation or a request for additional access rights. The workflow includes the `OpenServiceNowTicket` action configured with appropriate parameters to create a ticket in ServiceNow, automatically populating the ticket description and comments with relevant event details or request information.

**Prerequisites:** 

- ServiceNow instance must be accessible via the network settings defined in `CommonSettings.Default.HelpDeskSystemUrl`.
- Valid ServiceNow credentials (username and password) must be configured in `CommonSettings.Default.HelpDeskSystemUser` and `CommonSettings.Default.HelpDeskSystemPassword`.
- The user executing the workflow must have permissions to create tickets in the target ServiceNow instance.

**Error Handling and Troubleshooting:** 

- **Error creating ticket:** Verify that the ServiceNow URL and credentials in `CommonSettings` are correct and that the ServiceNow instance is accessible.
- **Missing parameters:** Ensure both `ServiceRequestComment` and `ServiceRequestDescription` parameters are provided and contain valid information.
- **Connectivity issues:** Check network connectivity and firewall settings to ensure the ServiceNow instance is reachable from the Pathlock Cloud environment.
