**Technical Name:** ShowRequestDetailsAsButtonOnPortalPages

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

This parameter controls whether the details of requests within the Pathlock Cloud GRC platform are displayed directly on portal pages as a clickable button. When enabled, it enhances the user interface by allowing users to quickly access detailed information about their requests without navigating away from their current page.

**Business Impact:**

Enabling this feature can significantly improve the user experience for individuals managing or reviewing requests within the Pathlock environment. It streamlines workflow by providing immediate access to request details, reducing the time spent on navigation and search.

**Technical Impact when configured:**

- User interface on portal pages like MyApproverRequests and MyRequestsBootstrap is enhanced with additional bound columns for displaying request details directly.
- Fields such as "Comments" and "WaitingFor" become readily accessible, improving the efficiency of request management and review processes.

**Example Scenario:**

- **Approvals**: An approver can quickly view all relevant details of pending requests, such as comments and waiting period, directly from their dashboard without the need to open each request individually.
- **Audit Trails**: Auditors reviewing request logs can benefit from immediate access to detailed context, improving the efficacy of compliance checks and audits.

**Related Settings:**

- `RoleAdvisorExcludeRolesBusinessProcess`: Although indirectly related, optimizing which roles and processes are excluded can complement the efficient use of ShowRequestDetailsAsButtonOnPortalPages by focusing user attention on relevant requests.

**Applicable Workflows Actions:**

N/A

**Best Practices:** 

- **Configure when**: A quick overview and immediate access to request details are critical for operational efficiency, particularly in environments with a high volume of requests.
  
- **Avoid when**: The additional details may clutter the interface or when the simplicity of the portal pages is a priority over immediate access to detailed information.
