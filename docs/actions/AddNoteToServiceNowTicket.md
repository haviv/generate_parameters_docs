# AddNoteToServiceNowTicket

**Category:** Workflow

**Description:** The AddNoteToServiceNowTicket action allows users to automate the process of adding comments to existing ServiceNow tickets. This action connects to ServiceNow using preconfigured service account credentials and appends a specified comment to a ticket identified by its ticket number. This is particularly useful in scenarios where updates to a ticket need to be automated as part of a larger workflow, making the process efficient and reducing manual effort.

**Parameters:** 

- Basic:
  - **Name:** TicketNumber
    - **Description:** The identifier number of the ticket in ServiceNow to which the comment will be added. This parameter is utilized to locate the specific ticket in ServiceNow and ensure the comment is appended accurately.
    - **Default value:** None
    - **Mandatory:** Yes
  
  - **Name:** ServiceRequestComment
    - **Description:** The content of the comment to be added to the ServiceNow ticket. This parameter allows the user to specify the text that will be appended to the ticket as a note or comment, facilitating clear communication and record-keeping within ServiceNow.
    - **Default value:** None
    - **Mandatory:** Yes

**Business impact:** Implementing this action in workflows significantly enhances the efficiency and reliability of IT ticket management processes. By automating the addition of comments to tickets, companies can ensure timely updates and communications, improving response times and service quality. This capability is especially beneficial in environments where ticket volume is high, or rapid response is critical.

**Example of usage:** Imagine a scenario where a security incident is identified, and an automated workflow is triggered to address the incident. As part of this process, the AddNoteToServiceNowTicket action is utilized to automatically append a comment to the related ServiceNow ticket, informing the IT team of the incident details and actions taken. This ensures that all personnel are informed of the issue and the response in a timely manner.

**Prerequisites:** To execute this action, users must have:

- Access to the Pathlock workflow engine with permissions to configure and execute actions.
- Valid credentials for the ServiceNow instance configured in the `CommonSettings` (ServiceNow API access with rights to read and update tickets).
- A ServiceNow ticket number to which the comment will be added.

**Error Handling and Troubleshooting:**

- **Error:** Comment not added to the ticket
  - **Probable Cause:** Invalid ticket number provided
  - **Solution:** Verify the ticket number is correct and exists in ServiceNow.
  
- **Error:** Authentication failure
  - **Probable Cause:** Incorrect ServiceNow credentials in `CommonSettings`
  - **Solution:** Check and update the ServiceNow credentials in the CommonSettings to ensure they are current and valid.