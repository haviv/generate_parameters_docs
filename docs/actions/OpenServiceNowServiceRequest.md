Action Name: OpenServiceNowServiceRequest

**Category:** User Management

**Description:** The OpenServiceNowServiceRequest action is designed to automate the creation of service requests within the ServiceNow platform directly from the Pathlock Cloud workflow engine. When invoked, this action establishes a connection to the ServiceNow instance using predefined service account credentials. It then creates a new service request based on the provided Service Catalog Id and Service Request Comment, alongside any additional parameters captured in the workflow context. Upon successful creation, the action captures and stores the new ticket's number and API-use ticket ID back into the Pathlock Cloud workflow for further processing or reference.

**Parameters:**

*Basic:*

- Name: ServiceCatalogId
- Description: This is the identifier for the Service Catalog item in ServiceNow under which the request will be filed. It determines the type of service request being raised.
- Default value: N/A
- Mandatory: yes

- Name: ServiceRequestComment
- Description: A comment or note providing additional context or details for the service request. It is included in the request when it is created in ServiceNow.
- Default value: N/A
- Mandatory: yes

*Advanced:*

N/A

**Business impact:** Automating service request submissions through the OpenServiceNowServiceRequest action streamlines support operations and access management processes, significantly reducing manual overhead and improving response times for service requests. It ensures timely action on critical tasks such as access provisioning, password resets, or software installations, thereby enhancing overall operational efficiency and user satisfaction.

**Example of usage:** Considering a scenario where an end user requires access to a specific application, they can initiate a workflow in Pathlock Cloud. This workflow, upon reaching the OpenServiceNowServiceRequest action, would automatically raise a service request in ServiceNow for the IT helpdesk to grant the necessary application access, without the user needing to manually navigate and fill out the service request form in ServiceNow.

**Prerequisites:** The Pathlock Cloud environment must have network access to the ServiceNow instance. The service account credentials used by the action (configured in CommonSettings) must have the necessary permissions in ServiceNow to create service requests.

**Error Handling and Troubleshooting:**

- Common error: "Authentication failure"
  - Probable cause: Incorrect service account credentials.
  - Recommended solution: Verify the service account username and password configured in CommonSettings.
  
- Common error: "ServiceCatalogId not found"
  - Probable cause: An invalid ServiceCatalogId was provided.
  - Recommended solution: Ensure the ServiceCatalogId matches an existing item in the ServiceNow Service Catalog.

- Common error: "Unable to connect to ServiceNow instance"
  - Probable cause: Network issues or incorrect ServiceNow instance URL.
  - Recommended solution: Verify the ServiceNow instance URL in CommonSettings and ensure the network allows communication between Pathlock Cloud and ServiceNow.