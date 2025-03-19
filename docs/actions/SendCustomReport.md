Action Name: SendCustomReport

**Category:** Reporting

**Description:**  
The `SendCustomReport` action is designed to generate and distribute custom reports based on specific workflow parameters. It compiles a report using given parameters, such as report name, title, and recipient details. Depending on the configuration, it can either attach the report to the workflow or send it via email to designated recipients. It supports including both static and dynamically generated content, offering flexibility in addressing various reporting needs. The action involves several steps, including recipient calculation, report generation, and distribution. 

**Parameters:**  
*Basic Parameters:*  
- Name: SendCustomReport_ReportName  
  Description: The name of the report to be generated.  
  Default value: N/A  
  Mandatory: no  

- Name: SendCustomReport_ReportTitle  
  Description: The title of the report. This title is used in the email subject or report file name.  
  Default value: N/A  
  Mandatory: no  

- Name: SendCustomReport_TemplateId  
  Description: The ID of the email template used when sending the report via email.  
  Default value: -1  
  Mandatory: no  

- Name: SendCustomReport_MailRecipient  
  Description: The email addresses of the recipients who will receive the report. Addresses are separated by semicolons (;).  
  Default value: N/A  
  Mandatory: yes  

*Advanced Parameters:*  
- Name: SendCustomReport_CustomReportIds  
  Description: IDs of custom reports to include, separated by commas. Allows for multiple reports to be compiled.  
  Default value: N/A  
  Mandatory: no  

- Name: SendCustomReport_SendMailToWorkflowUser  
  Description: A boolean parameter deciding if the report should be emailed to the current workflow user.  
  Default value: false  
  Mandatory: no  

- Name: SendCustomReport_SendMailToTheAdditionalReferenceUser  
  Description: Decides if the report should be sent to an additional reference user, likely in a managerial or oversight position.  
  Default value: false  
  Mandatory: no  

**Business impact:**  
This action streamlines the distribution of customizable reports related to identity and governance, risk, and compliance (GRC) processes, significantly affecting operational efficiency and decision-making. Timely and targeted report distribution ensures that stakeholders stay informed about critical metrics and status updates, enhancing oversight and enabling quicker responses to potential issues.

**Example of usage:**  
In a scenario where a company needs to send monthly access review reports to department heads and IT administrators, a `SendCustomReport` action could be configured with appropriate report names, titles, and recipient lists. This ensures that each stakeholder receives relevant data for their purview, aiding in compliance and risk management efforts. 

**Prerequisites:**  
- Appropriate permissions to generate and distribute reports.
- Existence of specified report templates and recipient email addresses.
- Workflow must be configured with the necessary parameters to support report generation and distribution.

**Error Handling and Troubleshooting:**  
- **Recipient Email Not Found:** Ensure the provided email addresses are correct and exist in the system.
- **Template ID Invalid:** Verify the template ID corresponds to an existing email template. If -1 is used as a default, no emails will be sent.
- **Custom Report IDs Incorrect:** Check that all custom report IDs provided exist and are accessible by the user.
- **Report Generation Failure:** Double-check report parameters for accuracy and ensure the system has access to all necessary data sources.
