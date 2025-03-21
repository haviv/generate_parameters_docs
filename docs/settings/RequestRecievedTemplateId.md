# Request Received Template

**Technical Name:** RequestRecievedTemplateId

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:** 

This parameter defines the template ID used for generating emails when a request is received within the Pathlock Cloud GRC platform. The template determines the format and content of the notification sent to users when their requests are received, ensuring clear communication and action upon requests.

**Business Impact:** 

Configuring the correct template ID enhances the user experience by providing timely and relevant communication regarding their requests. It ensures that users are promptly informed about their request status, which is critical for maintaining operational efficiency and compliance in business processes. An appropriate template ensures clarity, reduces the need for follow-up inquiries, and drives faster decision-making.

**Technical Impact when configured:** 

With the appropriate template ID configured, the platform can automatically send out notification emails to the designated recipients when a request is received. This automation reduces manual intervention, ensuring that notifications are consistently sent out without delay. It also reduces the risk of human error in communication.

**Example Scenario:** 

For instance, a user submits a request for access to a sensitive financial report. Upon receiving this request, the platform utilizes the specified Request Received Template to send a notification email to the user, confirming the receipt of the request and outlining the next steps or estimated processing time. This immediate feedback loop enhances user satisfaction and trust in the process.

**Related Settings:** 

- Send Workflow Mails in Advanced Configuration.
- RequestApprovedTemplateId

**Best Practices:** configure when the platform is set up to manage a significant volume of requests to ensure users are always informed. Avoid configuration without customizing the template to reflect the specific communication standards and information requirements of your organization.