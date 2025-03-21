# Daily EMail Add Link To Waiting Requests

**Technical Name:** DailyEMailAddLinkToWaitingRequests

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter decides whether to include a direct link to any pending requests within the daily email notifications sent to users. When enabled, it aims to streamline the process for users to view and act upon their waiting requests directly from their email inbox, enhancing the efficiency of request management.

**Business Impact:** Enabling this feature can significantly increase the response rate to pending requests, as it reduces the steps a user needs to take to access their tasks. This swift access is crucial for maintaining the pace of request processing and ensuring timely compliance and decision-making processes within the organization.

**Technical Impact when configured:** When enabled, daily email notifications to users will include a direct link to their pending requests in the Pathlock Cloud GRC platform. This modification necessitates ensuring that email templates are correctly set up to include the link and that users have the necessary permissions to view and act on the requests directly from the email.

**Examples Scenario:** A user receives a daily notification email indicating there are pending access requests awaiting their approval. With the DailyEMailAddLinkToWaitingRequests parameter enabled, the email includes a direct link. The user clicks on this link, is authenticated into the Pathlock platform, and is taken directly to the list of waiting requests, where they can perform necessary actions much faster than navigating through the application interface without direct access.

**Related Settings:** NA

**Best Practices:** 
- Configure when: You have a well-defined process for handling requests and want to streamline the decision-making process by making it easier for users to access their pending requests.
- Avoid when: Users do not have consistent access to their emails or the necessary permissions to view and act on requests directly from an email link, which could lead to confusion or security concerns.