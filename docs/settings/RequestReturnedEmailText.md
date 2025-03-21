# Request Returned Email Text

**Technical Name:** RequestReturnedEmailText

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The RequestReturnedEmailText parameter is used to customize the email content sent to users when a request is returned in the Pathlock Cloud GRC platform. The configuration influences how recipients perceive and action returned requests, thereby impacting the request review process.

**Business Impact:**

Customizing this email text can significantly enhance communication efficiency within the GRC processes. Timely and clear notifications can help in faster resolution of returned requests, directly impacting compliance management and oversight capabilities.

**Technical Impact when configured:**

When configured, this parameter customizes the email notification sent to a group or a manager stating that a request has been returned for further action. This can include links to approve, reject, or move back the request, providing a direct call to action within the email itself.

**Examples Scenario:**

A user submits a request for accessing a high-risk financial report. The request is reviewed but needs additional information; hence, it's returned. The RequestReturnedEmailText is configured to include guidance on what information is needed and provides direct links for resubmission, streamlining the process for both the requester and the approver.

**Related Settings:**

- RequestOpenedEmailText

**Best Practices:** 

- **Configure when:** You want to ensure that returned requests are acted upon quickly and efficiently. Customization should aim to make it clear why the request was returned and what the next steps are.
  
- **Avoid when:** Default settings suffice for general notification purposes, or if email customization could lead to confusion due to poorly drafted content.