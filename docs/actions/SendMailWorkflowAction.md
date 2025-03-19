Action name: SendMailWorkflowAction

**Category:** Communication

**Description:** The SendMailWorkflowAction is designed to automate the process of sending emails based on predefined templates within the Pathlock Cloud platform. This action facilitates communication by using specific email templates along with parameters collected from user forms to generate and send customized email messages. When executed, the action fetches an email template by ID, compiles the message with relevant parameters, and dispatches it to specified recipients. This streamlined communication process is essential for notifying users or stakeholders about important updates or actions required, within GRC (Governance, Risk Management, and Compliance) contexts such as PAM (Privileged Access Management), Access Requests, or Risk Calculations.

**Parameters:** 

_Basic:_

    Name: SendMailWorkflowAction_TemplateId
    Description: The unique identifier for the email template to be used. This parameter is crucial as it determines the layout and content of the email to be sent. It is used to fetch the template details from the database.
    Default value: N/A
    Mandatory: yes
    
    Name: SendMailWorkflowAction_MailRecipent
    Description: The recipient's email address. This parameter specifies who will receive the email. It supports a single recipient as per the current implementation.
    Default value: N/A
    Mandatory: yes

_Advanced:_

    (No advanced parameters specified)

**Business impact:** Efficient and automated email communication is vital in any GRC platform, as it ensures timely notifications are sent to users regarding their access rights, compliance status, or risk assessments. The SendMailWorkflowAction simplifies the process of sending tailored communications, which is critical for maintaining robust security and compliance standards within an organization. It enables the platform to keep stakeholders informed, supports audit trails by documenting sent messages, and enhances user engagement through personalized communication.

**Example of usage:** An example scenario for using the SendMailWorkflowAction could involve a user requesting access to a specific resource. Upon approval of the request, this action could be triggered to send a confirmation email to the user, using a predefined template that includes details of the granted access and any necessary instructions or conditions.

**Prerequisites:** To successfully use this action, the following prerequisites must be met:

- A valid email template ID that exists within the system's database.
- The recipient's email address must be correctly specified in the action parameters.
- Proper configuration of the email server settings to ensure emails can be sent successfully.

**Error Handling and Troubleshooting:** 

1. **Template Not Found**: If the specified email template ID does not exist, an error will be logged stating that no email template was found. Ensure the template ID is correct and exists in the system.
   
2. **Failure to Send Email**: If there's an issue sending the email (such as a configuration issue with the mail server or invalid recipient email), it's essential to verify the mail server settings and ensure the recipient's email address is valid and correctly entered.

3. **Parameter Misconfiguration**: Ensure all mandatory parameters are correctly populated to avoid runtime errors. Missing or incorrect parameters will prevent the action from executing as intended.