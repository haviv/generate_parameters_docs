**Help Desk System Url**

**Technical Name:** HelpDeskSystemUrl

**Category:** Configuration

**Default Value:** 

**Impact Level:** High

**Description:**

The Help Desk System Url parameter specifies the base URL for integrating with a Help Desk or ticketing system, enabling automated ticket opening and management directly from within the Pathlock Cloud GRC platform. This setting is essential for organizations leveraging ServiceNow for incident management and request fulfillment processes related to security, risk, and compliance issues identified by Pathlock.

**Business Impact:**

Configuring the Help Desk System Url correctly ensures seamless integration between Pathlock Cloud GRC and the ServiceNow ticketing system. This integration facilitates automated creation, tracking, and resolution of security, risk, and compliance-related incidents, minimizing manual intervention and accelerating response times to potential threats or policy violations.

**Technical Impact when configured:**

Once configured, the Help Desk System Url enables the automatic generation of ServiceNow tickets from the Pathlock platform whenever a relevant workflow action, such as `OpenServiceNowServiceRequest`, is triggered. This process includes populating the ticket with essential details such as the user who initiated the workflow, the type of request, and a unique identifier for tracking within the GRC platform.

**Examples Scenario:**

If a user attempts to access a sensitive system or data that violates a predefined access control policy within Pathlock, an incident is automatically generated. With the Help Desk System Url configured, a ServiceNow ticket is immediately opened, containing all relevant incident details, including the involved user, the nature of the policy violation, and the specific access request ID. This ticket then allows IT and security teams to quickly investigate and resolve the incident directly through their ServiceNow instance.

**Related Settings:** N/A

**Applicable Workflows Actions:** 

- OpenServiceNowServiceRequest

**Best Practices:** configure when integrating Pathlock Cloud GRC with ServiceNow or a similar IT service management (ITSM) tool to automate ticketing. Avoid when no formal ITSM process or tool is in place for handling GRC-related tasks.